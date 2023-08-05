from smospy.J_Waveform import J_waveform
from smospy.smos_tools import write_point_shp
import numpy as np
import datetime,math
import os,fnmatch
import matplotlib.pyplot as plt
import pandas as pd
import copy
import h5py
from multiprocessing import Process,Queue
try:
    from osgeo import gdal
except ImportError:
    import gdal


class J_wavestream:
    '''
    list-like object containing objects of J_waveform type.
    
    Parameters
    ----------
    
    path : str
        path the to folder containing raw-data files of Japanese agencies or HDF5 files.
    flag : str
        filetype flag, one of:\n
        kik_net - NIED kik_net stations\n
        k_net - NIED k-net stations\n
        JMA_net - Japanese Meteorological Agency\n
        J_Form - Custom Format for loading/saving smospy.J_wavestreams to disc in plain text.\n
        HDF5 - HDF5 format for loading/saving smospy.J_wavestreams to disc.\n
    unit : str,optional
        unit of input files defaults to 'Acc' as NIED and JMA data is acceleration data.
    HDF5_filename : str,optional
        Filename of HDF5 file. Ignored if flag!='HDF5'
    
    Attributes
    ----------
    
    stream: list
        list of J_waveform objects in stream
        
    Examples
    --------
    >>> import smospy
    >>> st=smospy.J_wavestream('./Kik_K_data/20180906030800.knt','k_net')
    >>> print(len(st.stream)) #number of stations in stream
    268
    >>> st2=st[100:103] #slice stream like normal list
    >>> print(st2)
    BO.HKD064
    |E00|N00|Z00|
    BO.HKD065
    |E00|N00|Z00|
    BO.HKD066
    |E00|N00|Z00|
    
    >>> #workflow to compute Arias-intensity and energy like done in Von Specht, S., Ozturk, U., Veh, G., Cotton, F., & Korup, O. (2019)
    >>>
    >>> st.station_in_dist(200) #filter stream for distance in [km] around epicenter
    >>> st.plot_arias_intensity(filename='arias.shp') #compute Arias-intensity for every waveform in Stream and write it to a shape-file
    >>> st.baseline(core_count=8) #baseline correction of all waveform in stream using 8 cores at a time
    >>> st.acc_to_disp(unit='Vel',core_count=8) #use acc_to_disp function on all waveforms of stream with 8 cores
    >>> st.add_vs_amp_from_tiff("vs30.tiff") #add site-parameter information
    >>> st.plot_energy(filename='energy.shp') #compute energy for every waveform in Stream and write it to a shape-file
    
    See Also
    --------
    write_HDF5
    load_HDF5
    smospy.J_Waveform
    smospy.signal_c_lib
    smospy.J_Cord_to_tiff
    '''
    def __init__(self,path,flag,unit='Acc',HDF5_filename=None):
        self.flagdic={'kik_net':'*.EW1','k_net':'*.EW','JMA_net':'*.csv','J_Form':'*.txt','HDF5':'*.h5'}
        self.stream=[]
        if flag in self.flagdic.keys():
            if flag=='HDF5':
                if HDF5_filename==None:
                    HDF5_filename=input()
                filename=str(path)+'/'+str(HDF5_filename)    
                self.load_HDF5(filename,flag,unit)
            
            else:
                self.read_path(path,flag,unit)
        else:
            raise TypeError("filetype is not one of kik_net,k_net,JMA_net,J_Form or HDF5")
        
    def __iter__(self):
        self.pos=0
        return self
    
    def __next__(self):
        if self.pos>len(self.stream)-1:
            raise StopIteration
        else:
            self.pos+=1
            return self.stream[self.pos-1]
        
    def __add__(self,other):
        #no new objects (no deepcopy) are created.
        import inspect
        if isinstance(other,J_wavestream):
            self.stream += other.stream
        return self
    
    def __getitem__(self,n):
        if isinstance(n,slice):
            item=copy.copy(self)
            item.stream=self.stream[n]
            return item
        elif isinstance(n,int):
            if n>len(self.stream):
                print('index out of range')
                return
            else:
                return copy.copy(self.stream[n])
        else:
            raise TypeError('Invalid argument type: {}'.format(type(n)))
    
    def __str__(self):
        return '\n'.join(['BO.{sta}\n    |{channel}|\n'.format(sta=wave.station_name,channel='|'.join(wave.channel_data.keys())) for wave in self.stream])
    
    def read_path(self,path,flag,unit):
        for name in os.listdir(path):
            if fnmatch.fnmatch(name,self.flagdic[flag]):
                waveform=J_waveform(path,name.rsplit('.')[0],flag=flag,unit=unit)
                self.stream.append(waveform)
        return
    
    def sort(self,channel,reverse=False):
        '''
        sorts stream for distance from event
    
        Parameters
        ----------
        channel : str
            channel keyword eg. 'Z00'
            
        reverse : bool,optional
            sort in reverse order, default is False
        
        Examples
        --------
        >>> st2 = smospy.J_wavestream('./Kik_K_data/20180906030800.knt','k_net')
        >>> print([tr.get_event_dist('Z00') for tr in st2])
        [array([ 280015.15646463]),
        array([ 261382.54236447]),
        array([ 262995.11749074]),
        array([ 247787.96790796]),
        array([ 228597.90907264])]
        >>> stream.sort('Z00',True)
        print([tr.get_event_dist('Z00') for tr in st2])
        [array([ 280015.15646463]),
        array([ 262995.11749074]),
        array([ 261382.54236447]),
        array([ 247787.96790796]),
        array([ 228597.90907264])]
        '''
        self.stream.sort(key=lambda x: x.get_event_dist(channel),reverse = reverse)
        return
    
    def station_in_dist(self,dist,channel):
        '''
        filters stream for stations within distance in kilometer.
        
        Parameters
        ----------
        dist : float
            distance in [km]
        channel : str
            channel keyword, eg 'Z10' for borehole
        '''
        new_list=[wave for wave in self.stream if wave.get_event_dist(channel)<=(dist*1000)]
        self.stream=new_list
        return
    
    def get_statios(self,name):
        '''
        Find stations in stream. Takes Regular-Expressions. Returns single station J_waveform class if one match or sub-stream for several matches.
        
        Parameters
        ----------
        name : str
            search string
        
        Returns
        -------
        object : J_waveform or J_wavestream
            one match for station name or every match for Regular-Expressions 
        err_msg : str 
            dont found anything
        
        Examples
        --------
        >>> st = smospy.J_wavestream('./Kik_K_data/20180906030800.knt','k_net')
        >>> st.get_statios('AKT*')
        stations in stream: 8
        >>> print(st)
        BO.AKT001
            |E00|N00|Z00|
        BO.AKT002
            |E00|N00|Z00|
        BO.AKT003
            |E00|N00|Z00|
        BO.AKT005
            |E00|N00|Z00|
        BO.AKT010
            |E00|N00|Z00|
        BO.AKT011
            |E00|N00|Z00|
        BO.AKT021
            |E00|N00|Z00|
        BO.AKT023
            |E00|N00|Z00|
        '''
        new_list=[wave for wave in self.stream if fnmatch.fnmatch(wave.station_name,name)]
        if len(new_list)==0:
            print('not found')
            return
        if len(new_list)==1:
            return new_list[0]
        if len(new_list)>1:
            self.stream=new_list
            print('stations in stream:', len(self.stream))
            return
    
    def plot_travel_curve(self,channel_keyword,c=1,filename='travel_curve.png'):
        self.sort(channel = channel_keyword)
        
        fig = plt.figure(figsize=(40,100))
        for index, wave in enumerate(self.stream):
            
            if channel_keyword not in wave.channel_metadata:
                continue
            
            distance=wave.get_event_dist(channel_keyword)
            starttime=wave.channel_metadata[channel_keyword]['record time']-wave.origin_time
            samp_rate=wave.channel_metadata[channel_keyword]['sample rate']
            data=wave.channel_data[channel_keyword]
            y = distance/1000+(data/np.max(np.abs(data))*(c))
            freq=str(1/samp_rate)+'S'
            x = pd.timedelta_range(starttime, periods=y.size, freq=freq)
            data_points = pd.Series(y, index=x)
            ax=plt.plot(data_points,'k')

        plt.savefig(filename)
        return
    
    def plot_waveforms(self,channel_list=None):
        for waveform in self.stream:
            waveform.plot(channel_list)
        return

    def rotate_waveforms(self,angle):
        '''
        rotates all data in Stream with given angle in degree and extent waveform by R and T component
        
        Parameters
        ----------
        angle : float
            angle in degree
        
        See Also
        --------
        J_waveform.rotation
        '''
        for waveform in self.stream:
            waveform.roation(angle)
        return
            
    def cut_waveforms(self,dt,t0=0):
        '''
        cuttes all waveforms in to the time:\n
        origin_time+t0[s] -> origin_time+t0[s]+dt[s]
        
        Parameters
        ----------
        dt : float
            time in seconds
        t0 : float
            time in seconds
        '''
        for waveform in self.stream:
            waveform.cut_waveform(dt=dt,t=t0)
        return

    def plot_arias_intensity(self,dt=None,t0=0,channels=['E00','N00','Z00'],filename=None,percentile=95):
        '''
        calculates arias intensity for all Wave-forms in Stream and writes results into shp file for plotting in GIS software
        
        Parameters
        ----------
        dt : float,optional
            default None,cut traces in time[s] see cut_waveform
            
        t0 : float,optional
            default 0,cut traces in time[s] see cut_waveform
            
        channels : list
            one of ['E00','N00','Z00'] or ['E10','N10','Z10']
            
        filename : str,optional
            write out shape-file, if not given return tupel(list[station_name],list[arias_int])
            
        percentile : float 
            cutoff percentile for Arias, defaults to 95%
        
        '''
        lat=[]
        lon=[]
        arias_int=[]
        station_name=[]
        
        for wave in self.stream:
            station_name.append(wave.station_name)
            lat.append(wave.station_lat)
            lon.append(wave.station_lon)
            arias_int.append(wave.arias_intensity(dt,t0,channels,percentile))
            
        if filename!=None:    
            write_point_shp(lat=lat,lon=lon,label=station_name,values=arias_int,value_name='intensity',filename=filename)
            return
        else:
            return station_name,arias_int

    def plot_energy(self,channels=['E00','N00','Z00'],rho=2000,filename=None):
        '''
        calculates energy for all Wave-forms in Stream and writes results into shp file for plotting in GIS software
        
        Parameters
        ----------
        channels : list
            one of ['E00','N00','Z00'] or ['E10','N10','Z10']
        
        rho : float
            density of underground
            
        filename : str,optional
            write out shape-file, if not given return tupel(list[station_name],list[energy])
        '''
        lat=[]
        lon=[]
        energy=[]
        station_name=[]
        for wave in self.stream:
            station_name.append(wave.station_name)
            lat.append(wave.station_lat)
            lon.append(wave.station_lon)
            energy.append(wave.energy(channels,rho))
        if filename!=None:    
            write_point_shp(lat=lat,lon=lon,label=station_name,values=energy,value_name='energy',filename=filename)
            return
        else:
            return station_name,energy
        
    def save_stream(self,folder,encod="Shift_JIS"):
        '''
        saves stream in custom human readable .txt format (not recommend)
        
        Parameters
        ----------
        folder : str
            path to folder, create new one if not found
        endcode : str,optional
            use this encode, defaults to "Shift_JIS" because of JMA Japanese Station being in Kanji.
        
        See Also
        --------
        J_wavestream.write_HDF5
        '''
        if not os.path.exists(folder):
            os.makedirs(folder)
        for wave in self.stream:
            wave.save_waveform(folder,encod)
        return

    def __baseline(self,start,stop,jobs):
        queue_return={}
        if stop>len(self.stream):
            stop=len(self.stream)
        print(start,stop)
        for i in range(start,stop,1):
            print('station: ', self.stream[i].station_name)
            wave=self.stream[i]
            wave.baseline_corr()
            queue_return[i]=wave
        jobs.put(queue_return)
        return
    
    def baseline(self,core_count=1):
        '''
        Baseline corrects every wave in stream. Uses Python multiprocessing to accelerate.
        
        Parameters
        ----------
        core_count : int
            number of cores to be used
        See Also
        --------
        smospy.Py_C_signal_lib.icbm
        
        '''
        stackcount=int(math.ceil(len(self.stream)/core_count))
        start=0
        stop=stackcount
        job_list=[]
        jobs=Queue()
        
        if core_count>len(self.stream):
            core_count=len(self.stream)
        
        for i in range(core_count):
            prozess=Process(target=self.__baseline, args=(start,stop,jobs))
            prozess.start()
            print('start baseline. PID: ',prozess.pid)
            start+=stackcount
            stop+=stackcount
            job_list.append(prozess)
        
        print('Prozess running: ',len(job_list))
        if len(job_list)>0:
            for i in range(len(job_list)):
                queue_return=jobs.get(True) #wait until job is done
                for key in queue_return:
                    self.stream[key]=queue_return[key] #replace 
                
            for p in job_list:
                p.join()
                print('END',p.pid)
        return

    def acc_to_disp(self,unit,itp=0,itf=0,core_count=1):
        '''
        integrates all waves in stream. Uses Python multiprocessing to accelerate.
        
        Parameters
        ----------
        unit : str
            'Vel': for velocity out of acceleration\n
            'Disp' for displacement out of acceleration or velocity
        itp : int,optional
            default 0
        itf : int,optional
            default 0
            
        core_count : int
            number of cores to be used
        See Also
        --------
        smospy.Py_C_signal_lib.acc2disp
        
        '''
        stackcount=int(math.ceil(len(self.stream)/core_count))
        start=0
        stop=stackcount
        job_list=[]
        jobs=Queue()
        
        if core_count>len(self.stream):
            core_count=len(self.stream)
        
        for i in range(core_count):
            prozess=Process(target=self.__acc_to_disp, args=(unit,itp,itf,start,stop,jobs))
            prozess.start()
            print('start acc_to_disp. PID: ',prozess.pid)
            start+=stackcount
            stop+=stackcount
            job_list.append(prozess)
        
        print('Prozess running: ',len(job_list))
        if len(job_list)>0:
            for i in range(len(job_list)):
                queue_return=jobs.get(True) #wait until job is done
                for key in queue_return:
                    self.stream[key]=queue_return[key] #replace 
                
            for p in job_list:
                p.join()
                print('END',p.pid)
        return
    
    def __acc_to_disp(self,unit,itp,itf,start,stop,jobs):
        queue_return={}
        if stop>len(self.stream):
            stop=len(self.stream)
        print(start,stop)
        for i in range(start,stop,1):
            print('station: ', self.stream[i].station_name)
            wave=self.stream[i]
            wave.acc_to_disp(unit,itp,itf)
            queue_return[i]=wave
        jobs.put(queue_return)
        return
            
    def diff_stream(self,method='div'):
        '''
        differentiates all data with regards to time
        
        Parameters
        ----------
        method : str,optional
            defaults to 'div'\n 
            'div'   : numpy.ediff1d\n
            'grad'  : numpy.gradient\n
            
        '''
        for wave in self.stream:
            wave.diff_waveform(method)

    def add_vs_amp_from_tiff(self,tifffile):
        '''
        Adds site parameter AVS30 and Vs400 from tiff-file.
        
        Parameters
        ----------
        tifffile : str
            'path/filename' to tiff
        '''
        tiff=gdal.Open(tifffile)
        x_0,x_res,_,y_0,_,y_res = tiff.GetGeoTransform()
        tiff_array = tiff.ReadAsArray()
        for wave in self.stream:
            wave.add_vs_amp_from_tiff(tiff_array,x_0,x_res,y_0,y_res)
        return

    def Resp_Spek(self,channel=None,fr=None,zeta=0.05,fc=0.03,nbutter=4,filename=None):
        '''
        Calculates response spectra from given acceleration data in channel. Writes result in QGIS readable format.
        
        Parameters
        ----------
        channel : list,optional
            list of str channel name
        
        fr : array_like,optional
            list of frequencies the response is calculated for defaults to np.logspace(-2,np.log10(50))
            
        zeta : float, optional
            default: 0.05
        
        fc : float,optional
            default: 0.03
        
        nbutter : int,optional
            default: 4
        
        filename : str,optional
            defaults to None. give 'path/filename' to write out in csv format.
            
        Returns
        -------
        response : dict{dict}
            response spectra stored in dict[station_name][channel]
            
        See Also
        --------
        smos_tools.Response_Spec
        '''
        
        if fr == None:
            fr = np.logspace(-2,np.log10(50))
        resp_dic={}
        for wave in self.stream:
            print(wave.station_name)
            resp_dic[wave.station_name] = wave.RS(channel,fr,zeta,fc,nbutter)
        if filename!= None:
            for i in range(3):
                if i==0:
                    C0='E00'
                    C1='E10'
                if i==1:
                    C0='N00'
                    C1='N10'
                if i==2:
                    C0='Z00'
                    C1='Z10'

                with open(filename+C0+'.txt','w') as f,open(filename+C1+'.txt','w') as g:
                    #f.write('lon,lat,')
                    #g.write('lon,lat,')
                    f.write('0,0,')#placeholder for headerline
                    g.write('0,0,')
                    for i1,val in enumerate(fr):
                        if i1==len(fr)-1:
                            f.write('%f '%val)
                            g.write('%f '%val)
                        else:
                            f.write('%f, '%val)
                            g.write('%f, '%val)
                    f.write('\n')
                    g.write('\n')
                    for wave in self.stream:
                        lat=wave.station_lat
                        lon=wave.station_lon
                        name=wave.station_name
                        res=resp_dic[name]
                        if C0 in res:
                            f.write('%f,%f,'%(lon,lat))
                            line=res[C0]
                            for i1,val in enumerate(line):
                                if i1==len(line)-1:
                                    f.write('%f '%val)
                                else:
                                    f.write('%f, '%val)
                            f.write('\n')
                        if C1 in res:
                            g.write('%f,%f,'%(lon,lat))
                            line=res[C1]
                            for i1,val in enumerate(line):
                                if i1==len(line)-1:
                                    g.write('%f '%val)
                                else:
                                    g.write('%f, '%val)
                            g.write('\n')
        return resp_dic
    
    def write_HDF5(self,filename,folder='./'):
        '''
        writes stream to HDF5 format (recommend)
        
        Parameters
        ----------
        filename : str
            filename of HDF5-file
        
        folder : str,optional
            defaults to current work folder
        '''
        if not os.path.exists(folder):
            os.makedirs(folder)
        name=str(folder+filename)
        hf_file = h5py.File(name, 'w')
        for wave in self.stream:
            wave.__HF5_save__(hf_file)
        hf_file.close()
        return

    def load_HDF5(self,filename,flag,unit):
        hf = h5py.File(filename, 'r')
        for key in hf.keys():
            st=hf[key]
            waveform=J_waveform(path=None,filename=filename,flag=flag,unit=unit,HDF5_Station=st)
            self.stream.append(waveform)
        hf.close()
        return
    
        
if __name__=="__main__":
    pass
    
    
    
