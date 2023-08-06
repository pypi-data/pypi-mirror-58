#cython: embedsignature=True

#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2015, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

cimport cbat

# Infinity
BAT_INF_P = cbat.BAT_INF_P
BAT_INF_E = cbat.BAT_INF_E

class BatteryError(Exception):
    """
    Battery error exception.
    """

    pass

cdef class Battery:
    """
    Battery class.
    """

    cdef cbat.Bat* _c_ptr
    cdef bint alloc

    def __init__(self, num_periods=1, alloc=True):
        """
        Battery class.

        Parameters
        ----------
        num_periods : int
        alloc : |TrueFalse|
        """

        pass

    def __cinit__(self, num_periods=1, alloc=True):

        if alloc:
            self._c_ptr = cbat.BAT_new(num_periods)
        else:
            self._c_ptr = NULL
        self.alloc = alloc

    def __dealloc__(self):

        if self.alloc:
            cbat.BAT_array_del(self._c_ptr,1)
            self._c_ptr = NULL

    def _get_c_ptr(self):

        return new_CPtr(self._c_ptr)

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

        cdef char* info_string = cbat.BAT_get_var_info_string(self._c_ptr, index)
        if info_string:
            s = info_string.decode('UTF-8')
            free(info_string)
            return s
        else:
            raise BatteryError('index does not correspond to any variable')

    def has_flags(self, flag_type, q):
        """
        Determines whether the battery has the flags associated with
        certain quantities set.

        Parameters
        ----------
        flag_type : string (|RefFlags|)
        q : string or list of strings (|RefBatteryQuantities|)

        Returns
        -------
        flag : |TrueFalse|
        """

        q = q if isinstance(q,list) else [q]

        return cbat.BAT_has_flags(self._c_ptr,
                                  str2flag[flag_type],
                                  reduce(lambda x,y: x|y,[str2q[self.obj_type][qq] for qq in q],0))

    def is_in_service(self):
        """
        Determines whether the battery is in service.

        Returns
        -------
        in_service : |TrueFalse|
        """

        return cbat.BAT_is_in_service(self._c_ptr)

    def is_equal(self, other):
        """
        Determines whether the battery is equal to given battery.

        Parameters
        ----------
        other : |Battery|

        Returns
        -------
        flag : |TrueFalse|
        """

        cdef Battery b_other

        if not isinstance(other,Battery):
            return False

        b_other = other

        return cbat.BAT_is_equal(self._c_ptr,b_other._c_ptr)

    property in_service:
        """ In service flag (boolean). """
        def __get__(self): return cbat.BAT_is_in_service(self._c_ptr)
        def __set__(self, in_service): cbat.BAT_set_in_service(self._c_ptr, in_service)

    property name:
        """ Battery name (string). """
        def __get__(self):
            return cbat.BAT_get_name(self._c_ptr).decode('UTF-8')
        def __set__(self,name):
            name = name.encode('UTF-8')
            cbat.BAT_set_name(self._c_ptr,name)

    property num_periods:
        """ Number of time periods (int). """
        def __get__(self): return cbat.BAT_get_num_periods(self._c_ptr)

    property obj_type:
        """ Object type (string). """
        def __get__(self): return obj2str[cbat.BAT_get_obj_type(self._c_ptr)]

    property index:
        """ Battery index (int). """
        def __get__(self): return cbat.BAT_get_index(self._c_ptr)

    property index_Pc:
        """ Index of battery charging power variable (int or |Array|). """
        def __get__(self):
            return IntArray(cbat.BAT_get_index_Pc_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)
        
    property index_Pd:
        """ Index of battery discharging power variable (int or |Array|). """
        def __get__(self):
            return IntArray(cbat.BAT_get_index_Pd_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)

    property index_E:
        """ Index of battery energy level variable (int or |Array|). """
        def __get__(self):
            return IntArray(cbat.BAT_get_index_E_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)

    property bus:
        """ |Bus| to which battery is connected. """
        def __get__(self):
            return new_Bus(cbat.BAT_get_bus(self._c_ptr))
        def __set__(self, bus):
            cdef Bus cbus
            if not isinstance(bus,Bus) and bus is not None:
                raise BatteryError('Not a Bus type object')
            cbus = bus
            cbat.BAT_set_bus(self._c_ptr,cbus._c_ptr if bus is not None else NULL)

    property P:
        """ Battery charging power (p.u. system base MVA) (float or |Array|). """
        def __get__(self):
            return DoubleArray(cbat.BAT_get_P_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)
        def __set__(self, v):
            DoubleArray(cbat.BAT_get_P_array(self._c_ptr), self.num_periods)[:] = v

    property P_max:
        """ Battery charging power upper limit (p.u. system base MVA) (float). """
        def __get__(self): return cbat.BAT_get_P_max(self._c_ptr)
        def __set__(self,P): cbat.BAT_set_P_max(self._c_ptr,P)

    property P_min:
        """ Battery charging power lower limit (p.u. system base MVA) (float). """
        def __get__(self): return cbat.BAT_get_P_min(self._c_ptr)
        def __set__(self,P): cbat.BAT_set_P_min(self._c_ptr,P)

    property E:
        """ Battery energy level at the beginning of a time period (p.u. system base MVA times time unit) (float or |Array|). """
        def __get__(self):
            return DoubleArray(cbat.BAT_get_E_array(self._c_ptr), self.num_periods, owndata=False, toscalar=True)
        def __set__(self, v):
            DoubleArray(cbat.BAT_get_E_array(self._c_ptr), self.num_periods)[:] = v

    property E_init:
        """ Initial battery energy level (p.u. system base MVA times time unit) (float). """
        def __get__(self): return cbat.BAT_get_E_init(self._c_ptr)
        def __set__(self,E): cbat.BAT_set_E_init(self._c_ptr,E)

    property E_final:
        """ Battery energy level at the end of the last time period (p.u. system base MVA times time unit) (float). """
        def __get__(self): return cbat.BAT_get_E_final(self._c_ptr)
        def __set__(self,E): cbat.BAT_set_E_final(self._c_ptr,E)

    property E_max:
        """ Battery energy level upper limit (p.u. system base MVA times time unit) (float). """
        def __get__(self): return cbat.BAT_get_E_max(self._c_ptr)
        def __set__(self,E): cbat.BAT_set_E_max(self._c_ptr,E)

    property eta_c:
        """ Battery charging efficiency (unitless) (float). """
        def __get__(self): return cbat.BAT_get_eta_c(self._c_ptr)
        def __set__(self,eta_c): cbat.BAT_set_eta_c(self._c_ptr,eta_c)

    property eta_d:
        """ Battery discharging efficiency (unitless) (float). """
        def __get__(self): return cbat.BAT_get_eta_d(self._c_ptr)
        def __set__(self,eta_d): cbat.BAT_set_eta_d(self._c_ptr,eta_d)

    property json_string:
        """ JSON string (string). """
        def __get__(self): 
            cdef char* json_string = cbat.BAT_get_json_string(self._c_ptr, NULL)
            s = json_string.decode('UTF-8')
            free(json_string)
            return s

    property flags_vars:
        """ Flags associated with variable quantities (byte). """
        def __get__(self): return cbat.BAT_get_flags_vars(self._c_ptr)

    property flags_fixed:
        """ Flags associated with fixed quantities (byte). """
        def __get__(self): return cbat.BAT_get_flags_fixed(self._c_ptr)

    property flags_bounded:
        """ Flags associated with bounded quantities (byte). """
        def __get__(self): return cbat.BAT_get_flags_bounded(self._c_ptr)

    property flags_sparse:
        """ Flags associated with sparse quantities (byte). """
        def __get__(self): return cbat.BAT_get_flags_sparse(self._c_ptr)

cdef new_Battery(cbat.Bat* b):
    if b is not NULL:
        bat = Battery(alloc=False)
        bat._c_ptr = b
        return bat
    else:
        raise BatteryError('no battery data')
