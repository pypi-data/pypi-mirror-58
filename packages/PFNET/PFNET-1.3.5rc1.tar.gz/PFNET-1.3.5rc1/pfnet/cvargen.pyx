#cython: embedsignature=True

#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2015, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

cimport cvargen

# Infinity
VARGEN_INF_P = cvargen.VARGEN_INF_P
VARGEN_INF_Q = cvargen.VARGEN_INF_Q

class VarGeneratorError(Exception):
    """
    Variable generator error exception.
    """

    pass

cdef class VarGenerator:
    """
    Variable generator class.
    """

    cdef cvargen.Vargen* _c_ptr
    cdef bint alloc

    def __init__(self, num_periods=1, alloc=True):
        """
        Variable generator class.

        Parameters
        ----------
        num_periods : int
        alloc : |TrueFalse|
        """

        pass

    def __cinit__(self, num_periods=1, alloc=True):

        if alloc:
            self._c_ptr = cvargen.VARGEN_new(num_periods)
        else:
            self._c_ptr = NULL
        self.alloc = alloc

    def __dealloc__(self):

        if self.alloc:
            cvargen.VARGEN_array_del(self._c_ptr,1)
            self._c_ptr = NULL

    def _get_c_ptr(self):

        return new_CPtr(self._c_ptr)

    def has_flags(self, flag_type, q):
        """
        Determines whether the variable generator has the flags associated with
        certain quantities set.

        Parameters
        ----------
        flag_type : string (|RefFlags|)
        q : string or list of strings (|RefVarGeneratorQuantities|)

        Returns
        -------
        flag : |TrueFalse|
        """

        q = q if isinstance(q,list) else [q]

        return cvargen.VARGEN_has_flags(self._c_ptr,
                                        str2flag[flag_type],
                                        reduce(lambda x,y: x|y,[str2q[self.obj_type][qq] for qq in q],0))

    def is_in_service(self):
        """
        Determines whether the variable generator is in service.

        Returns
        -------
        in_service : |TrueFalse|
        """

        return cvargen.VARGEN_is_in_service(self._c_ptr)

    def is_equal(self, other):
        """
        Determines whether the var generator is equal to given var generator.

        Parameters
        ----------
        other : |VarGenerator|

        Returns
        -------
        flag : |TrueFalse|
        """

        cdef VarGenerator g_other

        if not isinstance(other,VarGenerator):
            return False

        g_other = other

        return cvargen.VARGEN_is_equal(self._c_ptr,g_other._c_ptr)

    def get_var_info_string(self, index):
        """
        Gets info string of variable associated with index.

        Parameters
        ----------
        index : int

        Returns
        -------
        info : string
        """

        cdef char* info_string = cvargen.VARGEN_get_var_info_string(self._c_ptr, index)
        if info_string:
            s = info_string.decode('UTF-8')
            free(info_string)
            return s
        else:
            raise VarGeneratorError('index does not correspond to any variable')

    property in_service:
        """ In service flag (boolean). """
        def __get__(self): return cvargen.VARGEN_is_in_service(self._c_ptr)
        def __set__(self, in_service): cvargen.VARGEN_set_in_service(self._c_ptr, in_service)

    property num_periods:
        """ Number of time periods (int). """
        def __get__(self): return cvargen.VARGEN_get_num_periods(self._c_ptr)

    property name:
        """ Variable generator name (string). """
        def __get__(self):
            return cvargen.VARGEN_get_name(self._c_ptr).decode('UTF-8')
        def __set__(self,name):
            name = name.encode('UTF-8')
            cvargen.VARGEN_set_name(self._c_ptr,name)

    property obj_type:
        """ Object type (string). """
        def __get__(self): return obj2str[cvargen.VARGEN_get_obj_type(self._c_ptr)]

    property index:
        """ Variable generator index (int). """
        def __get__(self): return cvargen.VARGEN_get_index(self._c_ptr)

    property index_P:
        """ Index of variable generator active power variable (int or |Array|). """
        def __get__(self):
            return IntArray(cvargen.VARGEN_get_index_P_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)

    property index_Q:
        """ Index of variable generator reactive power variable (int or |Array|). """
        def __get__(self):
            return IntArray(cvargen.VARGEN_get_index_Q_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)

    property bus:
        """ |Bus| to which variable generator is connected. """
        def __get__(self):
            return new_Bus(cvargen.VARGEN_get_bus(self._c_ptr))
        def __set__(self,bus):
            cdef Bus cbus
            if not isinstance(bus,Bus) and bus is not None:
                raise VarGeneratorError('Not a Bus type object')
            cbus = bus
            cvargen.VARGEN_set_bus(self._c_ptr,cbus._c_ptr if bus is not None else NULL) 

    property P:
        """ Variable generator active power after curtailments (p.u. system base MVA) (float or |Array|). """
        def __get__(self):
            return DoubleArray(cvargen.VARGEN_get_P_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)
        def __set__(self, v):
            DoubleArray(cvargen.VARGEN_get_P_array(self._c_ptr), self.num_periods)[:] = v

    property P_ava:
        """ Variable generator available active power (p.u. system base MVA) (float or |Array|). """
        def __get__(self):
            return DoubleArray(cvargen.VARGEN_get_P_ava_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)
        def __set__(self, v):
            DoubleArray(cvargen.VARGEN_get_P_ava_array(self._c_ptr), self.num_periods)[:] = v

    property P_max:
        """ Variable generator active power upper limit (p.u. system base MVA) (float). """
        def __get__(self): return cvargen.VARGEN_get_P_max(self._c_ptr)
        def __set__(self,P): cvargen.VARGEN_set_P_max(self._c_ptr,P)

    property P_min:
        """ Variable generator active power lower limit (p.u. system base MVA) (float). """
        def __get__(self): return cvargen.VARGEN_get_P_min(self._c_ptr)
        def __set__(self,P): cvargen.VARGEN_set_P_min(self._c_ptr,P)

    property P_std:
        """ Variable generator active power standard deviation (p.u. system base MVA) (float or |Array|). """
        def __get__(self):
            return DoubleArray(cvargen.VARGEN_get_P_std_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)
        def __set__(self, v):
            DoubleArray(cvargen.VARGEN_get_P_std_array(self._c_ptr), self.num_periods)[:] = v

    property Q:
        """ Variable generator reactive power (p.u. system base MVA) (float or |Array|). """
        def __get__(self):
            return DoubleArray(cvargen.VARGEN_get_Q_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)
        def __set__(self, v):
            DoubleArray(cvargen.VARGEN_get_Q_array(self._c_ptr), self.num_periods)[:] = v

    property Q_max:
        """ Variable generator maximum reactive power (p.u. system base MVA) (float). """
        def __get__(self): return cvargen.VARGEN_get_Q_max(self._c_ptr)
        def __set__(self,Q): cvargen.VARGEN_set_Q_max(self._c_ptr,Q)

    property Q_min:
        """ Variable generator minimum reactive power (p.u. system base MVA) (float). """
        def __get__(self): return cvargen.VARGEN_get_Q_min(self._c_ptr)
        def __set__(self,Q): cvargen.VARGEN_set_Q_min(self._c_ptr,Q)

    property json_string:
        """ JSON string (string). """
        def __get__(self): 
            cdef char* json_string = cvargen.VARGEN_get_json_string(self._c_ptr, NULL)
            s = json_string.decode('UTF-8')
            free(json_string)
            return s

    property flags_vars:
        """ Flags associated with variable quantities (byte). """
        def __get__(self): return cvargen.VARGEN_get_flags_vars(self._c_ptr)

    property flags_fixed:
        """ Flags associated with fixed quantities (byte). """
        def __get__(self): return cvargen.VARGEN_get_flags_fixed(self._c_ptr)

    property flags_bounded:
        """ Flags associated with bounded quantities (byte). """
        def __get__(self): return cvargen.VARGEN_get_flags_bounded(self._c_ptr)

    property flags_sparse:
        """ Flags associated with sparse quantities (byte). """
        def __get__(self): return cvargen.VARGEN_get_flags_sparse(self._c_ptr)

cdef new_VarGenerator(cvargen.Vargen* g):
    if g is not NULL:
        gen = VarGenerator(alloc=False)
        gen._c_ptr = g
        return gen
    else:
        raise VarGeneratorError('no vargen data')
