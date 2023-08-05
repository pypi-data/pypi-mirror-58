import sys
from smospy.signal_c_lib import Py_C_signal_lib
from smospy.smos_tools import *
import numpy as np
import datetime
import os
import matplotlib.pyplot as plt
import copy
import time,math
import multiprocessing as mp
from multiprocessing import Process,Queue

class J_waveform:
    '''
    J_Waveform contains all data and metadata of seismic records by Japanese Agencies NEED kik-net and K-net as well as Japanese Meteorological Agency (JMA)
    When reading from raw-files by Japanese Agencies, data is converted from gal to m/s**2 and the scale factor is applied. According to NEED arrival time in kik/k-net raw-data files is 15 seconds to late. 15 seconds are subtracted from record time given. 
    
    Parameters
    ----------
    
    path : str
        path the to folder containing raw-data files of Japanese agencies.
        
    filename : str
        filename of specific record
        
    flag : str
        filetype flag, one of:\n
        kik_net - NIED kik_net stations\n
        k_net - NIED k-net stations\n
        JMA_net - Japanese Meteorological Agency\n
        J_Form - Custom Format for loading/saving smospy.J_wavestreams to disc in plain text.
        
    detrend : boolean,optional
        defaults to true, automatic detrend of data after reading
        
    unit : str,optional
        unit of input files defaults to 'Acc' as NIED and JMA data is acceleration data.
    
    kwargs
        used for reading HDF5 files, please use the J_wavestream when loading HDF5 files
        
    Attributes
    ----------
    
    channel_data : dict
        dictionary containing pairs key: str value: ndarray. Keys are the channel names of the station, suffix "00" for surface and "10" for borehole.
    channel_metadata : dict
        dictionary containing pairs key: str value: dict. Keys are the channel names of the station, suffix "00" for surface and "10" for borehole.
        Inside the second dictionary values for the keys: 'station height', 'record time','sample rate' and 'scale factor' are stored.
    
    station_name : str
    station_lat : double
    station_lon : double
    
    site_parameters = dict
        additional site parameters can be attached under keys: 'AVS30' and 'Vs400'
    
    origin_time : numpy.datetime64 object
    event_lat : double
    event_lon : double
    event_depth : double
    event_mag : double
    
    Examples
    --------
    >>> import smospy
    >>> wave=smospy.J_waveform('./Kik_K_data/20180906030800.knt','HKD0401809060308',flag='k_net')
    
    >>> #get the raw data from a waveform object for custom plots or further processing
    >>> raw_data=wave.channel_data['E00']
    >>> print(raw_data)
        array([0,0,0,...,0,0,0])
    
    
    '''
    def __init__(self,path,filename,flag,detrend=True,unit='Acc',**kwargs):
        self.flag=flag                      #flag for file format
        self.filename = filename.strip()            
        self.path=path  
        self.channel_data={}                #data storage for functions
        self.channel_metadata={}            #metadata storage
        
        self.station_name = None
        self.station_lat = None
        self.station_lon = None
        
        self.site_parameters = {}
        
        self.origin_time = None
        self.event_lat = None
        self.event_lon = None
        self.event_depth = None
        self.event_mag = None
        
        
        self.unit = unit
        self.unit_dic ={'Acc':0 , 'Vel':1 , 'Disp':2 , 0:'Acc' , 1:'Vel' , 2:'Disp'}
        
        self.kik_k_net_channeldic={'EW1':'E00','EW2':'E10','NS1':'N00','NS2':'N10','UD1':'Z00','UD2':'Z10','EW':'E00','NS':'N00','UD':'Z00'}
        self.JMA_channels=['N00','E00','Z00']
        
        if (self.flag == 'kik_net' or self.flag == 'k_net'):
            for name in os.listdir(self.path):
                if name.startswith(self.filename) and not name.endswith('gz'):
                    if(flag == 'kik_net'):
                        key=name[-3:]
                    else:
                        key=name[-2:]
                    self.channel_metadata[self.kik_k_net_channeldic[key]]=self.read_header_kik_kN(key)
                    self.channel_data[self.kik_k_net_channeldic[key]]=self.read_data_kik_kN(key)
            ########################     
            if self.channel_data=={}:
                print('file not found:', self.filename)
                raise Exception()
            ########################
        
        if self.flag == 'JMA_net':
            if 'JMA_Event.txt' in os.listdir(self.path):
                with open(self.path+'/'+'JMA_Event.txt' ,'r') as f:
                    for number,line in enumerate(f):
                        if number == 0:
                            timestr=line.split('  ',1)[1].strip()
                            self.origin_time = np.datetime64(datetime.datetime.strptime(timestr,'%Y/%m/%d %H:%M:%S'),'ms')
                        if number == 1:
                            self.event_lat = float(line.split('  ',1)[1].strip())
                        
                        if number == 2:
                            self.event_lon = float(line.split('  ',1)[1].strip())
                            
                        if number == 3:
                            self.event_depth = float(line.split('  ',1)[1].strip())*(1000)
                            
                        if number == 4:
                            self.event_mag = float(line.split('  ',1)[1].strip())
            else:
                print('JMA_Event.txt not found')
                raise Exception()
            
            metadata=self.read_JMA_meta_data()
            for channel_key in self.JMA_channels:
                self.channel_metadata[channel_key]=metadata
            self.channel_data = self.read_JMA_data()
        
        if self.flag == 'J_Form':
            self.channel_metadata,number = self.read_J_Form_metadata()
            self.channel_data = self.read_J_Form_data(number)

        if self.flag == 'HDF5':
            if not 'HDF5_Station' in kwargs:
                print('provide HDF5 container as kwargs|->HDF5_Station|)')
                return()
            else:
                station=kwargs['HDF5_Station']
                self.read_HDF5_group(station)

        if detrend:
            for key in self.channel_data:
                self.channel_data[key]=detrend_data(self.channel_data[key])

    def __str__(self):
        return '\n'.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

    def __getattr__(self, attr):
        keys=attr.split('_')
        if keys[0]=='data':
            returnval=self.channel_data
            for key in keys[1:]:
                returnval=returnval[key]
            return returnval
                
        if keys[0]=='metadata':
            returnval=self.channel_metadata
            for key in keys[1:]:
                returnval=returnval[key]
            return returnval
        
        else:
            raise AttributeError

    def read_HDF5_group(self,station):
        self.station_name = station.attrs['station_name']
        self.station_lat = station.attrs['station_lat']
        self.station_lon = station.attrs['station_lon']
        self.origin_time = np.datetime64(station.attrs['origin_time'])
        self.event_lat = station.attrs['event_lat']
        self.event_lon = station.attrs['event_lon']
        self.event_depth = station.attrs['event_depth']
        self.event_mag = station.attrs['event_mag']
        
        self.site_parameters = {}
        self.channel_data={}                #data storage for functions
        self.channel_metadata={}            #metadata storage
        for key in station['Site parameter'].keys():
            self.site_parameters[key]=station['Site parameter'][key]
            
        for key in station['Data'].keys():
            self.channel_data[key]=np.array(station['Data'][key])
            self.channel_metadata[key]={}
            for attribut_key in station['Data'][key].attrs.keys():
                attr=station['Data'][key].attrs[attribut_key]
                if attribut_key=='record time':
                    attr=np.datetime64(attr)
                else:
                    attr=float(attr)
                self.channel_metadata[key][attribut_key]=attr
        return
        
    def read_JMA_meta_data(self):
        metadata={}
        with open(self.path+'/'+self.filename+'.csv' ,'r',encoding="Shift_JIS") as f:
                    for number,line in enumerate(f):
                        if number == 0:
                            self.station_name = line.split('=',1)[1].strip()
                
                        if number == 1:
                            self.station_lat = float(line.split('=',1)[1].strip())
                        
                        if number == 2:
                            self.station_lon = float(line.split('=',1)[1].strip())

                        if number == 3:
                            smp_string = line.split('=',1)[1].strip()
                            metadata['sample rate'] = float(smp_string.split('Hz')[0])
                            
                        if number == 5:
                            timestr=line.split('=',1)[1].strip()
                            metadata['record time'] = np.datetime64(datetime.datetime.strptime(timestr,'%Y %m %d %H %M %S'),'ms')
                            #J-waveform recordtime is 15 seconds off
                        
                        if number >6:
                            break
        
        metadata['station height'] = 0                
        metadata['scale factor'] = 1/100 #umrechnung gal-> m/s^2
        return metadata
    
    def read_JMA_data(self):
        data_dic={}
        data=np.genfromtxt(self.path+'/'+self.filename+'.csv',delimiter=',',skip_header=7,skip_footer=0 ,invalid_raise=False,encoding= "Shift_JIS")
        for i,channel_key in enumerate(self.JMA_channels):
            data_dic[channel_key]=data[:,i].flatten()*self.channel_metadata[channel_key]['scale factor']
        return data_dic
    
    def read_header_kik_kN(self,channel):
        metadata={}
        with open(self.path+'/'+self.filename + '.' + channel,'r') as f:
            for number,line in enumerate(f):
                if number == 0:
                    timestr=line.split('  ',1)[1].strip()
                    self.origin_time = np.datetime64(datetime.datetime.strptime(timestr,'%Y/%m/%d %H:%M:%S'),'ms')
                if number == 1:
                    self.event_lat = float(line.split('  ',1)[1].strip())
                
                if number == 2:
                    self.event_lon = float(line.split('  ',1)[1].strip())
                    
                if number == 3:
                    self.event_depth = float(line.split('  ',1)[1].strip())*(1000)
                    
                if number == 4:
                    self.event_mag = float(line.split('  ',1)[1].strip())
                    
                if number == 5:
                    self.station_name = line.split('  ',1)[1].strip()
                
                if number == 6:
                    self.station_lat = float(line.split('  ',1)[1].strip())
                
                if number == 7:
                    self.station_lon = float(line.split('  ',1)[1].strip())
                    
                if number == 8:
                    metadata['station height'] = float(line.split(')',1)[1].strip())                   
                
                if number == 9:
                    timestr=line.split('  ',1)[1].strip()
                    metadata['record time'] = np.datetime64(datetime.datetime.strptime(timestr,'%Y/%m/%d %H:%M:%S')-datetime.timedelta(seconds=15),'ms')
                    #J-waveform recordtime is 15 seconds off
                    
                if number == 10:
                    smp_string = line.split(')',1)[1].strip()
                    metadata['sample rate'] = float(smp_string.split('Hz')[0])
                    
                if number == 13:
                    scale_str = line.split('  ',1)[1].strip().split('/')
                    scale_nom = float(scale_str[0][:-5])
                    scale_denom = float(scale_str[1]) 
                    metadata['scale factor'] = scale_nom/(scale_denom*100) #umrechnung gal-> m/s^2
                
                if number >16:
                    break
        return metadata

    def read_data_kik_kN(self,channel):
        data=np.genfromtxt(self.path+'/'+self.filename+'.'+channel,skip_header=17,skip_footer=1 ,invalid_raise=False)
        return data.flatten()*self.channel_metadata[self.kik_k_net_channeldic[channel]]['scale factor']

    def save_waveform(self,folder,encod):
        __absatz=15
        f = open(folder+'/'+self.station_name+'.txt','w',encoding=encod)
        f.write('origin_time    : '+str(self.origin_time)+'\n')
        f.write('event_lat      : '+str(self.event_lat)+'\n')
        f.write('event_lon      : '+str(self.event_lon)+'\n')
        f.write('event_depth    : '+str(self.event_depth)+'\n')
        f.write('event_mag      : '+str(self.event_mag)+'\n')
        f.write('station_name   : '+str(self.station_name)+'\n')
        f.write('station_lat    : '+str(self.station_lat)+'\n')
        f.write('station_lon    : '+str(self.station_lon)+'\n')
            
        for channel in self.channel_metadata:
            f.write(str(channel)+'\n')
            for key in self.channel_metadata[channel]:
                f.write(str(key))
                for i in range(__absatz-len(str(key))):
                    f.write(' ')
                f.write(': ')
                f.write(str(self.channel_metadata[channel][key])+'\n')
            
        f.write('Data: \n')
        for key in self.channel_data.keys():
            f.write(str(key)+' ')
        f.write('\n')
        np.savetxt(f,np.array([channel_data for channel_data in self.channel_data.values()]).transpose(), delimiter=';')
        f.close()
        return

    def read_J_Form_metadata(self):
        metadata={}
        with open(self.path+'/'+self.filename+'.txt' ,'r',encoding="Shift_JIS") as f:
                    for number,line in enumerate(f):
                        
                        if line.startswith('Data'):
                            break
                        
                        entry=line.split(' : ')                        
                        
                        if number == 0:
                            self.origin_time = np.datetime64(entry[1])
                        if number == 1:
                            self.event_lat = float(entry[1])
                        if number == 2:
                            self.event_lon = float(entry[1])
                        if number == 3:
                            self.event_depth = float(entry[1])
                        if number == 4:
                            self.event_mag = float(entry[1])
                        if number == 5:
                            self.station_name = entry[1].strip()
                        if number == 6:
                            self.station_lat = float(entry[1])
                        if number == 7:
                            self.station_lon = float(entry[1])
                        if (number >7):
                            if len(entry)== 1:
                                channel=entry[0].strip()
                                metadata[channel]={}
                                continue
                            
                            if entry[0].strip()=='record time':
        
                                metadata[channel][entry[0].strip()]=np.datetime64(entry[1])
                                continue
                            else:
                                metadata[channel][entry[0].strip()]=float(entry[1])
        
        return metadata,number+2
    
    def read_J_Form_data(self,number):
        data_dic={}
        data=np.genfromtxt(self.path+'/'+self.filename+'.txt',delimiter=';',skip_header=number,skip_footer=0 ,invalid_raise=False,encoding= "Shift_JIS")
        for i,channel_key in enumerate(self.channel_metadata.keys()):
            data_dic[channel_key]=data[:,i].flatten()
        return data_dic

    def get_copy(self,keys=None):
        if keys==None:
            return copy.deepcopy(self)
        else:
            subclass=copy.deepcopy(self)
            subclass.channel_data=dict((k,self.channel_data[k]) for k in keys if k in self.channel_data)
            subclass.channel_metadata=dict((k,self.channel_metadata[k]) for k in keys if k in self.channel_metadata)
            return subclass

    def __HF5_save__(self,hf):
        station=hf.create_group(self.station_name)
        
        station.attrs['station_name']= self.station_name
        station.attrs['station_lat']= self.station_lat
        station.attrs['station_lon']= self.station_lon
        
        station.attrs['origin_time']= str(self.origin_time)
        station.attrs['event_lat']= self.event_lat
        station.attrs['event_lon']= self.event_lon
        station.attrs['event_depth']= self.event_depth
        station.attrs['event_mag']= self.event_mag
        site_parameters=station.create_group('Site parameter')
        for key in self.site_parameters:
            site_parameters.attrs[key]=self.site_parameters[key]
        
        data_group=station.create_group('Data')
        for key in self.channel_data:
            channel=data_group.create_dataset(key,data=self.channel_data[key])
            for attr_key in self.channel_metadata[key]:
                channel.attrs[attr_key]=str(self.channel_metadata[key][attr_key])
        
        return

    def plot(self,channel_list=None):
        '''
        quick plot of station data
        
        Parameters
        ----------
        channel_list : list,optional
            list of string naming channels to be plotted, all channels if None
        
        Examples
        --------
        >>> wave.plot(['E00','N00','Z00'])
        '''
        if channel_list==None:
            channel_list=self.channel_data
        fig=plt.figure()
        for i,key in enumerate(channel_list):
            ax=fig.add_subplot(len(self.channel_metadata),1,i+1)
            ax.plot(self.channel_data[key])
            ax.set_title(key)
        fig.suptitle(self.station_name)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
        return
    
    def RS(self,channel=None,fr=None,zeta=0.05,fc=0.03,nbutter=4):
        '''
        Calculates response spectra from given acceleration data in channel.
        
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
        
        nbutter: int,optional
            default: 4
        
        Returns
        -------
        response : dict
            response spectra stored in dict[channel]
            
        See Also
        --------
        smos_tools.Response_Spec
        '''
        if fr == None:
            fr = np.logspace(-2,np.log10(50))
            
        if self.unit != 'Acc':
            print('data not in Acc, return')
            return
        response={}
        
        if channel==None:
            channel=list(self.channel_data.keys())
        
        for key in channel:
            dt = 1/self.channel_metadata[key]["sample rate"]
            acc=self.channel_data[key]
            response[key]=Response_Spec(acc,dt,fr,zeta,fc,nbutter)
            
        response['unit']='spec '+self.unit
        return response

    def rotation(self,angle):
        '''
        rotate data with given angle in degree and extent waveform by R and T component
        
        Parameters
        ----------
        angle : float
            angle in degree
        
        Examples
        --------
        >>> wave.channel_data.keys()
        ['N00','E00','Z00']
        >>> wave.rotation(90)
        >>> wave.channel_data.keys()
        ['N00','E00','Z00','R00','T00']
        '''
        angle=np.deg2rad(angle)
        
        if ('E00' in self.channel_data.keys() and 'N00' in self.channel_data.keys()):
            self.channel_data['R00']=np.sin(angle)*self.channel_data['E00']+np.cos(angle)*self.channel_data['N00']
            self.channel_metadata['R00']=self.channel_metadata['E00']
        
            self.channel_data['T00']=np.cos(angle)*self.channel_data['E00']-np.sin(angle)*self.channel_data['N00']
            self.channel_metadata['T00']=self.channel_metadata['E00']
        if ('E10' in self.channel_data.keys() and 'N10' in self.channel_data.keys()):
            self.channel_data['R10']=np.sin(angle)*self.channel_data['E10']+np.cos(angle)*self.channel_data['N10']
            self.channel_metadata['R10']=self.channel_metadata['E10']
        
            self.channel_data['T10']=np.cos(angle)*self.channel_data['E10']-np.sin(angle)*self.channel_data['N10']
            self.channel_metadata['T10']=self.channel_metadata['E10']
        
        return

    def get_event_dist(self,channel):
        lat1=self.event_lat
        lon1=self.event_lon
        h1=self.event_depth
        
        lat2=self.station_lat
        lon2=self.station_lon
        h2=self.channel_metadata[channel]['station height']
        
        return distance((lat1,lon1,h1),(lat2,lon2,h2))

    def add_vs_amp_from_tiff(self,tiff_array,x_0,x_res,y_0,y_res):
        '''
        Adds site Parameter AVS30 and Vs400 from array. Recommended to call from J_wavestream
        
        Parameters
        ----------
        tiff_array : ndarray
            shape (2,x,y) array with AVS30 in 1. band and Vs400 in 2. band.
        x_0 : float
            corner x/lat coordinate of tiff
        x_res : float
            resolution in x direction
        y_0 : float
            corner y/lon coordinate of tiff
        y_res : float
            resolution in y direction
        
        See Also
        --------
        add_vs_amp_from_tiff,energy,J_Coord_file
        '''
        if not hasattr(self, 'site_parameters'):
            self.site_parameters = {}
            
        x=self.station_lon
        y=self.station_lat
        x_index = int(np.round((x-x_0) / x_res))
        y_index = int(np.round((y-y_0) / y_res))
        self.site_parameters['AVS30'] = tiff_array[0][y_index,x_index]
        self.site_parameters['Vs400'] = tiff_array[1][y_index,x_index]
        return

    def arias_intensity(self,dt=None,t0=0,channels=['E00','N00','Z00'],percentile=95):
        '''
        cuts copy of data to given time and calculates arias intensity for given percentile of it
        
        Parameters
        ----------
        dt : float,optional
            time window in seconds
        
        t0 : float,optional
            start time in seconds from trace onset  
            
        channels : list, optional
            traces to sum arias intensity over\n
            defaults to ['E00','N00','Z00']\n
            use ['E10','N10','Z10'] for borehole stations of kik-net
        
        fc : float,optional
            default: 0.03
        
        nbutter: int,optional
            default: 4
        
        Returns
        -------
        intensity : float
            summed arias intensity in in [m/s]
            
        See Also
        --------
        smos_tools.Response_Spec
        '''
        if self.unit != 'Acc':
            print('wrong unit')
            return
        
        subwave=self.get_copy(channels)
        if dt!=None:
            subwave.cut_waveform(dt,t0)
        
        intensity=0
        for key in subwave.channel_data:
            intensity+=arias_intensity(subwave.channel_data[key],subwave.channel_metadata[key]['sample rate'],percentile)
        return intensity

    def energy(self,channels=['E00','N00','Z00'],rho=2000.):
        '''
        Calculates energy at station for given traces. Traces need to be in velocity[m/s]. Attach site parameters first by calling add_vs_amp_from_tiff().
        
        Parameters
        ----------
        channels : list, optional
            traces to sum energy over\n
            defaults to ['E00','N00','Z00']\n
            use ['E10','N10','Z10'] for borehole stations of kik-net
        
        rho : float,optional
            density at station, default: 2000
        
        Returns
        -------
        energy : float
            energy at station
            
        See Also
        --------
        smos_tools.energy
        '''
        if not hasattr(self, 'site_parameters'):
            print('no attached site parameters')
            return
        if self.site_parameters == {}:
            print('no attached site parameters')
            return
        if self.unit != 'Vel':
            print('convert to Velocity first')
            return
        k1,k2,k3=channels
        
        lat1=self.event_lat
        lon1=self.event_lon
        h1=self.event_depth
        
        lat2=self.station_lat
        lon2=self.station_lon
        h2=self.channel_metadata[channel]['station height']
        
        p1 = (lat1,lon1,h1)
        p2 = (lat2,lon2,h2)
        
        A = energy_area(p1,p2)
        E = np.sum(np.square(self.channel_data[k1])+np.square(self.channel_data[k2])+np.square(self.channel_data[k3]))
        sf = self.channel_metadata[k1]['sample rate']
        AVS30 = self.site_parameters['AVS30']
        Vs400 = self.site_parameters['Vs400']
        return energy(A,E,sf,AVS30,Vs400,rho)

    def cut_waveform(self,dt,t=0):
        copy=self.get_copy()
        for key in copy.channel_data:
            t_0 = self.channel_metadata[key]['record time']
            freq= self.channel_metadata[key]['sample rate']
            size=copy.channel_data[key].size
            if t<0:
                t=0
            t0=t_0+(1000*t)
            if size/freq<dt:
                dt=size/freq
            
            pos1=int((t0-t_0).astype(int)*(freq/1000))#time in millisec
            pos2=int(pos1+(dt*freq))
            
            if pos1>size:
                print('t0 is after the end of the record')
                break
            if pos2>size:
                print('warning only cutted until end of stream due to dt beeing to big')
                pos2=size
            
            copy.channel_data[key]=self.channel_data[key][pos1:pos2]
            copy.channel_metadata[key]['record time'] = t0
        self.channel_metadata=copy.channel_metadata
        self.channel_data = copy.channel_data
        return
    
    def LTST_Picker(self,channel,nsta,nlta):
        sta=self.channel_data[channel]**2
        sta = np.require(sta, dtype=np.float)
        lta = sta.copy()
        sta[nsta-1:]=np.convolve(sta, np.ones((nsta,))/nsta, mode='valid')
        lta[nlta-1:]=np.convolve(lta, np.ones((nlta,))/nlta, mode='valid')
        sta[:nlta - 1] = 0
        lta[:nlta - 1] = 0
        dtiny = np.finfo(0.0).tiny
        idx = lta < dtiny
        lta[idx] = dtiny
        return sta / lta
    
    def find_onset(self,sta,lta,channel=None,sta_lta_ratio=3):
        picks={}
        if channel==None:
            channels=self.channel_data.keys()
        else:
            channels=channel
            
        for key in channels:
            nsta = int(sta*self.channel_metadata[key]['sample rate'])
            nlta = int(lta*self.channel_metadata[key]['sample rate'])
            char_func=self.LTST_Picker(key,nsta,nlta)
            picks[key]=np.argmax(char_func>sta_lta_ratio)
        return picks
        
    def remove_pre_event_offset(self,sta,lta,channel=None):
        if channel==None:
            channels=self.channel_data.keys()
        else:
            channels=channel
        
        onset=self.find_onset(sta,lta,channels)
        print(onset)
        for key in onset:
            N=int(lta*self.channel_metadata[key]['sample rate'])
            self.channel_data[key]-=np.mean(self.channel_data[key][(onset[key]-N):(onset[key]-1)])
        return
    
    def __baseline_corr(self,E,N,Z,Nsmin,Nsmax,thrshld,nmin,c_wrapper):
        self.channel_data[E],self.channel_data[N],self.channel_data[Z]=np.array(c_wrapper.icbm([self.channel_data[E],self.channel_data[N],self.channel_data[Z]],Nsmin,Nsmax,thrshld,nmin))
        return
    
    def baseline_corr(self,Nsmin=1,Nsmax=6,thrshld=1e-5 ,nmin=500):
        c_wrapper=Py_C_signal_lib() #wrapperclass for Baseline correction
        keylist=list(self.channel_data.keys())
        if 'E00'and 'N00'and 'Z00' in keylist:
            self.__baseline_corr('E00','N00','Z00',Nsmin,Nsmax,thrshld,nmin,c_wrapper)
            
        if 'E10'and 'N10'and 'Z10' in keylist:
            self.__baseline_corr('E10','N10','Z10',Nsmin,Nsmax,thrshld,nmin,c_wrapper)
        
        del c_wrapper
        return

    def acc_to_disp(self,target_unit='Disp',itp=0,itf=0):
        unit_flag=self.unit_dic[target_unit]
        if self.unit=='Disp':
            print('return without caling c-lib_acc_to_disp')
            return
        if self.unit=='Vel':
            if target_unit=='Vel' or target_unit=='Acc':
                print('return without caling c-lib_acc_to_disp')
                return
            else:
                self.diff_waveform()
        if self.unit=='Acc':
            if target_unit=='Acc':
                print('return without caling c-lib_acc_to_disp')
                return
            else:
                print('caling c-lib_acc_to_disp')
                c_wrapper=Py_C_signal_lib() #wrapperclass for signal_c_lib
                keylist=list(self.channel_data.keys())
                
                for key in keylist:
                    self.channel_data[key] = np.array(c_wrapper.acc2disp(self.channel_data[key],self.channel_metadata[key]['sample rate'],itp,itf))[unit_flag]
                cut=min([self.channel_data[key].size for key in self.channel_data])
                for key in self.channel_data:
                    self.channel_data[key]=self.channel_data[key][:cut]
                self.unit=target_unit
                print(self.unit)
                del c_wrapper
        return
        
    def diff_waveform(self,method='div'):
        if self.unit=='Acc':
            return
        else:
            for key in self.channel_data:
                if method=='div':
                    self.channel_data[key]=(np.ediff1d(self.channel_data[key],None,0))/(1/self.channel_metadata[key]['sample rate'])
                if method=='grad':
                    self.channel_data[key]=np.gradient(self.channel_data[key],1/self.channel_metadata[key]['sample rate'])
            self.unit=self.unit_dic[self.unit_dic[self.unit]-1]




if __name__=="__main__":
    pass
