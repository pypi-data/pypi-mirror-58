#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2019, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

cimport cvec
cimport cmat
cimport cbus
cimport cbranch
cimport cgen
cimport cload
cimport cshunt
cimport cvargen
cimport cbat
cimport cbus_dc
cimport cbranch_dc
cimport cconv_vsc
cimport cconv_csc
cimport cfacts

cdef extern from "pfnet/net.h":

    ctypedef struct Net
    ctypedef struct Bus
    ctypedef struct Gen
    ctypedef struct Load
    ctypedef struct Shunt
    ctypedef struct Branch
    ctypedef struct Bat
    ctypedef struct Vargen
    ctypedef struct BusDC
    ctypedef struct BranchDC
    ctypedef struct ConvVSC
    ctypedef struct ConvCSC
    ctypedef struct Facts
    ctypedef double REAL

    void NET_add_buses(Net* net, cbus.Bus** br_ptr_array, int size)
    void NET_del_buses(Net* net, cbus.Bus** br_ptr_array, int size)

    void NET_add_branches(Net* net, cbranch.Branch** br_ptr_array, int size)
    void NET_del_branches(Net* net, cbranch.Branch** br_ptr_array, int size)

    void NET_add_gens(Net* net, cgen.Gen** gen_ptr_array, int size)
    void NET_del_gens(Net* net, cgen.Gen** gen_ptr_array, int size)

    void NET_add_loads(Net* net, cload.Load** load_ptr_array, int size)
    void NET_del_loads(Net* net, cload.Load** load_ptr_array, int size)

    void NET_add_shunts(Net* net, cshunt.Shunt** shunt_ptr_array, int size)
    void NET_del_shunts(Net* net, cshunt.Shunt** shunt_ptr_array, int size)

    void NET_add_bats(Net* net, cbat.Bat** bat_ptr_array, int size)
    void NET_del_bats(Net* net, cbat.Bat** bat_ptr_array, int size)

    void NET_add_vargens(Net* net, cvargen.Vargen** vargen_ptr_array, int size)
    void NET_del_vargens(Net* net, cvargen.Vargen** vargen_ptr_array, int size)

    void NET_add_vargens_from_params(Net* net, cbus.Bus* bus_list, REAL power_capacity, REAL power_base, REAL power_std, REAL corr_radius, REAL corr_value)
    void NET_add_batteries_from_params(Net* net, cbus.Bus* bus_list, REAL power_capacity,  REAL energy_capacity, REAL eta_c, REAL eta_d)        
    cbus.Bus* NET_bus_hash_number_find(Net* net, int number)
    cbus.Bus* NET_bus_hash_name_find(Net* net, char* name)
    cbus_dc.BusDC* NET_dc_bus_hash_number_find(Net* net, int number)
    cbus_dc.BusDC* NET_dc_bus_hash_name_find(Net* net, char* name)
    void NET_bus_hash_number_add(Net* net, cbus.Bus* bus)
    void NET_bus_hash_name_add(Net* net, cbus.Bus* bus)
    void NET_clear_error(Net* net)
    void NET_clear_flags(Net* net)
    void NET_clear_properties(Net* net)
    void NET_clear_sensitivities(Net* net)
    void NET_clear_outages(Net* net)
    cmat.Mat* NET_create_vargen_P_sigma(Net* net, int spread, REAL corr)
    void NET_copy_from_net(Net* net, Net* other_net, int* bus_index_map, int* branch_index_map, int mode)
    void NET_del(Net* net)
    Net* NET_extract_subnet(Net* net, Bus** bus_ptr_array, int size)
    Net* NET_get_copy(Net* net, bint merge_buses)
    REAL NET_get_base_power(Net* net)
    char* NET_get_error_string(Net* net)

    cbus.Bus* NET_get_bus(Net* net, int index)
    cbranch.Branch* NET_get_branch(Net* net, int index)
    cgen.Gen* NET_get_gen(Net* net, int index)
    cshunt.Shunt* NET_get_shunt(Net* net, int index)
    cload.Load* NET_get_load(Net* net, int index)
    cvargen.Vargen* NET_get_vargen(Net* net, int index)
    cbat.Bat* NET_get_bat(Net* net, int index)
    cbus_dc.BusDC* NET_get_dc_bus(Net* net, int index)
    cbranch_dc.BranchDC* NET_get_dc_branch(Net* net, int index)
    cconv_csc.ConvCSC* NET_get_csc_conv(Net* net, int index)
    cconv_vsc.ConvVSC* NET_get_vsc_conv(Net* net, int index)
    cfacts.Facts* NET_get_facts(Net* net, int index)
    cbus.Bus* NET_get_load_buses(Net* net)
    cbus.Bus* NET_get_gen_buses(Net* net)

    cgen.Gen* NET_get_gen_from_name_and_bus_number(Net* net, char* name, int number)
    cbranch.Branch* NET_get_branch_from_name_and_bus_numbers(Net* net, char* name, int number1, int number2)
    cshunt.Shunt* NET_get_shunt_from_name_and_bus_number(Net* net, char* name, int number)
    cshunt.Shunt* NET_get_fixed_shunt_from_name_and_bus_number(Net* net, char* name, int number)
    cshunt.Shunt* NET_get_switched_shunt_from_name_and_bus_number(Net* net, char* name, int number)
    cload.Load* NET_get_load_from_name_and_bus_number(Net* net, char* name, int number)
    cvargen.Vargen* NET_get_vargen_from_name_and_bus_number(Net* net, char* name, int number)
    cbat.Bat* NET_get_bat_from_name_and_bus_number(Net* net, char* name, int number)
    cbranch_dc.BranchDC* NET_get_dc_branch_from_name_and_dc_bus_names(Net* net, char* name, char* bus1_name, char* bus2_name)
    cconv_csc.ConvCSC* NET_get_csc_conv_from_name_and_ac_bus_number(Net* net, char* name, int number)
    cconv_csc.ConvCSC* NET_get_csc_conv_from_name_and_dc_bus_name(Net* net, char* name, char* bus_name)
    cconv_vsc.ConvVSC* NET_get_vsc_conv_from_name_and_ac_bus_number(Net* net, char* name, int number)
    cconv_vsc.ConvVSC* NET_get_vsc_conv_from_name_and_dc_bus_name(Net* net, char* name, char* bus_name)
    cfacts.Facts* NET_get_facts_from_name_and_bus_numbers(Net* net, char* name, int number1, int number2)

    unsigned long int NET_get_state_tag(Net* net)
    REAL NET_get_total_load_P(Net* net, int t)
    int NET_get_num_periods(Net* net)
    int NET_get_num_buses(Net* net, bint only_in_service)
    int NET_get_num_buses_out_of_service(Net* net)
    int NET_get_num_slack_buses(Net* net, bint only_in_service)
    int NET_get_num_star_buses(Net* net, bint only_in_service)
    int NET_get_num_red_buses(Net* net)
    int NET_get_num_buses_reg_by_gen(Net* net, bint only_in_service)
    int NET_get_num_buses_reg_by_tran(Net* net, bint only_in_service)
    int NET_get_num_buses_reg_by_tran_only(Net* net, bint only_in_service)
    int NET_get_num_buses_reg_by_shunt(Net* net, bint only_in_service)
    int NET_get_num_buses_reg_by_shunt_only(Net* net, bint only_in_service)
    int NET_get_num_buses_reg_by_vsc_conv(Net* net, bint only_in_service)
    int NET_get_num_buses_reg_by_facts(Net* net, bint only_in_service)
    int NET_get_num_branches(Net* net, bint only_in_service)
    int NET_get_num_branches_out_of_service(Net* net)
    int NET_get_num_fixed_trans(Net* net, bint only_in_service)
    int NET_get_num_lines(Net* net, bint only_in_service)
    int NET_get_num_zero_impedance_lines(Net* net, bint only_in_service)
    int NET_get_num_phase_shifters(Net* net, bint only_in_service)
    int NET_get_num_tap_changers(Net* net, bint only_in_service)
    int NET_get_num_tap_changers_v(Net* net, bint only_in_service)
    int NET_get_num_tap_changers_Q(Net* net, bint only_in_service)
    int NET_get_num_gens(Net* net, bint only_in_service)
    int NET_get_num_gens_out_of_service(Net* net)
    int NET_get_num_reg_gens(Net* net, bint only_in_service)
    int NET_get_num_slack_gens(Net* net, bint only_in_service)
    int NET_get_num_P_adjust_gens(Net* net, bint only_in_service)
    int NET_get_num_loads(Net* net, bint only_in_service)
    int NET_get_num_loads_out_of_service(Net* net)
    int NET_get_num_P_adjust_loads(Net* net, bint only_in_service)
    int NET_get_num_vdep_loads(Net* net, bint only_in_service)
    int NET_get_num_shunts(Net* net, bint only_in_service)
    int NET_get_num_shunts_out_of_service(Net* net)
    int NET_get_num_fixed_shunts(Net* net, bint only_in_service)
    int NET_get_num_switched_shunts(Net* net, bint only_in_service)
    int NET_get_num_switched_v_shunts(Net* net, bint only_in_service)
    int NET_get_num_vargens(Net* net, bint only_in_service)
    int NET_get_num_vargens_out_of_service(Net* net)
    int NET_get_num_bats(Net* net, bint only_in_service)
    int NET_get_num_bats_out_of_service(Net* net)
    int NET_get_num_dc_buses(Net* net, bint only_in_service)
    int NET_get_num_dc_buses_out_of_service(Net* net)
    int NET_get_num_dc_branches(Net* net, bint only_in_service)
    int NET_get_num_dc_branches_out_of_service(Net* net)
    int NET_get_num_csc_convs(Net* net, bint only_in_service)
    int NET_get_num_csc_convs_out_of_service(Net* net)
    int NET_get_num_vsc_convs(Net* net, bint only_in_service)
    int NET_get_num_vsc_convs_out_of_service(Net* net)
    int NET_get_num_vsc_convs_in_v_dc_mode(Net* net, bint only_in_service)
    int NET_get_num_vsc_convs_in_P_dc_mode(Net* net, bint only_in_service)
    int NET_get_num_vsc_convs_in_v_ac_mode(Net* net, bint only_in_service)
    int NET_get_num_vsc_convs_in_f_ac_mode(Net* net, bint only_in_service)
    int NET_get_num_facts(Net* net, bint only_in_service)
    int NET_get_num_facts_out_of_service(Net* net)
    int NET_get_num_facts_in_normal_series_mode(Net* net, bint only_in_service)
    int NET_get_num_reg_facts(Net* net, bint only_in_service)
    int NET_get_num_vars(Net* net)
    int NET_get_num_fixed(Net* net)
    int NET_get_num_bounded(Net* net)
    int NET_get_num_sparse(Net* net)
    REAL NET_get_bus_v_max(Net* net, int t)
    REAL NET_get_bus_v_min(Net* net, int t)
    REAL NET_get_bus_v_vio(Net* net, int t)
    REAL NET_get_bus_P_mis(Net* net, int t)
    REAL NET_get_bus_Q_mis(Net* net, int t)
    REAL NET_get_gen_P_cost(Net* net, int t)
    REAL NET_get_gen_v_dev(Net* net, int t)
    REAL NET_get_gen_Q_vio(Net* net, int t)
    REAL NET_get_gen_P_vio(Net* net, int t)
    REAL NET_get_tran_v_vio(Net* net, int t)
    REAL NET_get_tran_r_vio(Net* net, int t)
    REAL NET_get_tran_p_vio(Net* net, int t)
    REAL NET_get_shunt_v_vio(Net* net, int t)
    REAL NET_get_shunt_b_vio(Net* net, int t)
    REAL NET_get_load_P_util(Net* net, int t)
    REAL NET_get_load_P_vio(Net* net, int t)
    REAL NET_get_vargen_corr_radius(Net* net)
    REAL NET_get_vargen_corr_value(Net* net)
    cvec.Vec* NET_get_var_values(Net* net, int code)
    char* NET_get_var_info_string(Net* net, int index)
    cmat.Mat* NET_get_var_projection(Net* net, char obj_type, char prop_mask, char var, int t_start, int t_end)
    char* NET_get_json_string(Net* net)
    bint NET_has_error(Net* net)
    void NET_make_all_in_service(Net* net)
    Net* NET_new(int num_periods)
    int NET_round_discrete_switched_shunts_b(Net* net, int t)
    void NET_clip_switched_shunts_b(Net* net, int t)
    void NET_set_base_power(Net* net, REAL base_power)
    void NET_set_flags(Net* net, char obj_type, char flag_mask, char prop_mask, char val_mask)
    void NET_set_flags_of_component(Net* net, void* obj, char obj_type, char flag_mask, char val_mask)
    void NET_set_var_values(Net* net, cvec.Vec* values)
    void NET_show_components(Net* net, int output_level)
    char* NET_get_show_components_str(Net* net, int output_level)
    void NET_show_properties(Net* net, int t)
    void NET_show_equiv_buses(Net* net)
    void NET_show_red_buses(Net* net)
    char* NET_get_show_properties_str(Net* net, int t)
    void NET_update_properties(Net* net, cvec.Vec* values)
    void NET_propagate_data_in_time(Net* net, int start, int end)
    void NET_update_reg_Q_participations(Net* net, int t)
    void NET_update_set_points(Net* net)
    void NET_update_hash_tables(Net* net)
    void NET_localize_gen_regulation(Net* net, int max_dist)

    void NET_set_bus_array(Net* net, cbus.Bus* bus_list, int num_buses)
    void NET_set_branch_array(Net* net, cbranch.Branch* branch_list, int num_branches)
    void NET_set_gen_array(Net* net, cgen.Gen* gen_list, int num_generators)
    void NET_set_load_array(Net* net, cload.Load* load_list, int num_loads)
    void NET_set_shunt_array(Net* net, cshunt.Shunt* shunt_list, int num_shunts)
    void NET_set_vargen_array(Net* net, cvargen.Vargen* vargen_list, int num_vargens)
    void NET_set_bat_array(Net* net, cbat.Bat* bat_list, int num_batteries)
    void NET_set_vsc_conv_array(Net* net, cconv_vsc.ConvVSC* conv, int num)
    void NET_set_csc_conv_array(Net* net, cconv_csc.ConvCSC* conv, int num)
    void NET_set_dc_bus_array(Net* net, cbus_dc.BusDC* bus, int num)
    void NET_set_dc_branch_array(Net* net, cbranch_dc.BranchDC* branch, int num)
    void NET_set_facts_array(Net* net, cfacts.Facts* facts, int num)
