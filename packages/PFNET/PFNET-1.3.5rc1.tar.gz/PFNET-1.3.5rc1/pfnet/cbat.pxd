#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2015, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

cdef extern from "pfnet/bat.h":

    ctypedef struct Bat
    ctypedef struct Bus
    ctypedef double REAL

    cdef char BAT_VAR_P
    cdef char BAT_VAR_E

    cdef double BAT_INF_P
    cdef double BAT_INF_E
       
    cdef char BAT_PROP_ANY

    char BAT_get_flags_vars(Bat* bat)
    char BAT_get_flags_fixed(Bat* bat)
    char BAT_get_flags_bounded(Bat* bat)
    char BAT_get_flags_sparse(Bat* bat)

    char* BAT_get_name(Bat* bat)
    char BAT_get_obj_type(void* bat)
    int BAT_get_num_periods(Bat* bat)
    int BAT_get_index(Bat* bat)
    int* BAT_get_index_Pc_array(Bat* bat)
    int* BAT_get_index_Pd_array(Bat* bat)
    int* BAT_get_index_E_array(Bat* bat)
    Bus* BAT_get_bus(Bat* bat)
    REAL* BAT_get_P_array(Bat* bat)
    REAL BAT_get_P_max(Bat* bat)
    REAL BAT_get_P_min(Bat* bat)
    REAL* BAT_get_E_array(Bat* bat)
    REAL BAT_get_E_max(Bat* bat)
    REAL BAT_get_E_init(Bat* bat)
    REAL BAT_get_E_final(Bat* bat)
    REAL BAT_get_eta_c(Bat* bat)
    REAL BAT_get_eta_d(Bat* bat)
    Bat* BAT_get_next(Bat* bat)
    char* BAT_get_json_string(Bat* bat, char* output)
    char* BAT_get_var_info_string(Bat* bat, int index)
    bint BAT_has_flags(Bat* bat, char flag_type, char mask)
    bint BAT_is_equal(Bat* bat, Bat* other)
    bint BAT_is_in_service(void* bat)
    Bat* BAT_new(int num_periods)
    Bat* BAT_array_new(int size, int num_periods)
    void BAT_array_del(Bat* bat_array, int size)
    void BAT_set_name(Bat* bat, char* name)
    void BAT_set_bus(Bat* bat, Bus* bus)
    void BAT_set_P_min(Bat* bat, REAL P_min)
    void BAT_set_P_max(Bat* bat, REAL P_max)
    void BAT_set_E_max(Bat* bat, REAL E)
    void BAT_set_E_init(Bat* bat, REAL E)
    void BAT_set_E_final(Bat* bat, REAL E)
    void BAT_set_eta_c(Bat* bat, REAL eta_c)
    void BAT_set_eta_d(Bat* bat, REAL eta_d)
    void BAT_set_in_service(Bat* bat, bint in_service)
