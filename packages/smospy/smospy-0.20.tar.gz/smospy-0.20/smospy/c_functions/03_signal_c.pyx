# distutils: language = c++
# Cython interface file for wrapping the object

from libcpp.vector cimport vector
import cython
import numpy as np
cimport numpy as np


cdef extern from "02_signal_c.h" namespace "std" :
  cdef cppclass C_signal_lib:
        c_signal_lib() except +
        double sum_vec(vector[double])
        vector[double] test(vector[double])
        vector[vector[double]] test2(vector[vector[double]])
        vector[vector[double]] icbm(vector[vector[double]],int,int,double,int)
        vector[vector[double]] acc2disp(vector[double], int , int )
        
@cython.embedsignature(True)
cdef class Py_C_signal_lib:
    '''
    class wrapper for c++ library containing icbm and acc_2_disp functions
    
    Examples
    --------
    >>> wrapper = Py_C_signal_lib()
    >>> t = [1,2,3,4,5]
    >>> print(wrapper.icbm([t,t,t]))
    [[-2.5 -1.5 -0.5  0.5  1.5]
    [-2.5 -1.5 -0.5  0.5  1.5]
    [-2.5 -1.5 -0.5  0.5  1.5]]
    
    '''
    def __init__(self):
        pass
    
    cdef C_signal_lib *self_c_signal      # hold a C++ instance which we're wrapping
    
    def __cinit__(self):
        self.self_c_signal = new C_signal_lib()
        
    def __dealloc__(self):
        del self.self_c_signal
        
    def sum_vec(self, sv):
        '''
        Test function for people wanting to know how wrapping c++ functions work.
        
        Parameters
        ----------
        
        sv : ndarray
        
        Returns
        -------
        
        float
            sum of array
        '''
        return self.self_c_signal.sum_vec(sv)
    
    def test(self,sv):
        '''
        Test function for people wanting to know how wrapping c++ functions work.
        
        Parameters
        ----------
        
        sv : ndarray
        
        Returns
        -------
        
        ndarray
            array with length of sv filled with 100
        '''
        return self.self_c_signal.test(sv)
    
    def test2(self,sv):
        '''
        Test function for armadillo library and multidimensional arguments.
        
        Parameters
        ----------
        
        sv : ndarray[ndarray]
        
        Returns
        -------
        
        ndarray
            returns input and prints a random 4x4 array by using arma::randu(4,4)
        '''
        return self.self_c_signal.test2(sv)
    
    def icbm(self,x,Nsmin=1,Nsmax=6,thrshld=1e-5 ,nmin=500):
        '''
        icbm function by Sebastian von Specht for baseline correction of strong motion data.
        
        Parameters
        ----------
        
        x : ndarray
            3 component data given in multidimensional array [Z,N,E] or [Z,R,T]
        
        Nsmin : int, optional
             ... defaults to 1
        
        Nsmax : int, optional
             ... defaults to 6
        
        thrshld : float, optional
             ... defaults to 1e-5
             
        nmin : int, optional
             ... defaults to 500
        
        Returns
        -------
        
        ndarray
            array [Z,N,E] or [Z,R,T] baseline corrected
        
        References
        ----------
        Sebastian von Specht(2019). SRL Early Edition ICBM — Integrated Combined Baseline Modification : An Algorithm for Segmented Baseline Estimation. XX(Xx), 1–13. 
        https://doi.org/10.1785/0220190134
        '''
        x=np.array(x)
        return np.array(self.self_c_signal.icbm(x,Nsmin,Nsmax,thrshld,nmin))
    
    def acc2disp(self,x,freq,itp=0,itf=0):
        '''
        acc2disp function by Sebastian von Specht implementing the algorithm by Wang,R for baseline correction of strong motion data.
        
        Parameters
        ----------
        
        x : ndarray
            acceleration trace of signal
        
        freq : float
             sample frequency of the signal
        
        itp : float, optional
             ... defaults to 0
        
        itf : float, optional
             ... defaults to 0
        
        Returns
        -------
        
        ndarray
            array [acc,vel,disp] corrected
        
        References
        ----------
            Wang, R., Schurr, B., Milkereit, C., Shao, Z., and Jin, M.: "An Im- proved Automatic Scheme for Empirical Baseline Correction of Digital Strong-Motion Records",
            Bull. Seismol. Soc. Am., 101, 2029–2044, https://doi.org/10.1785/0120110039, 2011
        '''
        trace = np.array(self.self_c_signal.acc2disp(x,itp,itf))
        return (trace/[[1],[freq],[freq*freq]])
