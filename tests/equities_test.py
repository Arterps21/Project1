import unittest
from def_equities import equitiesfortest


class ClosestTest(unittest.TestCase):
    def test_1_single(self):
        self.assertEqual(equitiesfortest("equities/spb-birzha-pao"), 200)

    def test_2_single(self):
        self.assertEqual(equitiesfortest("equities/moskovskaya-birzha-oao"), 200)

    def test_3_single(self):
        self.assertEqual(equitiesfortest("equities/tcs-group-holding-plc?cid=1153662"), 200)

    def test_4_single(self):
        self.assertEqual(equitiesfortest("equities/sberbank_rts"), 200)

    def test_5_single(self):
        self.assertEqual(equitiesfortest("equities/vtb_rts"), 200)
