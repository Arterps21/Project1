import unittest
from def_main import mainfortest


class ClosestTest(unittest.TestCase):
    def test_1_single(self):
        self.assertEqual(mainfortest("сбер"), None)

    def test_2_single(self):
        self.assertEqual(mainfortest("English"), None)

    def test_3_single(self):
        self.assertEqual(mainfortest("/start"),["Какое действие выполнить",'Узнать котировки', 'Прочитать новости', 'Прочитать аналитические статьи'])
    def test_4_single(self):
        self.assertEqual(mainfortest("Привет"), None)

    def test_5_single(self):
        self.assertEqual(mainfortest("Ещё"), None)
