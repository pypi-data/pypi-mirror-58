#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2015, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

cdef extern from "pfnet/vargen.h":

    ctypedef struct Vargen
    ctypedef struct Bus
    ctypedef double REAL
    
    cdef char VARGEN_VAR_P
    cdef char VARGEN_VAR_Q

    cdef double VARGEN_INF_P
    cdef double VARGEN_INF_Q

    cdef char VARGEN_PROP_ANY

    char VARGEN_get_flags_vars(Vargen* gen)
    char VARGEN_get_flags_fixed(Vargen* gen)
    char VARGEN_get_flags_bounded(Vargen* gen)
    char VARGEN_get_flags_sparse(Vargen* gen)

    int VARGEN_get_num_periods(Vargen* gen)
    char* VARGEN_get_name(Vargen* gen)
    char VARGEN_get_obj_type(void* gen)
    int VARGEN_get_index(Vargen* gen)
    int* VARGEN_get_index_P_array(Vargen* gen)
    int* VARGEN_get_index_Q_array(Vargen* gen)
    Bus* VARGEN_get_bus(Vargen* gen)
    REAL* VARGEN_get_P_array(Vargen* gen)
    REAL* VARGEN_get_P_ava_array(Vargen* gen)
    REAL VARGEN_get_P_max(Vargen* gen)
    REAL VARGEN_get_P_min(Vargen* gen)
    REAL* VARGEN_get_P_std_array(Vargen* gen)
    REAL* VARGEN_get_Q_array(Vargen* gen)
    REAL VARGEN_get_Q_max(Vargen* gen)
    REAL VARGEN_get_Q_min(Vargen* gen)
    Vargen* VARGEN_get_next(Vargen* gen)
    char* VARGEN_get_json_string(Vargen* gen, char* output)
    char* VARGEN_get_var_info_string(Vargen* gen, int index)
    bint VARGEN_has_flags(Vargen* gen, char flag_type, char mask)
    bint VARGEN_is_in_service(void* gen)
    bint VARGEN_is_equal(Vargen* gen, Vargen* other)
    Vargen* VARGEN_new(int num_periods)
    Vargen* VARGEN_array_new(int size, int num_periods)
    void VARGEN_array_del(Vargen* gen_array, int size)
    void VARGEN_set_bus(Vargen* gen, Bus* bus)
    void VARGEN_set_name(Vargen* gen, char* name)
    void VARGEN_set_P_max(Vargen* gen, REAL P_max)
    void VARGEN_set_P_min(Vargen* gen, REAL P_min)
    void VARGEN_set_Q_max(Vargen* gen, REAL Q)
    void VARGEN_set_Q_min(Vargen* gen, REAL Q)
    void VARGEN_set_in_service(Vargen* gen, bint in_service)
