import numpy as np
import datetime
import os,fnmatch
import matplotlib.pyplot as plt
import shapefile
import scipy.fftpack as sf

def distance(p1,p2):
    '''
    tunnel distance between two points (lat,lon,depth) p1 and p2 for Earth as spheroid with a = 6378137.000 and b = 6356752.3142
    
    Parameters
    ----------
    p1 : tupel like 
        (lat1 : float , lon1 : float, h1 : float)
    p2 : tupel like 
        (lat2 : float , lon2 : float, h2 : float)
        
    Returns
    -------
    float
        tunnel distance in meter[m]
    '''
    
    lat1,lon1,h1 = p1
    lat2,lon2,h2 = p2
    
    
    lat=np.deg2rad([lat1,lat2])
    lon=np.deg2rad([lon1,lon2])
    
    a = np.array([6378137.000]) 
    b = np.array([6356752.3142])
    
    N_phi = a*a/np.sqrt(a**2*np.cos(lat)**2+b*b*np.sin(lat)**2)
    
    X = (N_phi+[-h1,h2])*np.cos(lat)*np.cos(lon)
    Y = (N_phi+[-h1,h2])*np.cos(lat)*np.sin(lon)
    Z = ((b**2/a**2)*N_phi+[h1,h2])*np.sin(lat)
    
    return np.sqrt(np.diff(X)**2+np.diff(Y)**2+np.diff(Z)**2)

def energy_area(p1,p2):
    '''
    Area to which energy will be radiated between two points p1 and p2 for Earth as spheroid with a = 6378137.000 and b = 6356752.3142
    
    Parameters
    ----------
    p1 : tupel like 
        (lat1 : float , lon1 : float, h1 : float)
    p2 : tupel like 
        (lat2 : float , lon2 : float, h2 : float)
        
    Returns
    -------
    float
        area in  square meter[m**2] 
    '''
    r=distance(p1,p2)
    _,_,h1 = p1
    _,_,h2 = p2
    
    dT=h1+h2
    h=r-dT
    Marea=np.pi*2*r*h
    O=4*np.pi*r*r
    return (O-Marea)

def energy(A,E,sf,AVS30,Vs400,rho):
    '''
    calculates and corrects energy at station for distance and site parameter
    
    Parameters
    ----------
    A : float
        Area of radiated energy
    E : float
        Energy from velocity traces not corrected: sum(Z**2+N**2+E**2)
        
    sf : float
        sample frequency of traces
    
    AVS30 : float
        vs value under the station
    
    Vs400 :
        site amplification under the station
            
    rho:
        density under the station
        
    Returns
    -------
    float
        corrected Energy A*E/sf*AVS30*rho/Vs400**2
    
    References
    ----------
    Von Specht, S., Ozturk, U., Veh, G., Cotton, F., & Korup, O. (2019). "Effects of finite source rupture on landslide triggering: The 2016 Mw 7.1 Kumamoto earthquake." Solid Earth, 10(2), 463–486. https://doi.org/10.5194/se-10-463-2019
    '''
    return A*E/sf*AVS30*rho/Vs400**2

def arias_intensity(trace,sr,percentile):
    '''
    calculates arias intensity for single trace
    
    Parameters
    ----------
    trace : ndarray
        acceleration in [m/(s**2)]
        
    sr : float
        sample rate of trace
        
    percentile : float
            take q-th percentile of result
            see numpy.percentile
    
    Returns
    -------
    float
        arias intensity in [m/s] 
    
    References
    ----------
    Arias, "A. MEASURE OF EARTHQUAKE INTENSITY",pp 438-83 of Seismic Design for Nuclear Power Plants. Hansen, Robert J. (ed.). Cambridge, Mass. Massachusetts Inst. of Tech. Press (1970).,1970. Web. 
    '''
    arias_sum=np.pi/(2*9.80665)*np.cumsum(detrend_data(trace)**2)/sr
    return np.percentile(arias_sum,percentile)

