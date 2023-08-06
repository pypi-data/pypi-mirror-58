#cython: embedsignature=True

#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2015, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

import numpy as np
cimport numpy as np

from functools import reduce

cimport cconstants
cimport cvec
cimport cmat
cimport cparser_raw
cimport cparser_epc

from scipy import misc
import tempfile

from scipy.sparse import coo_matrix

from libc.stdlib cimport free, malloc

np.import_array()

# Constants
###########

PI = cconstants.PI

# Information
#############

def has_raw_parser():
    return bool(cparser_raw.HAVE_RAW_PARSER)

def has_epc_parser():
    return bool(cparser_epc.HAVE_EPC_PARSER)

# C pointer
###########

cdef class CPtr:
    """
    C Pointer class.
    """

    cdef void* _c_ptr

cdef new_CPtr(void* ptr):
    cptr = CPtr()
    cptr._c_ptr = ptr
    return cptr

# Vector
########

cdef extern from "numpy/arrayobject.h":
    void PyArray_ENABLEFLAGS(np.ndarray arr, int flags)
    void PyArray_CLEARFLAGS(np.ndarray arr, int flags)

cdef Vector(cvec.Vec* v, owndata=False):
    cdef np.npy_intp shape[1]
    if v is not NULL:
        shape[0] = <np.npy_intp>cvec.VEC_get_size(v)
        arr = np.PyArray_SimpleNewFromData(1,shape,np.NPY_DOUBLE,cvec.VEC_get_data(v))
        if owndata:
            PyArray_ENABLEFLAGS(arr,np.NPY_OWNDATA)
        return arr
    else:
        return np.zeros(0)

# Double array
##############

cdef DoubleArray(double* a, int size, owndata=False, toscalar=False):
    cdef np.npy_intp shape[1]
    if a is not NULL:
        shape[0] = <np.npy_intp>size
        arr = np.PyArray_SimpleNewFromData(1,shape,np.NPY_DOUBLE,a)
        if owndata:
            PyArray_ENABLEFLAGS(arr,np.NPY_OWNDATA)
        if arr.size == 1 and toscalar:
            return AttributeFloat(arr[0])
        else:
            return arr
    else:
        return np.zeros(0)        

# Int array
###########

cdef IntArray(int* a, int size, owndata=False, toscalar=False):
    cdef np.npy_intp shape[1]
    if a is not NULL:
        shape[0] = <np.npy_intp>size
        arr = np.PyArray_SimpleNewFromData(1,shape,np.NPY_INT,a)
        if owndata:
            PyArray_ENABLEFLAGS(arr,np.NPY_OWNDATA)
        if arr.size == 1 and toscalar:
            return AttributeInt(arr[0])
        else:
            return arr
    else:
        return np.zeros(0,dtype='int')

# Matrix
########

cdef Matrix(cmat.Mat* m, owndata=False):
    cdef np.npy_intp shape[1]
    if m is not NULL:
        shape[0] = <np.npy_intp> cmat.MAT_get_nnz(m)
        size1 = cmat.MAT_get_size1(m)
        size2 = cmat.MAT_get_size2(m)
        row = np.PyArray_SimpleNewFromData(1,shape,np.NPY_INT,cmat.MAT_get_row_array(m))
        col = np.PyArray_SimpleNewFromData(1,shape,np.NPY_INT,cmat.MAT_get_col_array(m))
        data = np.PyArray_SimpleNewFromData(1,shape,np.NPY_DOUBLE,cmat.MAT_get_data_array(m))
        if owndata:
            PyArray_ENABLEFLAGS(row,np.NPY_OWNDATA)
            PyArray_ENABLEFLAGS(col,np.NPY_OWNDATA)
            PyArray_ENABLEFLAGS(data,np.NPY_OWNDATA)
        return coo_matrix((data,(row,col)),shape=(size1,size2))
    else:
        return coo_matrix(([],([],[])),shape=(0,0))

# Attribute array
#################

class AttributeArray(np.ndarray):

    def __new__(cls, data, func=None):
        cls.func = func
        return np.asarray(data).view(cls)

    def __setitem__(self, key, value):
        self.func(value, key)
        np.ndarray.__setitem__(self, key, value)

# Attribute int
###############

class AttributeInt(np.int32):

    def __len__(self):
        return 0

    def __getitem__(self, key):
        if key == 0:
            return self
        else:
            raise IndexError

# Attribute float
#################

class AttributeFloat(float):

    def __getitem__(self, key):
        if key == 0:
            return self
        else:
            raise IndexError

# Others
########

include "cstrings.pyx" 
include "cparser.pyx"
include "cbus.pyx"
include "cbranch.pyx"
include "cgen.pyx"
include "cshunt.pyx"
include "cload.pyx"
include "cvargen.pyx"
include "cbat.pyx"
include "cbus_dc.pyx"
include "cbranch_dc.pyx"
include "cconv_vsc.pyx"
include "cconv_csc.pyx"
include "cfacts.pyx"
include "cbrycor.pyx"
include "cnet.pyx"
include "ccont.pyx"
include "cfunc.pyx"
include "cconstr.pyx"
include "cheur.pyx"
include "cprob.pyx"
