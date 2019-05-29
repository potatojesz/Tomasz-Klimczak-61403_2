import unittest

import mLista


class TestMLista(unittest.TestCase):

    def test_create(self):
        testList = mLista.MLista(10)
        self.assertIsNotNone(testList, "MLista did not create")
        self.assertEqual(testList.capacity, 10, "Capacity should be 10")

    def test_rozmiar(self):
        testList = mLista.MLista(5)
        self.assertEqual(testList.rozmiar(), 0, "Length should be 0")
        testList.dodaj_element(5)
        self.assertEqual(testList.rozmiar(), 1, "Length should be 1")

    def test_pojemnosc(self):
        testList = mLista.MLista(5)
        self.assertEqual(testList.pojemnosc(), 5, "Capacity should be 5")
        self.assertEqual(testList.capacity, 5, "Capacity should be 5")
        self.assertTrue(testList.zwieksz_pojemnosc(5), "Should be TRUE")
        self.assertEqual(testList.pojemnosc(), 10, "Capacity should be 10")
        self.assertEqual(testList.capacity, 10, "Capacity should be 10")
        self.assertTrue(testList.zmniejsz_pojemnosc(3), "Should be TRUE")
        self.assertEqual(testList.pojemnosc(), 7, "Capacity should be 7")
        self.assertEqual(testList.capacity, 7, "Capacity should be 7")
        self.assertFalse(testList.zmniejsz_pojemnosc(150), "Should be FALSE")
        self.assertFalse(testList.zwieksz_pojemnosc(-5), "Should be FALSE")

    def test_zwieksz_pojemnosc(self):
        testList = mLista.MLista(5)
        self.assertTrue(testList.zwieksz_pojemnosc(5), "Should be TRUE")
        self.assertFalse(testList.zwieksz_pojemnosc(-5), "Should be FALSE")

    def test_zmniejsz_pojemnosc(self):
        testList = mLista.MLista(5)
        self.assertTrue(testList.zmniejsz_pojemnosc(3), "Should be TRUE")
        self.assertFalse(testList.zmniejsz_pojemnosc(150), "Should be FALSE")

    def test_usun_powtorzenia(self):
        testList = mLista.MLista(5)
        testList.dodaj_element(5)
        testList.dodaj_element(5)
        self.assertEqual(testList.rozmiar(), 2, "Length should be 2")
        testList.usun_powtorzenia(5)
        self.assertEqual(testList.rozmiar(), 1, "Length should be 1")

    def test_dodaj_element(self):
        testList = mLista.MLista(1)
        self.assertTrue(testList.dodaj_element(5), "Should be TRUE")
        self.assertFalse(testList.dodaj_element(5), "Should be FALSE")

    def test_znajdz(self):
        testList = mLista.MLista(5)
        testList.dodaj_element(5)
        testList.dodaj_element(4)
        testList.dodaj_element(3)
        self.assertEqual(testList.znajdz(3), 2, "Index should be 2")
        self.assertEqual(testList.znajdz(4), 1, "Index should be 1")
        self.assertEqual(testList.znajdz(6), -1, "Index should be -1")

    def test_pobierz(self):
        testList = mLista.MLista(5)
        testList.dodaj_element(5)
        testList.dodaj_element(4)
        testList.dodaj_element(3)
        self.assertEqual(testList.pobierz(0), 5, "Value should be 5")
        self.assertEqual(testList.pobierz(2), 3, "Value should be 3")

    def test_odwroc(self):
        testList = mLista.MLista(3)
        testList.dodaj_element(5)
        testList.dodaj_element(4)
        testList.dodaj_element(3)
        testList.odwroc()
        self.assertEqual(testList.pobierz(0), 3, "Value should be 3")
        self.assertEqual(testList.pobierz(1), 4, "Value should be 4")
        self.assertEqual(testList.pobierz(2), 5, "Value should be 5")