def write_point_shp(lat,lon,label,values,value_name,filename):
    '''
    writes list of points to a shape file using shapefile-package
    
    Parameters
    ----------
    lat : array_like
        list of ordered lat values
    
    lon : array_like
        list of ordered lon values
    
    label : array_like
        list of labels for each point (lat,lon), use for station names
    
    values : array_like
        list of values for each point
    
    value_name : str
        field name for values
    
    filename : str
        filename for output file
        
    Returns
    -------
    none
        writes shape file to disk
    '''
    w = shapefile.Writer(filename)
    w.autoBalance = 1
    w.field(value_name, 'F',30,3)
    w.field('Station','C')
    for la,lo,value,lab in zip(lat,lon,values,label):
        w.point(float(lo),float(la))
        w.record(value,lab)
    w.close()
    return

def _bw(f,n=4,f0_l=None, f0_h=None):
        F = np.ones_like(f)
        #lowpassfilter
        if f0_l is not None:
            F1 = np.ones_like(f)
            F1[f != 0.] = 1./np.sqrt(1.+(f[f!=0]/f0_l)**(2.*n))
            F *= F1
        #highpassfilter
        if f0_h is not None:
            F1 = np.zeros_like(f)
            F1[f != 0.] = 1./np.sqrt(1.+(f0_h/f[f!=0])**(2.*n))
            F *= F1
        return F

def pads(s,n,f0,fs):
    '''
    adds zeros to s to +/-[fs*1.5*n/f0 / 2.]
    
    Parameters
    ----------
    s : ndarray
        data

    n : int
    
    f0 : float
    
    fs : float
        sampling frequency of data
        
    Returns
    -------
    ndarray
        zero paded sequence 
    
    Examples
    --------
    >>> acc = np.arange(10)
    >>> acc = pads(acc,4,0.03,100)
    >>> print(acc)
    array([0., 0., 0., ..., 0., 0., 0.])
    
    References
    ----------
    Boore, D. M., & Bommer, J. J. (2005). Processing of strong-motion accelerograms: Needs, options and consequences. Soil Dynamics and Earthquake Engineering, 25(2), 93–115. https://doi.org/10.1016/j.soildyn.2004.10.007
    '''
    N = s.size
    Npad2 = int(np.ceil(fs*1.5*n/f0 / 2.))
    
    spad = np.zeros(N+Npad2*2)
    spad[Npad2:-Npad2] = s
    return spad

def unpads(s,n,f0,fs):
    '''
    removes zeros from s
    
    Parameters
    ----------
    s : ndarray
        data

    n : int
    
    f0 : float
    
    fs : float
        sampling frequency of data
        
    Returns
    -------
    out ndarray
    
    See Also
    --------
    pads
    
    Examples
    --------
    >>> acc = np.array([0., 0., 0., ..., 0., 0., 0.])
    >>> acc = unpads(acc,4,0.03,100)
    >>> print(acc)
    array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
    '''
    
    N = s.size
    Npad2 = int(np.ceil(fs*1.5*n/f0 / 2.))
    dpad = s[Npad2:-Npad2]
    return dpad

def BP_filter(signal,fs,n=4,f0_l=None, f0_h=None):
    '''
    filters signal with low/band/highpass filter
    
    Parameters
    ----------
    signal : ndarray
        data

    fs : float
        sample rate
        
    n  : int, optional
        order of filter
    
    f0_l : float, optional
        frequency lowpassfilter defaults to none
    
    f0_h : float, optional 
        frequency highpassfilter defaults to none
        
    Returns
    -------
    out ndarray
        filtered signal
    
    Examples
    --------
    >>> signal=np.sin(np.deg2rad(np.arange(0,360,45)))
    >>> low_pass = smospy.BP_filter((signal,1,4,0.03,None))
    >>> print(low_pass)
    array([ 1.15229549e-18,  2.34599768e-03,  3.31774174e-03,  2.34599768e-03,
    1.72175251e-18, -2.34599768e-03, -3.31774174e-03, -2.34599768e-03])
    >>> high_pass = smospy.BP_filter(signal,1,4,None,10)
    >>> band_pass = smospy.BP_filter(signal,1,4,0.03,10)
    '''
    S = sf.fft(signal)
    f = sf.fftfreq(signal.size,1./fs)
    H = _bw(f,n,f0_l, f0_h)
    return np.real(sf.ifft(H*S))

