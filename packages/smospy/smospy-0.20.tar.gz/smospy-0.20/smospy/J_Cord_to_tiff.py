import os,fnmatch
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
from collections import defaultdict
import argparse
try:
    from osgeo import gdal
except ImportError:
    import gdal

class J_Coord_file:
    '''
    Converts csv files that contain models for Average Shear-Wave Velocity of upper 30m (AVS30) and Site Amplification Factor for surface Vs=400 (Vs400) of Japan given by j-shis into geotiff files. Usable from command line: call J_Cord_to_tiff -h for available options.
    
    Parameters
    ----------
    
    folder : str
        path to folder containing j-shis AMP-VS400 files
    
    filename : str,optional
        comma separated string of filenames
    
    flag : str,optional
        filename ending, defaults to '.csv'
    
    plot : bool,optional
        plot data,defaults to false
        
    tiffname : str,optional
        defaults to None (don`t save), save under this name
        
    Examples
    --------
    
    >>> path = ./Amp_fac' #path to downloaded files
    >>> from smospy import J_Coord_file
    >>> J_Coord_file(path,plot=True)
    
    
    References
    ----------
    http://www.j-shis.bosai.go.jp/map/
    '''
    def __init__(self,folder,filename=None,flag='.csv',plot=False,tiffname=None):
        self.folder=folder
        if filename==None:
            self.filename=self.get_files(self.folder,flag)
        else:
            self.filename=filename.split(',')
            
        self.min_LO,self.min_LA,self.AFl,self.VSl=self.read_files()
        if plot==True:
            self.plot()
        if tiffname!= None:
            self.write_geotiff(tiffname)
        
    def get_files(self,folder,flag):
        filename=[]
        for name in os.listdir(folder):
            if fnmatch.fnmatch(name,'*'+flag):
                filename.append(name)
        filename.sort(key=lambda x: int(x[-8:-4]))
        return filename
    
    def read_files(self):
        AFl = defaultdict(dict)
        VSl = defaultdict(dict)
        minLO = np.inf
        minLA = np.inf
        
        for filename in self.filename:
            print(filename)
            latkey=int(filename[-8:-6])
            lonkey=int(filename[-6:-4])
            
            if lonkey < minLO:
                minLO = lonkey
                
            if latkey< minLA:
                minLA = latkey
            
            AF2 = np.zeros((320,320))
            VS2 = np.zeros((320,320))
            
            dataframe=pd.read_csv('/'.join((self.folder,filename)),sep=',',names=['Code','JCode','AVS','ARV'],dtype={'Code' : str,'JCode' : np.float64,'AVS': np.float64,'ARV': np.float64},skiprows=7)
            
            af=dataframe['ARV'].tolist()
            vs=dataframe['AVS'].tolist()
            ################
            lo,la,I_J=self.coord_conv(dataframe['Code'].tolist())
            ################
            
            for i,tupel in enumerate(I_J):
                AF2[tupel[0],tupel[1]] = af[i]
                VS2[tupel[0],tupel[1]] = vs[i]
            
            AFl[latkey][lonkey]=AF2
            VSl[latkey][lonkey]=VS2
                
        for key in AFl:
            print(key,AFl[key].keys())
        
        print(minLO+100,minLA/1.5)
        return (minLO+100),(minLA/1.5),AFl,VSl
    
    def plot(self):
        lat = np.linspace(0,2./3.,320)
        lon = np.linspace(0,1,320)+100
        for  key_lat in self.AFl:
            for key_lon in self.AFl[key_lat]:
                ax1=plt.subplot(1,2,1)
                plt.pcolormesh(lon+float(key_lon),lat+float(key_lat)*2./3.,self.AFl[key_lat][key_lon])
                ax2=plt.subplot(1,2,2)
                plt.pcolormesh(lon+float(key_lon),lat+float(key_lat)*2./3.,self.VSl[key_lat][key_lon])
                plt.clim((0.,3.))
        plt.show()
        return
    
    def coord_conv(self,coord_string):
        LO=[]
        LA=[]
        I_J=[]
        for l in coord_string:
            la = float(l[:2])/1.5
            lo = 100.+float(l[2:4])
            I = 0
            J = 0

            # secondary area partition
            la += float(l[4])/1.5/8.
            lo += float(l[5])/8.
            I += int(l[4])*40
            J += int(l[5])*40

            # basic grid square
            la += float(l[6])/1.5/(8.*10.)
            lo += float(l[7])/(8.*10.)
            I += int(l[6])*4
            J += int(l[7])*4


            # half grid square
            v = int(l[8])
            if v == 2:
                lo += 1./(8.*10.*2.)
                J += 2
            elif v == 3:
                la += 1./(1.5*8.*10.*2.)
                I += 2
            elif v == 4:
                lo += 1./(8.*10.*2.)
                la += 1./(1.5*8.*10.*2.)
                I += 2
                J += 2

            # quarter grid square
            v = int(l[9])
            if v == 2:
                lo += 1./(8.*10.*4.)
                J += 1
            elif v == 3:
                la += 1./(1.5*8.*10.*4.)
                I += 1
            elif v == 4:
                lo += 1./(8.*10.*4.)
                la += 1./(1.5*8.*10.*4.)
                I += 1
                J += 1
            LO.append(lo)
            LA.append(la)
            I_J.append((I,J))
            
        return LO,LA,I_J

    def create_mesh(self,keyword):
        if keyword=='AFl':
            dic=self.AFl
        if keyword=='VSl':
            dic=self.VSl
        
        lat_len = len(dic.keys())
        lat_min = np.min(list(dic.keys()))
        
        lon_len = 0
        lon_min = np.inf
        
        for lat_key in dic:
            if len(dic[lat_key].keys()) > lon_len:
                lon_len=len(dic[lat_key].keys())
                
            if np.min(list(dic[lat_key].keys())) < lon_min:
                lon_min = np.min(list(dic[lat_key].keys()))
        mesh=np.ones((lat_len*320,lon_len*320))*-9999
        
        for lat_key in dic:
            for lon_key in dic[lat_key]:
                lat=(lat_key-lat_min)*320
                lon=(lon_key-lon_min)*320
                mesh[lat:lat+320,lon:lon+320]=dic[lat_key][lon_key]
        return mesh

    def write_geotiff(self,filename):
        AFl=self.create_mesh('AFl')
        VSl=self.create_mesh('VSl')
        nrows,ncols = VSl.shape
        lores = 1/320
        lares = 1/(320*1.5)
        geotransform = (self.min_LO-lores/2,lores,0,self.min_LA-lares/2,0, lares)  
        
        
        driver = gdal.GetDriverByName('Gtiff')
        dataset = driver.Create(filename, ncols, nrows, 2, gdal.GDT_Float32)
        dataset.SetGeoTransform(geotransform)
        dataset.GetRasterBand(1).WriteArray(VSl)
        dataset.GetRasterBand(2).WriteArray(AFl)
        return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', help='Path to folder of the VS400_M250 files. Defaults to current one.')
    parser.add_argument('--n', help='string of VS400_M250 files to use from given folder. Defaults to all files')
    parser.add_argument('--e', help='filetype ending, defaults to .csv')
    parser.add_argument('--p', help='give any value to plot, defaults False')
    parser.add_argument('--r', help='return Tifffile with given name, defaults False')
    args = parser.parse_args()
    
    if args.f==None:
        folder='.'
    else:
        folder=args.f
        
    if args.n==None:
        filename=None
    else:
        filename=args.n
        
    if args.e == None:
        flag='.csv'
    else:
        flag=args.e
    
    if args.p:
        plot=True
    else:
        plot=False
        
    if args.r:
        tiffname=args.r
    else:
        tiffname=None
        
    test=J_Coord_file(folder,filename,flag,plot,tiffname)

if __name__=='__main__':
    main()
    
