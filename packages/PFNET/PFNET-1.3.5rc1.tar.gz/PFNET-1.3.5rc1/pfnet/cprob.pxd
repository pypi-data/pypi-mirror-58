#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2019, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

cdef extern from "pfnet/problem.h":

    ctypedef struct Prob
    ctypedef struct Constr
    ctypedef struct Func
    ctypedef struct Net
    ctypedef struct Vec
    ctypedef struct Mat
    ctypedef struct Heur
    ctypedef double REAL
        
    void PROB_add_constr(Prob* p, Constr* c)
    void PROB_add_func(Prob* p, Func* f)
    void PROB_add_heur(Prob* p, Heur* h)
    void PROB_analyze(Prob* p)
    void PROB_apply_heuristics(Prob* p, Vec* point)
    void PROB_eval(Prob* p, Vec* point)
    void PROB_store_sens(Prob* p, Vec* sA, Vec* sf, Vec* sGu, Vec* sGl)
    void PROB_del(Prob* p)
    void PROB_clear(Prob* p)
    void PROB_clear_error(Prob* p)
    void PROB_combine_H(Prob* p, Vec* coeff, bint ensure_psd)
    Constr* PROB_find_constr(Prob* p, char* name)
    Constr* PROB_get_constr(Prob* p)
    char* PROB_get_error_string(Prob* p)
    Func* PROB_get_func(Prob* p)
    Heur* PROB_get_heur(Prob* p)
    Vec* PROB_get_init_point(Prob* p)
    Vec* PROB_get_upper_limits(Prob* p)
    Vec* PROB_get_lower_limits(Prob* p)
    Net* PROB_get_network(Prob* p)
    REAL PROB_get_phi(Prob* p)
    Vec* PROB_get_gphi(Prob* p)
    Mat* PROB_get_Hphi(Prob* p)
    Vec* PROB_get_b(Prob* p)
    Mat* PROB_get_A(Prob* p)
    Vec* PROB_get_l(Prob* p)
    Vec* PROB_get_u(Prob* p)
    Mat* PROB_get_G(Prob* p)
    Vec* PROB_get_f(Prob* p)
    Mat* PROB_get_J(Prob* p)
    Mat* PROB_get_H_combined(Prob* p)
    bint PROB_has_error(Prob* p)
    Prob* PROB_new(Net* net)
    void PROB_show(Prob* p)
    char* PROB_get_show_str(Prob* p)
    void PROB_update_lin(Prob* p)
    int PROB_get_num_primal_variables(Prob* p)
    int PROB_get_num_linear_equality_constraints(Prob* p)
    int PROB_get_num_linear_inequality_constraints(Prob* p)
    int PROB_get_num_nonlinear_equality_constraints(Prob* p)
    int PROB_get_num_extra_vars(Prob* p)
