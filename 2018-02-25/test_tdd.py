"""Testy do zadan z zajec 2018-02-25
"""
import unittest
import tdd
import random


class TestMoje(unittest.TestCase):

    def test_test(self):
        self.assertTrue(True)

    def test_f1_1(self):
        b = tdd.f1(0)
        self.assertEqual(b, 0)

    def test_f1_2(self):
        b = tdd.f1(1)
        self.assertEqual(b, 1)

    def test_f1_3(self):
        b = tdd.f1(2)
        self.assertEqual(b, 4)

    def test_f1_4(self):
        b = tdd.f1(2, 1)
        self.assertEqual(b, 5)

    def test_f1_5(self):
        b = tdd.f1(2, 3)
        self.assertEqual(b, 7)

    def test_f2_1(self):
        b = tdd.f2("ala")
        self.assertEqual(b, "a")

    def test_f2_2(self):
        b = tdd.f2([1, 2, 3])
        self.assertEqual(b, 1)

    def test_f2_3(self):
        b = tdd.f2([])
        self.assertEqual(b, "BUUUUM")

    def test_f3_1(self):
        b = tdd.f3(1)
        self.assertEqual(b, "jeden")

    def test_f3_2(self):
        b = tdd.f3(2)
        self.assertEqual(b, "dwa")

    def test_f3_3(self):
        b = tdd.f3(3)
        self.assertEqual(b, "trzy")

    def test_f3_4(self):
        b = tdd.f3(random.choice(range(4, 1000)))
        self.assertEqual(b, "other")

    def test_f4_1(self):
        b = tdd.f4("ala")
        self.assertEqual(b, "ala ma kota")

    def test_f4_2(self):
        b = tdd.f4("kot")
        self.assertEqual(b, "kot ma kota")

    def test_f4_3(self):
        b = tdd.f4("kot", "psa")
        self.assertEqual(b, "kot ma kota i psa")

    def test_f4_4(self):
        b = tdd.f4("kot", "mysz")
        self.assertEqual(b, "kot ma kota i mysz")

    def test_f5_1(self):
        b = tdd.f5(0)
        self.assertEqual(b, [])

    def test_f5_2(self):
        b = tdd.f5(1)
        self.assertEqual(b, [0])

    def test_f5_3(self):
        b = tdd.f5(2)
        self.assertEqual(b, [0, 1])

    def test_f5_4(self):
        b = tdd.f5(7)
        self.assertEqual(b, [0, 1, 2, 3, 4, 5, 6])

    def test_f5_5(self):
        b = tdd.f5(7, 2)
        self.assertEqual(b, [0, 2, 4, 6])

    def test_f5_6(self):
        b = tdd.f5(17, 2)
        self.assertEqual(b, [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_f5_7(self):
        b = tdd.f5(17, 5)
        self.assertEqual(b, [0, 5, 10, 15])

    def test_f6_1(self):
        b = tdd.f6(1, "*")
        self.assertEqual(b, "*")

    def test_f6_2(self):
        b = tdd.f6(7, "*")
        self.assertEqual(b, "*******")

    def test_f7_1(self):
        b = tdd.f7("ala")
        self.assertEqual(b, "slowo")

    def test_f7_2(self):
        b = tdd.f7(1)
        self.assertEqual(b, "cyfra")

    def test_f7_3(self):
        b = tdd.f7(11111)
        self.assertEqual(b, "liczba")

    def test_f7_4(self):
        b = tdd.f7(-11111)
        self.assertEqual(b, "liczba_ze_znakiem")

    def test_f7_5(self):
        b = tdd.f7("Ala ma kota.")
        self.assertEqual(b, "zdanie")

    def test_f7_6(self):
        b = tdd.f7("<taaag>")
        self.assertEqual(b, "tag poczatkowy")

    def test_f7_7(self):
        b = tdd.f7("</taaag>")
        self.assertEqual(b, "tag koncowy")

    def test_f8_1(self):
        b = tdd.f8("kot", "ala ma kota")
        self.assertTrue(b)

    def test_f8_2(self):
        b = tdd.f8("pies", "ala ma kota")
        self.assertFalse(b)

    def test_f9_1(self):
        b = tdd.f9(1, 2)
        self.assertEqual(b, "dodatnie")

    def test_f9_2(self):
        b = tdd.f9(-1, -2)
        self.assertEqual(b, "ujemne")

    def test_f9_3(self):
        b = tdd.f9(-1, 1)
        self.assertEqual(b, "roznych znakow")

    def test_f9_4(self):
        b = tdd.f9(-1, 0)
        self.assertEqual(b, "jest zero")

    def test_f10_1(self):
        b = tdd.f10(1, 1)
        self.assertEqual(b, "rowne")

    def test_f10_2(self):
        b = tdd.f10(1, 2)
        self.assertEqual(b, "rozne")

    def test_f19_1(self):
        b = tdd.f19(1, 2)
        self.assertEqual(b, "rozne")

    def test_f20_1(self):
        b = tdd.f20("Wynik to:1231231239")
        self.assertEqual(b, "1231231239")

    def test_f100_1(self):
        r = tdd.f100("<tag></tag>")
        self.assertEqual(r, "")

    def test_f100_2(self):
        r = tdd.f100("<tag>ala ma kota</tag>")
        self.assertEqual(r, "ala ma kota")

    def test_f100_3(self):
        r = tdd.f100("<tag>ala ma kota</tag>")
        self.assertEqual(r, "ala ma kota")

    def test_f100_4(self):
        r = tdd.f100("<tag>1 > 0</tag>")
        self.assertEqual(r, "1 > 0")

    def test_f100_5(self):
        r = tdd.f100("<tag>ala ma kota</tag></tag>")
        self.assertEqual(r, "ala ma kota")

    def test_f100_6(self):
        r = tdd.f100("<tag><tag>ala ma kota</tag></tag>")
        self.assertEqual(r, "ala ma kota")

    def test_f100_7(self):
        r = tdd.f100("<tag><tag>1 > 0</tag></tag>")
        self.assertEqual(r, "1 > 0")

    def test_f100_8(self):
        r = tdd.f100("<tag><tag><tag>ala ma kota</tag></tag></tag>")
        self.assertEqual(r, "ala ma kota")

    def test_f100_9(self):
        r = tdd.f100("<tag><tag><tag>1 > 0</tag></tag></tag>")
        self.assertEqual(r, "1 > 0")


if __name__ == '__main__':
    unittest.main()
