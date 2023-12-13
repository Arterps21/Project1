import unittest
from def_photo import photo


class ClosestTest(unittest.TestCase):
    def test_1_single(self):
        self.assertEqual(photo("https://www.1zoom.ru/big2/541/255095-Sepik.jpg"), 200)
    def test_2_single(self):
        self.assertEqual(photo("https://w.forfun.com/fetch/c8/c86afb95ddb1dbd07dbc06a7aa432e0a.jpeg"), 200)
    def test_3_single(self):
        self.assertEqual(photo("https://w.forfun.com/fetch/22/22396c9115a8b621fc158309466c1bf6.jpeg"), 200)
    def test_4_single(self):
        self.assertEqual(photo("https://w.forfun.com/fetch/3d/3d0064328645371409b1b7b9bbd1ae86.jpeg"), 200)
    def test_5_single(self):
        self.assertEqual(photo("https://w.forfun.com/fetch/90/9019ce2ebe10975533a9b242e79b26ee.jpeg"), 200)