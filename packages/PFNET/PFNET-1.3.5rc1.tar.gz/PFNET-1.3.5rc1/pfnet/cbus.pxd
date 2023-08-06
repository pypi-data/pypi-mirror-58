#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2015, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

cimport cnet

cdef extern from "pfnet/bus.h":

    ctypedef struct Bus
    ctypedef struct Gen
    ctypedef struct Load
    ctypedef struct Branch
    ctypedef struct Shunt
    ctypedef struct Vargen
    ctypedef struct Bat
    ctypedef struct ConvCSC
    ctypedef struct ConvVSC
    ctypedef struct Facts
    ctypedef double REAL
    ctypedef char BOOL

    cdef char BUS_VAR_VMAG
    cdef char BUS_VAR_VANG

    cdef double BUS_INF_V_MAG
    cdef double BUS_INF_V_ANG

    cdef char BUS_PROP_ANY
    cdef char BUS_PROP_SLACK
    cdef char BUS_PROP_VSET_REG
    cdef char BUS_PROP_REG_BY_GEN
    cdef char BUS_PROP_REG_BY_TRAN
    cdef char BUS_PROP_REG_BY_SHUNT
    cdef char BUS_PROP_NOT_REG_BY_GEN
    cdef char BUS_PROP_NOT_SLACK

    cdef char BUS_SENS_LARGEST
    cdef char BUS_SENS_P_BALANCE
    cdef char BUS_SENS_Q_BALANCE
    cdef char BUS_SENS_V_MAG_U_BOUND
    cdef char BUS_SENS_V_MAG_L_BOUND
    cdef char BUS_SENS_V_ANG_U_BOUND
    cdef char BUS_SENS_V_ANG_L_BOUND
    cdef char BUS_SENS_V_SET_REG
    cdef char BUS_SENS_V_REG_BY_TRAN
    cdef char BUS_SENS_V_REG_BY_SHUNT

    cdef char BUS_MIS_LARGEST
    cdef char BUS_MIS_ACTIVE
    cdef char BUS_MIS_REACTIVE

    char BUS_get_flags_vars(Bus* bus)
    char BUS_get_flags_fixed(Bus* bus)
    char BUS_get_flags_bounded(Bus* bus)
    char BUS_get_flags_sparse(Bus* bus)

    int BUS_get_area(Bus* bus)
    int BUS_get_zone(Bus* bus)
    char BUS_get_obj_type(void* bus)
    int BUS_get_num_periods(Bus* bus)
    int BUS_get_oindex(Bus* bus)
    int BUS_get_index(Bus* bus)
    int BUS_get_dP_index(Bus* bus, int t)
    int BUS_get_dQ_index(Bus* bus, int t)
    int* BUS_get_index_v_mag_array(Bus* bus)
    int* BUS_get_index_v_ang_array(Bus* bus)
    int BUS_get_number(Bus* bus)
    int BUS_get_num_vars(void* bus, char var, int t_start, int t_end)
    REAL* BUS_get_price_array(Bus* bus)
    char* BUS_get_name(Bus* bus)
    Gen* BUS_get_gen(Bus* bus)
    Gen* BUS_get_reg_gen(Bus* bus)
    Branch* BUS_get_reg_tran(Bus* bus)
    Shunt* BUS_get_reg_shunt(Bus* bus)
    Branch* BUS_get_branch_k(Bus* bus)
    Branch* BUS_get_branch_m(Bus* bus)
    Facts* BUS_get_facts_k(Bus* bus)
    Facts* BUS_get_facts_m(Bus* bus)
    Facts* BUS_get_reg_facts(Bus* bus)
    Load* BUS_get_load(Bus* bus)
    Vargen* BUS_get_vargen(Bus* bus)
    Bat* BUS_get_bat(Bus* bus)
    Shunt* BUS_get_shunt(Bus* bus)
    ConvCSC* BUS_get_csc_conv(Bus* bus)
    ConvVSC* BUS_get_vsc_conv(Bus* bus)
    ConvVSC* BUS_get_reg_vsc_conv(Bus* bus)
    int BUS_get_degree(Bus* bus)
    REAL BUS_get_total_gen_P(Bus* bus, int t)
    REAL BUS_get_total_gen_Q(Bus* bus, int t)
    REAL BUS_get_total_gen_Q_max(Bus* bus)
    REAL BUS_get_total_gen_Q_min(Bus* bus)
    REAL BUS_get_total_reg_gen_Q(Bus* bus, int t)
    REAL BUS_get_total_reg_gen_Q_max(Bus* bus)
    REAL BUS_get_total_reg_gen_Q_min(Bus* bus)
    REAL BUS_get_total_load_P(Bus* bus, int t)
    REAL BUS_get_total_load_Q(Bus* bus, int t)
    REAL BUS_get_total_shunt_g(Bus* bus)
    REAL BUS_get_total_shunt_b(Bus* bus, int t)
    REAL BUS_get_v_base(Bus* bus)
    REAL* BUS_get_v_mag_array(Bus* bus)
    REAL* BUS_get_v_ang_array(Bus* bus)
    REAL* BUS_get_v_set_array(Bus* bus)
    REAL BUS_get_v_max_reg(Bus* bus)
    REAL BUS_get_v_min_reg(Bus* bus)
    REAL BUS_get_v_max_norm(Bus* bus)
    REAL BUS_get_v_min_norm(Bus* bus)
    REAL BUS_get_v_max_emer(Bus* bus)
    REAL BUS_get_v_min_emer(Bus* bus)
    REAL BUS_get_P_mis(Bus* bus, int t)
    REAL BUS_get_Q_mis(Bus* bus, int t)

    REAL* BUS_get_sens_P_balance_array(Bus* bus)
    REAL* BUS_get_sens_Q_balance_array(Bus* bus)
    REAL* BUS_get_sens_v_mag_u_bound_array(Bus* bus)
    REAL* BUS_get_sens_v_mag_l_bound_array(Bus* bus)
    REAL* BUS_get_sens_v_ang_u_bound_array(Bus* bus)
    REAL* BUS_get_sens_v_ang_l_bound_array(Bus* bus)
    REAL* BUS_get_sens_v_set_reg_array(Bus* bus)
    REAL* BUS_get_sens_v_reg_by_tran_array(Bus* bus)
    REAL* BUS_get_sens_v_reg_by_shunt_array(Bus* bus)

    REAL BUS_get_largest_sens(Bus* bus, int t)
    int BUS_get_largest_sens_type(Bus* bus, int t)
    REAL BUS_get_largest_mis(Bus* bus, int t)
    int BUS_get_largest_mis_type(Bus* bus, int t)
    Bus* BUS_get_next(Bus* bus)
    char* BUS_get_json_string(Bus* bus, char* output)
    char* BUS_get_var_info_string(Bus* bus, int index)
    bint BUS_is_in_service(void* bus)
    bint BUS_is_equal(Bus* bus, Bus* other)
    bint BUS_is_slack(Bus* bus)
    bint BUS_is_star(Bus* bus)
    bint BUS_is_v_set_regulated(Bus* bus, bint only_in_service)
    bint BUS_is_regulated_by_gen(Bus* bus, bint only_in_service)
    bint BUS_is_regulated_by_tran(Bus* bus, bint only_in_service)
    bint BUS_is_regulated_by_shunt(Bus* bus, bint only_in_service)
    bint BUS_is_regulated_by_vsc_conv(Bus* bus, bint only_in_service)
    bint BUS_is_regulated_by_facts(Bus* bus, bint only_in_service)
    bint BUS_has_flags(Bus* bus, char flag_type, char mask)
    Bus* BUS_new(int num_periods)
    Bus* BUS_array_new(int size, int num_periods)
    void BUS_array_del(Bus* bus_array, int size)
    void BUS_set_area(Bus* bus, int area)
    void BUS_set_zone(Bus* bus, int zone)
    void BUS_set_slack_flag(Bus* bus, bint slack)
    void BUS_set_star_flag(Bus* bus, bint star)
    void BUS_set_next(Bus* bus, Bus* next_bus)
    void BUS_set_number(Bus* bus, REAL num)
    void BUS_set_name(Bus* bus, char* name)
    void BUS_set_v_base(Bus* bus, REAL v_base)
    void BUS_set_v_max_reg(Bus* bus, REAL v_max_reg)
    void BUS_set_v_min_reg(Bus* bus, REAL v_min_reg)
    void BUS_set_v_max_norm(Bus* bus, REAL v_max_norm)
    void BUS_set_v_min_norm(Bus* bus, REAL v_min_norm)
    void BUS_set_v_max_emer(Bus* bus, REAL v_max_emer)
    void BUS_set_v_min_emer(Bus* bus, REAL v_min_emer)
    void BUS_set_in_service(Bus* bus, bint in_service)
    void BUS_set_dP_index(Bus* bus, int idx, int t)
    void BUS_set_dQ_index(Bus* bus, int idx, int t)

    void BUS_add_gen(Bus* bus, Gen* gen)
    void BUS_del_gen(Bus* bus, Gen* gen)
    void BUS_add_load(Bus* bus, Load* load)
    void BUS_del_load(Bus* bus, Load* load)
    void BUS_add_reg_gen(Bus* bus, Gen* reg_gen)
    void BUS_del_reg_gen(Bus* bus, Gen* reg_gen)
    void BUS_add_reg_tran(Bus* bus, Branch* reg_tran)
    void BUS_del_reg_tran(Bus* bus, Branch* reg_tran)  
    void BUS_add_reg_shunt(Bus* bus, Shunt* reg_shunt)
    void BUS_del_reg_shunt(Bus* bus, Shunt* reg_shunt)
    void BUS_add_shunt(Bus* bus, Shunt* shunt)
    void BUS_del_shunt(Bus* bus, Shunt* shunt)
    void BUS_add_vargen(Bus* bus, Vargen* gen)
    void BUS_del_vargen(Bus* bus, Vargen* gen)
    void BUS_add_bat(Bus* bus, Bat* bat)
    void BUS_del_bat(Bus* bus, Bat* bat)
    void BUS_add_branch_k(Bus* bus, Branch* branch)
    void BUS_del_branch_k(Bus* bus, Branch* branch)
    void BUS_add_branch_m(Bus* bus, Branch* branch)
    void BUS_del_branch_m(Bus* bus, Branch* branch)
    void BUS_add_reg_vsc_conv(Bus* bus, ConvVSC* conv)
    void BUS_del_reg_vsc_conv(Bus* bus, ConvVSC* conv)
    void BUS_del_all_connections(Bus* bus)

    void BUS_show(Bus* bus, int t)
