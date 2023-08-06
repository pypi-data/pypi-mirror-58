#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2015, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

import json
import pickle
import unittest
import pfnet as pf
import numpy as np
import multiprocessing
from . import test_cases
from scipy.sparse import coo_matrix, bmat, triu

TEST_BRANCHES = 100
TEST_GENS = 100
TEST_BUSES = 20

class ContingencyHandler:

    def __call__(self, c):
        return c.num_generator_outages == 1 and c.num_branch_outages == 0 and 'gen' in c.name

class TestContingency(unittest.TestCase):

    def setUp(self):

        pass

    def test_parallel_pool_map(self):

        for case in test_cases.CASES:

            net = pf.Parser(case).parse(case)
            self.assertEqual(net.num_periods,1)

            if net.num_branches > 1 and net.num_generators > 1:

                contingencies = []
                for gen in net.generators[:5]:
                    c = pf.Contingency(generators=[gen])
                    c.name = 'gen %d' %gen.index
                    self.assertEqual(c.name, 'gen %d' %gen.index)
                    indices = c.generator_outages
                    self.assertEqual(indices.size,1)
                    self.assertEqual(indices[0], gen.index)
                    self.assertEqual(c.branch_outages.size,0)
                    contingencies.append(c)
                        
                pool = multiprocessing.Pool()
                results = pool.map(ContingencyHandler(),contingencies)
                self.assertEqual(results,[True]*min([5,net.num_generators]))

    def test_pickle(self):

        for case in test_cases.CASES:

            net = pf.Parser(case).parse(case)
            self.assertEqual(net.num_periods,1)

            cont1 = pf.Contingency()

            self.assertEqual(cont1.name, "")
            cont1.name = 'foo'
            self.assertEqual(cont1.name, 'foo')

            if net.num_branches > 1 and net.num_generators > 1:
                cont1.add_branch_outage(net.get_branch(net.num_branches-1))
                cont1.add_branch_outage(net.get_branch(net.num_branches-2))
                cont1.add_generator_outage(net.get_generator(0))
                cont1.add_generator_outage(net.get_generator(1))
                ibr = cont1.branch_outages
                igen = cont1.generator_outages
                self.assertEqual(ibr.size, cont1.num_branch_outages)
                self.assertEqual(ibr.size, 2)
                self.assertEqual(igen.size, cont1.num_generator_outages)
                self.assertEqual(igen.size, 2)
                self.assertTrue(net.get_generator(0).index in igen)
                self.assertTrue(net.get_generator(1).index in igen)
                self.assertTrue(net.get_branch(net.num_branches-1).index in ibr)
                self.assertTrue(net.get_branch(net.num_branches-2).index in ibr)

                pkld_cont = pickle.dumps(cont1,protocol=-1)
                cont2 = pickle.loads(pkld_cont)

                self.assertEqual(cont2.name, 'foo')

                self.assertEqual(cont1.num_generator_outages,cont2.num_generator_outages)
                self.assertEqual(cont1.num_branch_outages,cont2.num_branch_outages)
                iibr = cont2.branch_outages
                iigen = cont2.generator_outages
                self.assertEqual(iibr.size, cont2.num_branch_outages)
                self.assertEqual(iibr.size, 2)
                self.assertEqual(iigen.size, cont2.num_generator_outages)
                self.assertEqual(iigen.size, 2)
                self.assertTrue(net.get_generator(0).index in iigen)
                self.assertTrue(net.get_generator(1).index in iigen)
                self.assertTrue(net.get_branch(net.num_branches-1).index in iibr)
                self.assertTrue(net.get_branch(net.num_branches-2).index in iibr)
                
                for branch in net.branches:
                    if cont1.has_branch_outage(branch):
                        self.assertTrue(cont2.has_branch_outage(branch))
                    else:
                        self.assertFalse(cont2.has_branch_outage(branch))
                for gen in net.generators:
                    if cont1.has_generator_outage(gen):
                        self.assertTrue(cont2.has_generator_outage(gen))
                    else:
                        self.assertFalse(cont2.has_generator_outage(gen))
                self.assertEqual(cont1.json_string,cont2.json_string)
                
    def test_json_string(self):

        for case in test_cases.CASES:

            net = pf.Parser(case).parse(case)
            self.assertEqual(net.num_periods,1)

            cont = pf.Contingency()
            s = json.loads(cont.json_string)

            self.assertTrue('generator_outages' in s)
            self.assertTrue('branch_outages' in s)
            self.assertTrue('name' in s)

            self.assertEqual(s['name'],'')
            self.assertEqual(s['generator_outages'],[])
            self.assertEqual(s['branch_outages'],[])

            if net.num_branches > 1 and net.num_generators > 1:
                cont.add_branch_outage(net.get_branch(net.num_branches-1))
                cont.add_branch_outage(net.get_branch(net.num_branches-2))
                cont.add_generator_outage(net.get_generator(0))
                cont.add_generator_outage(net.get_generator(1))
                cont.name = 'bar'
                s = json.loads(cont.json_string)
                self.assertEqual(s['generator_outages'],[0,1])
                self.assertEqual(s['branch_outages'],[net.num_branches-1,net.num_branches-2])
                self.assertEqual(s['name'], 'bar')

    def test_construction(self):

        for case in test_cases.CASES:

            net = pf.Parser(case).parse(case)
            self.assertEqual(net.num_periods,1)

            # outage init
            for gen in net.generators:
                self.assertTrue(gen.is_in_service())
                self.assertTrue(gen.in_service)
            for branch in net.branches:
                self.assertTrue(branch.is_in_service())
                self.assertTrue(branch.in_service)

            self.assertEqual(net.get_num_generators_out_of_service(),0)
            self.assertEqual(net.get_num_branches_out_of_service(),0)

            # outage set
            gen = net.get_generator(0)
            branch = net.get_branch(0)
            gen.in_service = False
            branch.in_service = False

            self.assertEqual(net.get_num_generators_out_of_service(),1)
            self.assertEqual(net.get_num_branches_out_of_service(),1)

            net.make_all_in_service()

            self.assertEqual(net.get_num_generators_out_of_service(),0)
            self.assertEqual(net.get_num_branches_out_of_service(),0)

            # outages at construction
            c0 = pf.Contingency([net.get_generator(0)],
                                [net.get_branch(1)])
            self.assertTrue(c0.has_generator_outage(net.get_generator(0)))
            self.assertTrue(c0.has_branch_outage(net.get_branch(1)))
            self.assertEqual(c0.generator_outages.size,1)
            self.assertEqual(c0.generator_outages[0], net.get_generator(0).index)
            self.assertEqual(c0.branch_outages.size,1)
            self.assertEqual(c0.branch_outages[0], net.get_branch(1).index)
            c1 = pf.Contingency(generators=[net.get_generator(0)],
                                branches=[net.get_branch(2)])
            self.assertTrue(c1.has_generator_outage(net.get_generator(0)))
            self.assertTrue(c1.has_branch_outage(net.get_branch(2)))

            # list of all outages
            self.assertEqual(c1.outages, [('branch', 2), ('generator', 0)])

            # contingency
            g0 = net.get_generator(0)
            bus0 = g0.bus
            reg_bus0 = g0.reg_bus
            br7 = net.get_branch(0)
            br3 = net.get_branch(1)
            bus_k7 = br7.bus_k
            bus_k3 = br3.bus_k
            bus_m7 = br7.bus_m
            bus_m3 = br3.bus_m
            bus_k7_degree = br7.bus_k.degree
            bus_m7_degree = br7.bus_m.degree
            bus_k3_degree = br3.bus_k.degree
            bus_m3_degree = br3.bus_m.degree
            if net.num_generators > 5:
                g5 = net.get_generator(5)
                bus5 = g5.bus
                reg_bus5 = g5.reg_bus
            cont = pf.Contingency()
            self.assertEqual(cont.num_generator_outages,0)
            self.assertEqual(cont.num_branch_outages,0)
            cont.add_generator_outage(g0)
            cont.add_branch_outage(br7)
            self.assertEqual(cont.num_generator_outages,1)
            self.assertEqual(cont.num_branch_outages,1)
            cont.add_generator_outage(g0)
            cont.add_branch_outage(br7)
            self.assertEqual(cont.num_generator_outages,1)
            self.assertEqual(cont.num_branch_outages,1)
            if net.num_generators > 5:
                cont.add_generator_outage(g5)
                self.assertEqual(cont.num_generator_outages,2)
                self.assertTrue(cont.has_generator_outage(g5))
            self.assertTrue(cont.has_generator_outage(g0))
            cont.add_branch_outage(br3)
            self.assertEqual(cont.num_branch_outages,2)
            self.assertTrue(cont.has_branch_outage(br3))
            self.assertTrue(cont.has_branch_outage(br7))

            # apply
            self.assertEqual(len([g for g in net.generators if g.in_service]),net.num_generators)
            self.assertEqual(len([b for b in net.branches if b.in_service]),net.num_branches)
            self.assertEqual(len([g for g in net.generators if not g.in_service]),0)
            self.assertEqual(len([b for b in net.branches if not b.in_service]),0)
            cont.apply(net)
            if net.num_generators > 5:
                self.assertEqual(net.get_num_generators(only_in_service=True),net.num_generators-2)
                self.assertEqual(len([g for g in net.generators if not g.in_service]),2)
            else:
                self.assertEqual(net.get_num_generators(only_in_service=True),net.num_generators-1)
                self.assertEqual(len([g for g in net.generators if not g.in_service]),1)
            self.assertEqual(len([b for b in net.branches if not b.in_service]),2)
            self.assertEqual(net.get_num_branches(only_in_service=True),net.num_branches-2)
            for g in net.generators:
                if g.index == 0 or g.index == 5:
                    self.assertFalse(g.is_in_service())
                    self.assertFalse(g.in_service)
                    if g.Q_max > g.Q_min:
                        self.assertTrue(g.is_regulator())
                    g.bus
                    g.reg_bus
                    if g.index == 0:
                        self.assertTrue(g.index in [y.index for y in bus0.generators])
                        if reg_bus0 is not None:
                            self.assertTrue(g.index in [y.index for y in reg_bus0.reg_generators])
                    elif g.index == 5:
                        self.assertTrue(g.index in [y.index for y in bus5.generators])
                        if reg_bus5 is not None:
                            self.assertTrue(g.index in [y.index for y in reg_bus5.reg_generators])
                else:
                    self.assertTrue(g.is_in_service())
                    self.assertTrue(g.in_service)
            if bus_k7 == bus_k3 or bus_k7 == bus_m3:
                self.assertEqual(bus_k7_degree,bus_k7.degree)
            else:
                self.assertEqual(bus_k7_degree,bus_k7.degree)
            if bus_m7 == bus_k3 or bus_m7 == bus_m3:
                self.assertEqual(bus_m7_degree,bus_m7.degree)
            else:
                self.assertEqual(bus_m7_degree,bus_m7.degree)
            if bus_k3 == bus_k7 or bus_k3 == bus_m7:
                self.assertEqual(bus_k3_degree,bus_k3.degree)
            else:
                self.assertEqual(bus_k3_degree,bus_k3.degree)
            if bus_m3 == bus_k7 or bus_m3 == bus_m7:
                self.assertEqual(bus_m3_degree,bus_m3.degree)
            else:
                self.assertEqual(bus_m3_degree,bus_m3.degree)
            for b in net.branches:
                if b.index == 0 or b.index == 1:
                    self.assertFalse(b.is_in_service())
                    self.assertFalse(b.in_service)
                    b.bus_k
                    b.bus_m
                    if b.index == 0:
                        self.assertTrue(b.index in [y.index for y in bus_k7.branches_k])
                        self.assertTrue(b.index in [y.index for y in bus_k7.branches])
                        self.assertFalse(b.index in [y.index for y in bus_k7.branches_m])
                        self.assertFalse(b.index in [y.index for y in bus_m7.branches_k])
                        self.assertTrue(b.index in [y.index for y in bus_m7.branches])
                        self.assertTrue(b.index in [y.index for y in bus_m7.branches_m])
                    elif b.index == 1:
                        self.assertTrue(b.index in [y.index for y in bus_k3.branches_k])
                        self.assertTrue(b.index in [y.index for y in bus_k3.branches])
                        self.assertFalse(b.index in [y.index for y in bus_k3.branches_m])
                        self.assertFalse(b.index in [y.index for y in bus_m3.branches_k])
                        self.assertTrue(b.index in [y.index for y in bus_m3.branches])
                        self.assertTrue(b.index in [y.index for y in bus_m3.branches_m])
                else:
                    self.assertTrue(b.is_in_service())
                    self.assertTrue(b.in_service)
            cont2 = pf.Contingency()
            cont2.add_branch_outage(net.get_branch(2))
            self.assertTrue(net.get_branch(2).in_service)
            cont2.apply(net)
            self.assertFalse(net.get_branch(2).in_service)
            self.assertFalse(net.get_branch(0).in_service)
            self.assertFalse(net.get_branch(1).in_service)
            self.assertFalse(net.get_generator(0).in_service)
            if net.num_generators > 5:
                self.assertFalse(net.get_generator(5).in_service)
            self.assertEqual(cont2.num_branch_outages,1)
            self.assertEqual(cont2.num_generator_outages,0)

            # clear
            cont.clear(net)
            self.assertFalse(net.get_branch(2).in_service)
            self.assertTrue(net.get_branch(1).in_service)
            self.assertTrue(net.get_branch(0).in_service)
            self.assertTrue(net.get_generator(0).in_service)
            if net.num_generators > 5:
                self.assertTrue(net.get_generator(5).in_service)
            self.assertEqual(len([b for b in net.branches if not b.in_service]),1)
            cont2.clear(net)
            self.assertEqual(len([b for b in net.branches if not b.in_service]),0)
            for g in net.generators:
                if g.index == 0 or g.index == 5:
                    self.assertTrue(g.is_in_service())
                    self.assertTrue(g.in_service)
                    if g.index == 0:
                        self.assertEqual(g.bus.index,bus0.index)
                        self.assertTrue(g.index in [y.index for y in bus0.generators])
                        if reg_bus0 is not None:
                            self.assertEqual(g.reg_bus.index,reg_bus0.index)
                            self.assertTrue(g.index in [y.index for y in reg_bus0.reg_generators])
                    elif g.index == 5:
                        self.assertEqual(g.bus.index,bus5.index)
                        self.assertTrue(g.index in [y.index for y in bus5.generators])
                        if reg_bus5 is not None:
                            self.assertEqual(g.reg_bus.index,reg_bus5.index)
                            self.assertTrue(g.index in [y.index for y in reg_bus5.reg_generators])
                else:
                    self.assertTrue(g.is_in_service())
                    self.assertTrue(g.in_service)
            self.assertEqual(bus_k7_degree,bus_k7.degree)
            self.assertEqual(bus_m7_degree,bus_m7.degree)
            self.assertEqual(bus_k3_degree,bus_k3.degree)
            self.assertEqual(bus_m3_degree,bus_m3.degree)
            for b in net.branches:
                if b.index == 0 or b.index == 1:
                    self.assertTrue(b.is_in_service())
                    self.assertTrue(b.in_service)
                    if b.index == 0:
                        self.assertEqual(b.bus_k.index,bus_k7.index)
                        self.assertEqual(b.bus_m.index,bus_m7.index)
                        self.assertTrue(b.index in [y.index for y in bus_k7.branches_k])
                        self.assertTrue(b.index in [y.index for y in bus_k7.branches])
                        self.assertFalse(b.index in [y.index for y in bus_k7.branches_m])
                        self.assertFalse(b.index in [y.index for y in bus_m7.branches_k])
                        self.assertTrue(b.index in [y.index for y in bus_m7.branches])
                        self.assertTrue(b.index in [y.index for y in bus_m7.branches_m])
                    elif b.index == 1:
                        self.assertEqual(b.bus_k.index,bus_k3.index)
                        self.assertEqual(b.bus_m.index,bus_m3.index)
                        self.assertTrue(b.index in [y.index for y in bus_k3.branches_k])
                        self.assertTrue(b.index in [y.index for y in bus_k3.branches])
                        self.assertFalse(b.index in [y.index for y in bus_k3.branches_m])
                        self.assertFalse(b.index in [y.index for y in bus_m3.branches_k])
                        self.assertTrue(b.index in [y.index for y in bus_m3.branches])
                        self.assertTrue(b.index in [y.index for y in bus_m3.branches_m])

            # do it again
            net = pf.Parser(case).parse(case)
            self.assertEqual(net.num_periods,1)

            # generator single contingencies
            for gen in net.generators:

                self.assertTrue(gen.is_in_service())
                cont = pf.Contingency()
                cont.add_generator_outage(gen)
                self.assertTrue(gen.is_in_service())

                bus = gen.bus
                reg_bus = gen.reg_bus if gen.is_regulator() else None

                gens = bus.generators
                if reg_bus is not None:
                    reg_gens = reg_bus.reg_generators

                cont.apply(net)
                cont.apply(net)
                cont.apply(net)

                self.assertFalse(gen.is_in_service())
                if reg_bus is not None:
                    self.assertTrue(gen.is_regulator())
                gen.bus
                if reg_bus is not None:
                    gen.reg_bus
                self.assertTrue(gen.index in [x.index for x in bus.generators])
                self.assertTrue(gen.index in [x.index for x in gens])
                if reg_bus is not None:
                    self.assertTrue(gen.is_regulator())
                    self.assertTrue(gen.index in [x.index for x in reg_bus.reg_generators])
                    self.assertTrue(gen.index in [x.index for x in reg_gens])

                cont.clear(net)
                cont.clear(net)
                cont.clear(net)

                self.assertTrue(gen.is_in_service())
                self.assertEqual(gen.bus.index,bus.index)
                if reg_bus is not None:
                    self.assertTrue(gen.is_regulator())
                    self.assertEqual(gen.reg_bus.index,reg_bus.index)
                self.assertTrue(gen.index in [x.index for x in gens])
                self.assertTrue(gen.index in [x.index for x in bus.generators])
                self.assertEqual(len(gens),len(bus.generators))
                self.assertTrue(set(map(lambda x: x.index,bus.generators)) ==
                                set(map(lambda x: x.index,gens)))
                if reg_bus is not None:
                    self.assertTrue(gen.index in [x.index for x in reg_gens])
                    self.assertTrue(gen.index in [x.index for x in reg_bus.reg_generators])
                    self.assertEqual(len(reg_gens),len(reg_bus.reg_generators))
                    self.assertTrue(set(map(lambda x: x.index,reg_bus.reg_generators)) ==
                                    set(map(lambda x: x.index,reg_gens)))

            # branch single contingencies
            for br in net.branches:

                self.assertTrue(br.is_in_service())
                cont = pf.Contingency()
                cont.add_branch_outage(br)
                self.assertTrue(br.is_in_service())

                bus_k = br.bus_k
                bus_m = br.bus_m
                reg_bus = br.reg_bus if br.is_tap_changer_v() else None

                bus_k_branches_k = bus_k.branches_k
                bus_k_branches_m = bus_k.branches_m
                bus_k_branches = bus_k.branches
                bus_m_branches_k = bus_m.branches_k
                bus_m_branches_m = bus_m.branches_m
                bus_m_branches = bus_m.branches

                if reg_bus is not None:
                    reg_trans = reg_bus.reg_trans

                br_types = (br.is_line(),
                            br.is_fixed_tran(),
                            br.is_phase_shifter(),
                            br.is_tap_changer(),
                            br.is_tap_changer_v(),
                            br.is_tap_changer_Q())

                cont.apply(net)
                cont.apply(net)
                cont.apply(net)

                self.assertFalse(br.is_in_service())
                if reg_bus is not None:
                    self.assertTrue(br.is_tap_changer())
                self.assertTupleEqual(br_types, (br.is_line(),
                                                 br.is_fixed_tran(),
                                                 br.is_phase_shifter(),
                                                 br.is_tap_changer(),
                                                 br.is_tap_changer_v(),
                                                 br.is_tap_changer_Q()))
                br.bus_k
                br.bus_m
                if reg_bus is not None:
                    br.reg_bus

                if br.bus_k.index != br.bus_m.index:
                    self.assertFalse(br.index in [x.index for x in bus_k.branches_m])
                    self.assertFalse(br.index in [x.index for x in bus_m.branches_k])
                else:
                    self.assertTrue(br.index in [x.index for x in bus_k.branches_m])
                    self.assertTrue(br.index in [x.index for x in bus_m.branches_k])
                self.assertTrue(br.index in [x.index for x in bus_k.branches_k])
                self.assertTrue(br.index in [x.index for x in bus_k.branches])
                self.assertTrue(br.index in [x.index for x in bus_m.branches_m])
                self.assertTrue(br.index in [x.index for x in bus_m.branches])

                if br.bus_k.index != br.bus_m.index:
                    self.assertFalse(br.index in [x.index for x in bus_k_branches_m])
                    self.assertFalse(br.index in [x.index for x in bus_m_branches_k])
                else:
                    self.assertTrue(br.index in [x.index for x in bus_k_branches_m])
                    self.assertTrue(br.index in [x.index for x in bus_m_branches_k])
                self.assertTrue(br.index in [x.index for x in bus_k_branches_k])
                self.assertTrue(br.index in [x.index for x in bus_k_branches])
                self.assertTrue(br.index in [x.index for x in bus_m_branches_m])
                self.assertTrue(br.index in [x.index for x in bus_m_branches])

                if reg_bus is not None:
                    self.assertTrue(br.is_tap_changer())
                    self.assertTrue(br.index in [x.index for x in reg_bus.reg_trans])
                    self.assertTrue(br.index in [x.index for x in reg_trans])

                cont.clear(net)
                cont.clear(net)
                cont.clear(net)

                self.assertTrue(br.is_in_service())
                self.assertEqual(br.bus_k.index,bus_k.index)
                self.assertEqual(br.bus_m.index,bus_m.index)
                if reg_bus is not None:
                    self.assertTrue(br.is_tap_changer_v())
                    self.assertTrue(br.is_tap_changer())
                    self.assertEqual(br.reg_bus.index,reg_bus.index)


                if br.bus_k.index != br.bus_m.index:
                    self.assertFalse(br.index in [x.index for x in bus_k_branches_m])
                    self.assertFalse(br.index in [x.index for x in bus_k.branches_m])
                else:
                    self.assertTrue(br.index in [x.index for x in bus_k_branches_m])
                    self.assertTrue(br.index in [x.index for x in bus_k.branches_m])
                self.assertTrue(br.index in [x.index for x in bus_k_branches_k])
                self.assertTrue(br.index in [x.index for x in bus_k_branches])
                self.assertTrue(br.index in [x.index for x in bus_k.branches_k])
                self.assertTrue(br.index in [x.index for x in bus_k.branches])
                self.assertEqual(len(bus_k_branches_k),len(bus_k.branches_k))
                self.assertEqual(len(bus_k_branches_m),len(bus_k.branches_m))
                self.assertEqual(len(bus_k_branches),len(bus_k.branches))

                if br.bus_k.index != br.bus_m.index:
                    self.assertFalse(br.index in [x.index for x in bus_m_branches_k])
                    self.assertFalse(br.index in [x.index for x in bus_m.branches_k])
                else:
                    self.assertTrue(br.index in [x.index for x in bus_m_branches_k])
                    self.assertTrue(br.index in [x.index for x in bus_m.branches_k])
                self.assertTrue(br.index in [x.index for x in bus_m_branches])
                self.assertTrue(br.index in [x.index for x in bus_m_branches_m])
                self.assertTrue(br.index in [x.index for x in bus_m.branches])
                self.assertTrue(br.index in [x.index for x in bus_m.branches_m])
                self.assertEqual(len(bus_m_branches_k),len(bus_m.branches_k))
                self.assertEqual(len(bus_m_branches_m),len(bus_m.branches_m))
                self.assertEqual(len(bus_m_branches),len(bus_m.branches))

                self.assertTrue(set(map(lambda x: x.index,bus_k_branches_k)) ==
                                set(map(lambda x: x.index,bus_k.branches_k)))
                self.assertTrue(set(map(lambda x: x.index,bus_k_branches_m)) ==
                                set(map(lambda x: x.index,bus_k.branches_m)))
                self.assertTrue(set(map(lambda x: x.index,bus_k_branches)) ==
                                set(map(lambda x: x.index,bus_k.branches)))

                self.assertTrue(set(map(lambda x: x.index,bus_m_branches_k)) ==
                                set(map(lambda x: x.index,bus_m.branches_k)))
                self.assertTrue(set(map(lambda x: x.index,bus_m_branches_m)) ==
                                set(map(lambda x: x.index,bus_m.branches_m)))
                self.assertTrue(set(map(lambda x: x.index,bus_m_branches)) ==
                                set(map(lambda x: x.index,bus_m.branches)))

                if reg_bus is not None:
                    self.assertTrue(br.index in [x.index for x in reg_trans])
                    self.assertTrue(br.index in [x.index for x in reg_bus.reg_trans])
                    self.assertEqual(len(reg_trans),len(reg_bus.reg_trans))
                    self.assertTrue(set(map(lambda x: x.index,reg_bus.reg_trans)) ==
                                    set(map(lambda x: x.index,reg_trans)))

                self.assertTupleEqual(tuple(br_types),
                                      (br.is_line(),
                                       br.is_fixed_tran(),
                                       br.is_phase_shifter(),
                                       br.is_tap_changer(),
                                       br.is_tap_changer_v(),
                                       br.is_tap_changer_Q()))

    def test_slack_outages(self):

        for case in test_cases.CASES:

            net = pf.Parser(case).parse(case)

            generators = []
            slack_buses = []
            for bus in net.buses:
                if bus.is_slack():
                    generators += bus.generators
                    slack_buses.append(bus)

            self.assertGreater(len(generators),0)
            self.assertGreater(len(slack_buses),0)
                    
            c = pf.Contingency(generators=generators)

            c.apply(net)

            self.assertEqual(net.get_num_generators(only_in_service=True),
                             net.num_generators-len(generators))

            self.assertTrue(all([g.is_slack() for g in generators]))
            self.assertTrue(all([b.is_slack() for b in slack_buses]))

            c.clear(net)

            self.assertEqual(net.get_num_generators(only_in_service=True),
                             net.num_generators)

            self.assertTrue(all([g.is_slack() for g in generators]))
            self.assertTrue(all([b.is_slack() for b in slack_buses]))

    def test_gen_cost(self):

        for case in test_cases.CASES:

            net = pf.Parser(case).parse(case)
            self.assertEqual(net.num_periods,1)

            # variables
            net.set_flags('generator',
                          'variable',
                          'any',
                          'active power')
            self.assertEqual(net.num_vars,net.num_generators)

            # pre contingency
            net.update_properties()
            gen_cost_base = net.gen_P_cost
            func = pf.Function('generation cost',1.,net)
            func.analyze()
            func.eval(net.get_var_values())
            phi_base = func.phi
            gphi_base = func.gphi.copy()
            Hphi_base = func.Hphi.copy()
            self.assertEqual(phi_base,gen_cost_base)
            self.assertTupleEqual(gphi_base.shape,(net.num_vars,))
            self.assertEqual(Hphi_base.nnz,net.num_vars)

            # gen outages
            counter = 0
            for gen in net.generators:

                cont = pf.Contingency()
                cont.add_generator_outage(gen)
                cont.apply(net)

                func.del_matvec()
                func.analyze()
                func.eval(net.get_var_values())

                net.update_properties()

                # value
                self.assertLess(np.abs(phi_base-gen.P_cost-func.phi),1e-8)
                self.assertLess(np.abs(gen_cost_base-gen.P_cost-net.gen_P_cost),1e-8)

                # grad
                gphi = func.gphi
                self.assertEqual(gphi[gen.index_P],0.)
                gphi[gen.index_P] = gphi_base[gen.index_P]
                self.assertLess(np.linalg.norm(gphi-gphi_base,np.inf),1e-8)

                # Hessian
                Hphi = func.Hphi
                self.assertTrue(np.all(Hphi.row != gen.index_P))
                self.assertTrue(np.all(Hphi.col != gen.index_P))

                cont.clear(net)
                counter += 1
                if counter > TEST_GENS:
                    break

            # branch outages
            counter = 0
            for br in net.branches:

                if br.bus_k.degree == 1 or br.bus_m.degree == 1:
                    continue

                cont = pf.Contingency()
                cont.add_branch_outage(br)
                cont.apply(net)

                func.del_matvec()
                func.analyze()
                func.eval(net.get_var_values())

                net.update_properties()

                # value
                self.assertLess(np.abs(phi_base-func.phi),1e-8)
                self.assertLess(np.abs(gen_cost_base-net.gen_P_cost),1e-8)

                # grad
                self.assertLess(np.linalg.norm(func.gphi-gphi_base,np.inf),1e-8)

                # Hessian
                E = func.Hphi-Hphi_base
                self.assertEqual(E.nnz,0)

                cont.clear(net)
                counter += 1
                if counter > TEST_BRANCHES:
                    break

    def test_contingency_on_multiple_nets(self):

        for case in test_cases.CASES:

            net1 = pf.Parser(case).parse(case)
            net2 = net1.get_copy()

            c = pf.Contingency(generators=net1.generators,
                               branches=net1.branches)
            self.assertEqual(net1.get_num_generators_out_of_service(), 0)
            self.assertEqual(net1.get_num_branches_out_of_service(), 0)
            self.assertEqual(net2.get_num_generators_out_of_service(), 0)
            self.assertEqual(net2.get_num_branches_out_of_service(), 0)

            c.apply(net1)

            self.assertEqual(net1.get_num_generators_out_of_service(), net1.num_generators)
            self.assertEqual(net1.get_num_branches_out_of_service(), net1.num_branches)
            self.assertEqual(net2.get_num_generators_out_of_service(), 0)
            self.assertEqual(net2.get_num_branches_out_of_service(), 0)

            c.apply(net2)

            self.assertEqual(net1.get_num_generators_out_of_service(), net1.num_generators)
            self.assertEqual(net1.get_num_branches_out_of_service(), net1.num_branches)
            self.assertEqual(net2.get_num_generators_out_of_service(), net2.num_generators)
            self.assertEqual(net2.get_num_branches_out_of_service(), net2.num_branches)

    def test_acpf(self):

        for case in test_cases.CASES:

            net = pf.Parser(case).parse(case).get_copy(merge_buses=True)
            self.assertEqual(net.num_periods,1)

            # variables
            net.set_flags('generator',
                          'variable',
                          'any',
                          'active power')
            net.set_flags('generator',
                          'variable',
                          'regulator',
                          'reactive power')
            net.set_flags('bus',
                          'variable',
                          'any',
                          ['voltage magnitude','voltage angle'])
            net.set_flags('branch',
                          'variable',
                          'tap changer',
                          'tap ratio')
            net.set_flags('shunt',
                          'variable',
                          'switching - v',
                          'susceptance')
            self.assertEqual(net.num_vars,
                             (net.num_generators +
                              net.get_num_reg_gens() +
                              2*net.num_buses +
                              net.get_num_tap_changers() +
                              net.get_num_switched_v_shunts()))

            # pre contingency
            net.update_properties()
            constr = pf.Constraint('AC power balance',net)
            constr.analyze()
            constr.eval(net.get_var_values())
            Pmismatches = {}
            Qmismatches = {}
            for bus in net.buses:
                Pmismatches[bus.index] = bus.P_mismatch
                Qmismatches[bus.index] = bus.Q_mismatch
            f = constr.f.copy()

            # gen outages
            counter = 0
            for gen in net.generators:

                bus = gen.bus

                cont = pf.Contingency()
                cont.add_generator_outage(gen)
                cont.apply(net)

                constr.del_matvec()
                constr.analyze()
                constr.eval(net.get_var_values())

                net.update_properties()

                self.assertLess(np.abs(constr.f[bus.dP_index]-bus.P_mismatch),1e-8)
                self.assertLess(np.abs(constr.f[bus.dQ_index]-bus.Q_mismatch),1e-8)
                self.assertLess(np.abs(f[bus.dP_index]-constr.f[bus.dP_index]-gen.P),1e-8)
                self.assertLess(np.abs(f[bus.dQ_index]-constr.f[bus.dQ_index]-gen.Q),1e-8)
                self.assertLess(np.abs(Pmismatches[bus.index]-bus.P_mismatch-gen.P),1e-8)
                self.assertLess(np.abs(Qmismatches[bus.index]-bus.Q_mismatch-gen.Q),1e-8)

                counter1 = 0
                for bus1 in net.buses:
                    if bus != bus1:
                        self.assertLess(np.abs(constr.f[bus1.dP_index]-f[bus1.dP_index]),1e-8)
                        self.assertLess(np.abs(constr.f[bus1.dQ_index]-f[bus1.dQ_index]),1e-8)
                        self.assertLess(np.abs(bus1.P_mismatch-Pmismatches[bus1.index]),1e-8)
                        self.assertLess(np.abs(bus1.Q_mismatch-Qmismatches[bus1.index]),1e-8)
                        counter1 += 1
                        if counter1 > TEST_BUSES:
                            break

                cont.clear(net)
                counter += 1
                if counter > TEST_GENS:
                    break

            # branch outages
            counter = 0
            for br in net.branches:

                if br.bus_k.degree == 1 or br.bus_m.degree == 1:
                    continue

                cont = pf.Contingency()
                cont.add_branch_outage(br)
                cont.apply(net)

                constr.del_matvec()
                constr.analyze()
                constr.eval(net.get_var_values())

                net.update_properties()

                Pkm = br.get_P_km()
                Qkm = br.get_Q_km()
                Pmk = br.get_P_mk()
                Qmk = br.get_Q_mk()

                self.assertLess(np.abs(constr.f[br.bus_k.dP_index]-br.bus_k.P_mismatch),1e-8)
                self.assertLess(np.abs(constr.f[br.bus_k.dQ_index]-br.bus_k.Q_mismatch),1e-8)
                self.assertLess(np.abs(f[br.bus_k.dP_index]-constr.f[br.bus_k.dP_index]+Pkm),1e-8)
                self.assertLess(np.abs(f[br.bus_k.dQ_index]-constr.f[br.bus_k.dQ_index]+Qkm),1e-8)
                self.assertLess(np.abs(Pmismatches[br.bus_k.index]-br.bus_k.P_mismatch+Pkm),1e-8)
                self.assertLess(np.abs(Qmismatches[br.bus_k.index]-br.bus_k.Q_mismatch+Qkm),1e-8)

                self.assertLess(np.abs(constr.f[br.bus_m.dP_index]-br.bus_m.P_mismatch),1e-8)
                self.assertLess(np.abs(constr.f[br.bus_m.dQ_index]-br.bus_m.Q_mismatch),1e-8)
                self.assertLess(np.abs(f[br.bus_m.dP_index]-constr.f[br.bus_m.dP_index]+Pmk),1e-8)
                self.assertLess(np.abs(f[br.bus_m.dQ_index]-constr.f[br.bus_m.dQ_index]+Qmk),1e-8)
                self.assertLess(np.abs(Pmismatches[br.bus_m.index]-br.bus_m.P_mismatch+Pmk),1e-8)
                self.assertLess(np.abs(Qmismatches[br.bus_m.index]-br.bus_m.Q_mismatch+Qmk),1e-8)
                
                counter1 = 0
                for bus1 in net.buses:
                    if br.bus_k != bus1 and br.bus_m != bus1:
                        self.assertLess(np.abs(constr.f[bus1.dP_index]-f[bus1.dP_index]),1e-8)
                        self.assertLess(np.abs(constr.f[bus1.dQ_index]-f[bus1.dQ_index]),1e-8)
                        self.assertLess(np.abs(bus1.P_mismatch-Pmismatches[bus1.index]),1e-8)
                        self.assertLess(np.abs(bus1.Q_mismatch-Qmismatches[bus1.index]),1e-8)
                        counter1 += 1
                        if counter1 > TEST_BUSES:
                            break
                
                cont.clear(net)
                counter += 1
                if counter > TEST_BRANCHES:
                    break

    def test_dcpf(self):

        for case in test_cases.CASES:

            net = pf.Parser(case).parse(case)
            self.assertEqual(net.num_periods,1)

            # variables
            net.set_flags('generator',
                          'variable',
                          'any',
                          'active power')
            net.set_flags('bus',
                          'variable',
                          'not slack',
                          'voltage angle')
            net.set_flags('branch',
                          'variable',
                          'phase shifter',
                          'phase shift')
            self.assertEqual(net.num_vars,
                             (net.num_generators +
                              net.num_buses-net.get_num_slack_buses() +
                              net.get_num_phase_shifters()))

            # pre contingency
            constr = pf.Constraint('DC power balance',net)
            constr.analyze()
            constr.eval(net.get_var_values())
            A = constr.A.copy()
            b = constr.b.copy()
            x = net.get_var_values()

            # gen outages
            counter = 0
            for gen in net.generators:

                bus = gen.bus

                cont = pf.Contingency()
                cont.add_generator_outage(gen)
                cont.apply(net)

                self.assertTrue(gen.has_flags('variable', 'active power'))
                self.assertFalse(gen.is_in_service())

                constr.del_matvec()
                constr.analyze()
                constr.eval(x)

                self.assertFalse(np.all(A.col != gen.index_P))
                self.assertTrue(np.all(constr.A.col != gen.index_P))

                self.assertLess(np.abs((A*x-b)[bus.index]-
                                       (constr.A*x-constr.b)[bus.index]-gen.P),1e-8)

                counter1 = 0
                for bus1 in net.buses:
                    if bus != bus1:
                        self.assertLess(np.abs((A*x-b)[bus1.index]-
                                               (constr.A*x-constr.b)[bus1.index]),1e-8)
                        counter1 += 1
                        if counter1 > TEST_BUSES:
                            break

                cont.clear(net)
                counter += 1
                if counter > TEST_GENS:
                    break

            # branch outages
            counter = 0
            for br in net.branches:

                bus_k = br.bus_k
                bus_m = br.bus_m

                if br.bus_k.degree == 1 or br.bus_m.degree == 1:
                    continue

                Pkm = br.P_km_DC

                cont = pf.Contingency()
                cont.add_branch_outage(br)
                cont.apply(net)

                constr.del_matvec()
                constr.analyze()
                constr.eval(net.get_var_values())

                self.assertLess(np.abs((A*x-b)[bus_k.index]-
                                       ((constr.A*x-constr.b)[bus_k.index]-Pkm)),1e-8)
                self.assertLess(np.abs((A*x-b)[bus_m.index]-
                                       ((constr.A*x-constr.b)[bus_m.index]+Pkm)),1e-8)

                cont.clear(net)
                counter += 1
                if counter > TEST_BRANCHES:
                    break

    def test_dc_flow_lim(self):

        for case in test_cases.CASES:

            net = pf.Parser(case).parse(case)
            self.assertEqual(net.num_periods,1)

            for branch in net.branches:
                if branch.ratingA == 0.:
                    branch.ratingA = 100.

            # variables
            net.set_flags('bus',
                          'variable',
                          'not slack',
                          'voltage angle')
            net.set_flags('branch',
                          'variable',
                          'phase shifter',
                          'phase shift')
            self.assertEqual(net.num_vars,
                             (net.num_buses-net.get_num_slack_buses() +
                              net.get_num_phase_shifters()))

            # pre contingency
            constr = pf.Constraint('DC branch flow limits',net)
            constr.analyze()
            constr.eval(net.get_var_values())
            G = constr.G.copy()
            l = constr.l.copy()
            u = constr.u.copy()
            x = net.get_var_values()

            Grow = 0
            br_map = {}
            for bus in net.buses:
                for br in bus.branches_k:
                    br_map[br.index] = Grow
                    Grow += 1

            # gen outages
            counter = 0
            for gen in net.generators:

                cont = pf.Contingency()
                cont.add_generator_outage(gen)
                cont.apply(net)

                constr.del_matvec()
                constr.analyze()
                constr.eval(x)

                self.assertEqual((G-constr.G).nnz,0)
                self.assertEqual(np.linalg.norm(l-constr.l),0.)
                self.assertEqual(np.linalg.norm(u-constr.u),0.)

                cont.clear(net)
                counter += 1
                if counter > TEST_GENS:
                    break

            # branch outages
            counter = 0
            for bus in net.buses:
                for br in bus.branches_k:

                    if br.bus_k.degree == 1 or br.bus_m.degree == 1:
                        Grow += 1
                        continue

                    cont = pf.Contingency()
                    cont.add_branch_outage(br)
                    cont.apply(net)

                    constr.del_matvec()
                    constr.analyze()
                    constr.eval(net.get_var_values())

                    lnew = constr.l.copy()
                    unew = constr.u.copy()
                    Gnew = constr.G.copy()

                    self.assertTupleEqual(lnew.shape,(l.size-1,))
                    self.assertTupleEqual(unew.shape,(u.size-1,))
                    self.assertTupleEqual(Gnew.shape,(G.shape[0]-1,G.shape[1]))

                    Grow = br_map[br.index]
                    
                    self.assertLess(np.linalg.norm(lnew-np.hstack((l[:Grow],l[Grow+1:])),np.inf),1e-8)
                    self.assertLess(np.linalg.norm(unew-np.hstack((u[:Grow],u[Grow+1:])),np.inf),1e-8)
                    indices = G.row != Grow
                    row = G.row[indices]
                    row = row - 1*(row>Grow)
                    col = G.col[indices]
                    data = G.data[indices]
                    Gcut = coo_matrix((data,(row,col)),shape=(net.num_branches-1,net.num_vars))
                    self.assertEqual((Gnew-Gcut).nnz,0)
                    
                    cont.clear(net)
                    counter += 1
                    if counter > TEST_BRANCHES:
                        break

    def test_variables(self):

        for case in test_cases.CASES:

            net = pf.Parser(case).parse(case)
            self.assertEqual(net.num_periods,1)

            cont = pf.Contingency()
            cont.add_generator_outage(net.get_generator(0))
            cont.add_branch_outage(net.get_branch(0))
            cont.add_branch_outage(net.get_branch(1))

            self.assertTrue(net.get_generator(0).is_in_service())
            self.assertTrue(net.get_branch(0).is_in_service())
            self.assertTrue(net.get_branch(1).is_in_service())

            cont.apply(net)

            self.assertFalse(net.get_generator(0).is_in_service())
            self.assertFalse(net.get_branch(0).is_in_service())
            self.assertFalse(net.get_branch(1).is_in_service())

            # variables
            net.set_flags('generator',
                          'variable',
                          'any',
                          'active power')
            net.set_flags('branch',
                          'variable',
                          'any',
                          'tap ratio')
            self.assertEqual(net.num_vars,
                             (net.num_generators-1+net.num_branches-2))
            for gen in net.generators:
                if gen.index != 0:
                    self.assertTrue(gen.has_flags('variable','active power'))
                else:
                    self.assertFalse(gen.has_flags('variable','active power'))
            for br in net.branches:
                if br.index not in [0,1]:
                    self.assertTrue(br.has_flags('variable','tap ratio'))
                else:
                    self.assertFalse(br.has_flags('variable','tap ratio'))

    def tearDown(self):

        pass
