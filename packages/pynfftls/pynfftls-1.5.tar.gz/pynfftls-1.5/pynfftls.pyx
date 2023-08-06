'''
                      PyNFFTls

This Python module provides the Fast Lomb-Scargle periodogram
developed by B. Leroy (2012, Astron. Astrophys. 545, A50)

It is based on the Non-equispaced Fast Fourier Transform (NFFTn http://www-user.tu-chemnitz.de/~potts/nfft/download.php) as well as the FFTW3 library (http://www.fftw.org/).
Both librairies must be installed.

Calling sequence:
    (f,p) = period(t,y,ofac,hifac)

For more details, see the associated documentation
For a complete example, see nfftls_test.py


This Python module also provides the following methods:
- the Non-equidistant Fast Fourier Transform (NFFT, see http://www-user.tu-chemnitz.de/~potts/nfft/) of a time series:
    (f,A) = nfft(t,y,p,d)
For more details, see the associated documentation

- the Discrete  Fourier Transform  (DFT) of a time series:
    A = dft(t,y,f)
For more details, see the associated documentation

For a complete example, see nfftls_test2.py

Change history:
1.5 (02/01/2020): now compatible with  Python 3 (Cython is now used as interface)  
1.4 (11/04/2019): interface of nfft() changed, this function can now compute an over-sampled fourier transform
1.3 (10/04/2019):  correct a bug that lead to over-estimate the frequency by a relative factor of 1e-5
1.2 (4/06/2013): 
1.1 (18/01/2013):
1.0 (3/01/2013): initial version

R. Samadi, LESIA (http://lesia.obspm.fr), Observatoire de Paris, 22 Dec. 2012

'''
import numpy as np
# "cimport" is used to import special compile-time information
# about the numpy module (this is stored in a file numpy.pxd which is
# currently part of the Cython distribution).
cimport numpy as np
# We now need to fix a datatype for our arrays. I've used the variable
# DTYPE for this, which is assigned to the usual NumPy runtime
# type info object.
DTYPE = np.double
CDTYPE = np.complex128
ITYPE = np.int
U64TYPE = np.uint64
# "ctypedef" assigns a corresponding compile-time type to DTYPE_t. For
# every type in the numpy module there's a corresponding compile-time
# type with a _t-suffix.
ctypedef np.double_t DTYPE_t
ctypedef np.complex128_t CDTYPE_t
ctypedef np.int_t ITYPE_t
ctypedef np.uint64_t U64TYPE_t
# "def" can type its arguments but not have a return type. The type of the
# arguments for a "def" function is checked at run-time when entering the
# function.

cimport cython

cdef extern from "ls.h":
    int periodogram_simple(const double* tobs, const double* yobs, int npts, double over, double hifac, double *  freqs  , double *  Pn   ) ;

cdef extern from "utils.h":
    extern void reduce(double* t, int npts, double oversampling);

cdef extern from "nfft.h":
    extern void cnfft(const double* t, const double complex * y, int n, int m,  double complex * d ) ;
    extern void rnfft(const double* t, const double* y, int n, int m,  double complex * d ) ;
    extern void rdft(const double* t, const double* y,  int n, const double *f, int m, int dir ,  double complex * d ) ;
    extern void cdft(const double* t, const double complex * y,  int n, const double *f, int m, int dir ,  double complex * d ) ;

