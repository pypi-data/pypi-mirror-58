#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2015, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

import os
import unittest
import numpy as np
import pfnet as pf
from . import test_cases

class TestHeuristics(unittest.TestCase):

    def test_PVPQ_switching_robustness(self):
        
        T = 2
        
        for case in test_cases.CASES:
            
            net = pf.Parser(case).parse(case, T)

            net.set_flags('bus', 'variable', 'any', 'voltage magnitude')
            
            c1 = pf.Constraint('AC power balance', net)
            c2 = pf.Constraint('PVPQ switching', net)
            c1.analyze()
            c2.analyze()
            
            h = pf.Heuristic('PVPQ switching', net)
            self.assertRaises(pf.HeuristicError, h.apply, [c1, c2], np.zeros(0))
            
            h.apply([c1, c2], np.zeros(net.num_vars))
            
            p = pf.Problem(net)
            p.add_heuristic(h)
            p.add_constraint(c1)
            p.add_constraint(c2)
            p.analyze()
            p.apply_heuristics(p.x)
        
    def test_PVPQ_switching(self):

        T = 2
        
        for case in test_cases.CASES:
            
            net = pf.Parser(case).parse(case, T)
            self.assertEqual(net.num_periods, T)

            for gen in net.generators:
                if gen.is_regulator():
                    gen.Q[:] = gen.Q_max + 1.

            # Variables
            net.set_flags('bus',
                          'variable',
                          'not slack',
                          ['voltage magnitude','voltage angle'])
            net.set_flags('generator',
                          'variable',
                          'slack',
                          'active power')
            net.set_flags('generator',
                          'variable',
                          'regulator',
                          'reactive power')
            net.set_flags('branch',
                          'variable',
                          'tap changer - v',
                          'tap ratio')
            net.set_flags('branch',
                          'variable',
                          'phase shifter',
                          'phase shift')
            net.set_flags('shunt',
                          'variable',
                          'switching - v',
                          'susceptance')
            
            self.assertEqual(net.num_vars,
                             (2*(net.num_buses-net.get_num_slack_buses()) +
                              net.get_num_slack_gens() +
                              net.get_num_reg_gens() +
                              net.get_num_tap_changers_v() + 
                              net.get_num_phase_shifters() +
                              net.get_num_switched_v_shunts())*T)
                             
            # Fixed
            net.set_flags('branch',
                          'fixed',
                          'tap changer - v',
                          'tap ratio')
            net.set_flags('branch',
                          'fixed',
                          'phase shifter',
                          'phase shift')
            net.set_flags('shunt',
                          'fixed',
                          'switching - v',
                          'susceptance')
            self.assertEqual(net.num_fixed,
                             (net.get_num_tap_changers_v() +
                              net.get_num_phase_shifters() +
                              net.get_num_switched_v_shunts())*T)
                             

            self.assertRaises(pf.HeuristicError, pf.Heuristic, 'foo', net)

            heur = pf.Heuristic('PVPQ switching', net)

            self.assertEqual(heur.name, 'PVPQ switching')

            self.assertTrue(heur.network.has_same_ptr(net))

            x = net.get_var_values()

            acpf = pf.Constraint('AC power balance', net)
            pvpq = pf.Constraint('PVPQ switching', net)
            fix = pf.Constraint('variable fixing', net)
            
            self.assertRaises(pf.HeuristicError, heur.apply, [], x)
            self.assertRaises(pf.HeuristicError, heur.apply, [fix], x)
            self.assertRaises(pf.HeuristicError, heur.apply, [fix, acpf], x)
            self.assertRaises(pf.HeuristicError, heur.apply, [fix, pvpq], x)
            self.assertRaises(pf.HeuristicError, heur.apply, [acpf, pvpq], x)
            self.assertRaises(pf.HeuristicError, heur.apply, [acpf, fix, pvpq], x)

            for c in [acpf, pvpq, fix]:
                c.analyze()

            A = pvpq.A.copy()

            self.assertRaises(pf.HeuristicError, heur.apply, [], x)
            self.assertRaises(pf.HeuristicError, heur.apply, [fix], x)
            self.assertRaises(pf.HeuristicError, heur.apply, [fix, acpf], x)
            self.assertRaises(pf.HeuristicError, heur.apply, [fix, pvpq], x)
            heur.apply([acpf, pvpq], x)
            self.assertEqual(acpf.f.size, 2*net.num_buses*T)
            self.assertEqual(pvpq.A.shape[1], net.num_vars)
            heur.apply([acpf, fix, pvpq], x)
            self.assertEqual(acpf.f.size, 2*net.num_buses*T)
            self.assertEqual(pvpq.A.shape[1], net.num_vars)

            self.assertFalse(np.all(A.data == pvpq.A.data))

            for gen in net.generators:
                gen.in_service = False

            for c in [acpf, pvpq, fix]:
                c.analyze()

            A = pvpq.A.copy()

            heur.apply([acpf, fix, pvpq], x)
            self.assertEqual(acpf.f.size, 2*net.num_buses*T)
            self.assertEqual(pvpq.A.shape[1], net.num_vars)

            self.assertTrue(np.all(A.data == pvpq.A.data))
            
            net.make_all_in_service()

            for bus in net.buses:
                bus.in_service = False

            for c in [acpf, pvpq, fix]:
                c.analyze()

            A = pvpq.A.copy()

            heur.apply([acpf, fix, pvpq], x)

            self.assertTrue(np.all(A.data == pvpq.A.data))
            
