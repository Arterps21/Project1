import unittest
from def_news import newsfortest


class ClosestTest(unittest.TestCase):
    def test_1_single(self):
        self.assertEqual(newsfortest("сбер"), 200)
    def test_2_single(self):
        self.assertEqual(newsfortest("Московская биржа"), 200)
    def test_3_single(self):
        self.assertEqual(newsfortest("Apple"), 200)
    def test_4_single(self):
        self.assertEqual(newsfortest("Тинькофф"), 200)
    def test_5_single(self):
        self.assertEqual(newsfortest("Совкомбанк"), 200)
    