def detrend_data(waveform):
        '''
        detrends Data using co-variance
        
        Parameters
        ----------
        
        waveform : ndarray
        
        Returns
        -------
        ndarray
            detrended signal
        '''
        T=np.arange(waveform.size)
        c=np.cov(T,waveform)
        b=c[0,1]/c[0,0]
        a=-b*waveform.size/2+waveform.mean()
        waveform-=b*T+a
        return waveform

def get_taper(n,fraction):
    '''
        gets taper function
        
        Parameters
        ----------
        
        n : shape int or sequence of ints
        
        fraction : fraction of signal being tapered at both ends of the signal
        
        Returns
        -------
        ndarray
            taper
        Examples
        --------
        >>> smospy.get_taper(10,0.8)
        array([0.03806023, 0.14644661, 1. , 0.96193977, 0.85355339,0.69134172, 0.5
        , 0.30865828, 0.14644661, 0.03806023])
        '''
    t=np.arange(n)
    taper = np.ones(n)
    f = int(round(fraction*n))
    taper[:f] = .5-.5*np.cos(np.pi*t[1:(f+1)]/f)
    taper[-f:] = .5-.5*np.cos(np.pi*t[f:0:-1]/f)
    return taper

def Response_Spec(acc,dt,fr,zeta=0.05,fc=0.03,nbutter=4):
    '''
    calculates response spectra from acceleration data
    
    Parameters
    ----------
    acc: ndarray
        data
        
    dt: float
        sample distance in s
    
    fr: array_like
        list of frequencies the response is calculated for
        
    zeta: float, optional
        default: 0.05
    
    fc: float,optional
        default: 0.03
    
    nbutter: int,optional
        default: 4
        
    See Also
    --------
    detrend_data
    get_taper
    pads
    BP_filter
    
    Returns
    -------
    ndarray
        maximum absolut value of response spectra for each frequency of fr
    
    References
    ----------
    
    Weber, Benedikt. Tragwerksdynamik. ETH Zurich Research Collection. https://doi.org/10.3929/ethz-a-007362062
    '''
    acc=detrend_data(acc)
    acc*=get_taper(acc.size,0.05)
    acc=pads(acc,nbutter,fc,1/dt)
    acc=BP_filter(acc,1/dt,nbutter,f0_h=fc)
    
    omega = 2.*np.pi*fr
    lambda0 = -zeta*omega + 1j*omega*np.sqrt(1.-zeta**2)
    lambda1 = -zeta*omega - 1j*omega*np.sqrt(1.-zeta**2)
    
    vel=acc[:2].mean() *dt
    dis=((acc[:3].sum()+acc[1])/4)*dt**2
    y0 = 2.*lambda0 / (lambda0-lambda1) * (-acc[0] + lambda0*vel - lambda0*lambda1*dis)
    
    rsa = np.zeros((acc.size,omega.size))
    rsa[0,:] = y0.real + acc[0]
        
    c1 = np.exp(lambda0*dt)
    c2 = 2.*(1.-np.exp(lambda0*dt))/((lambda0-lambda1)*dt)
    for i in range(1,acc.size):
        y1 = c1*y0 + c2*(acc[i]-acc[i-1])
        rsa[i,:] = y1.real + acc[i]
        y0 = 1.*y1

    rs = np.max(np.abs(rsa),axis=0)
    return rs


if __name__=="__main__":
    pass