def dft(np.ndarray [DTYPE_t,ndim=1, mode='c'] t , np.ndarray   y, np.ndarray [DTYPE_t,ndim=1, mode='c'] f, int dir = 1):
    '''
    Computes the Discrete Fourier Transform (DFT) of a time series
    
    A = dft(t,y,f,dir=1)
    
    Inputs:
    t: times
    y: signal (real or complex)
    f: the frequencies for which we want the Fourier component
    dir (keyword): direction of the transform: dir >= 0 for a forward transform and dir < 0 for an inverse transform
    
    Outputs:
    A: the Fourier components (complex numbers) as many as frequncies
    
    '''
    cdef int n = t.size
    cdef int m = f.size
    cdef np.ndarray [CDTYPE_t,ndim=1, mode='c'] Ac 
    cdef np.ndarray [CDTYPE_t,ndim=1, mode='c'] yc 
    cdef np.ndarray [DTYPE_t,ndim=1, mode='c'] yr 


    Ac = np.empty(m,dtype=CDTYPE)
    
    if(y.dtype == CDTYPE):
        yc = y
        cdft(&t[0],&yc[0],n,&f[0],m,dir,&Ac[0])
    else:    
        yr = y
        rdft(&t[0],&yr[0],n,&f[0],m,dir,&Ac[0])

    return Ac

    
def nfft(np.ndarray [DTYPE_t,ndim=1, mode='c'] t , np.ndarray   y, int m , double dt = 1., int over = 1):
    '''
    Computes the Non-equidistant Fast Fourier Transform (NFFT, see http://www-user.tu-chemnitz.de/~potts/nfft/) 
    of a time series
    
    (f,A) = nfft(t,y,p,dt=1)
    
    Inputs:
    t: times
    y: signal (real or complex). None for computing the FT of the window. 
    p: number of positives frequencies
    dt: sampling time (default: 1)
    
    Outputs:
    f: the frequencies ( 2*p elements)
    A: the Fourier spectrum (complex numbers) with 2p elements
    A[1:p] contains the positive-frequency terms, and A[p:] contains the negative-frequency terms, in order of decreasingly negative frequency.
    
    '''
    cdef int n = t.size
    cdef i 
    cdef double df = 1./( (t[n-1]-t[0])*over) 
    cdef np.ndarray [CDTYPE_t,ndim=1, mode='c'] Ac 
    cdef np.ndarray [CDTYPE_t,ndim=1, mode='c'] yc 
    cdef np.ndarray [DTYPE_t,ndim=1, mode='c'] yr 

    cdef np.ndarray [DTYPE_t,ndim=1, mode='c'] f = np.empty(2*m,dtype=DTYPE)
    cdef np.ndarray [DTYPE_t,ndim=1, mode='c'] tn = np.empty(n,dtype=DTYPE)
    tn[:] = t[:]

    reduce(&tn[0] , n, 1.)
    for i in range(m):
        f[i] = i*df  # positive frequencies (m) , null frequency included
    for i in range(m,2*m): 
        f[i] = -(2*m - i)*df  # negative frequencies (m)

    Ac = np.empty(2*m,dtype=CDTYPE)
    
    if(y.dtype == CDTYPE):
        yc = y
        cnfft(&tn[0],&yc[0],n,m,&Ac[0])
    else:    
        yr = y
        rnfft(&tn[0],&yr[0],n,m,&Ac[0])
        
    return f,Ac


def period(np.ndarray [DTYPE_t,ndim=1, mode='c'] time , np.ndarray [DTYPE_t,ndim=1, mode='c']  y, ofac , hifac):
    '''
    Computes the Lomb-Scargle normalised periodogram of a time series
    
    (f,p) = period(t,y,ofac,hifac)
    t: times
    y: signal
    ofac: oversampling factor
    hifac: highest frequency in units of the Nyquist frequency
    
    Return: a tuple (f,p) where: 
    p: normalised periodogram
    f: frequencies
    
    For more details see Leroy (2012, Astron. Astrophys. 545, A50)
    
    '''
    
    cdef int n = time.size
    cdef int nfreq = 0
    cdef np.ndarray [DTYPE_t,ndim=1, mode='c'] f = np.zeros(n,dtype=DTYPE)
    cdef np.ndarray [DTYPE_t,ndim=1, mode='c'] p = np.zeros(n,dtype=DTYPE)
  
    nfreq = periodogram_simple(&time[0],&y[0],n,ofac,hifac,&f[0],&p[0])
    nfreq = min(nfreq,n)
    return f[0:nfreq],p[0:nfreq]
