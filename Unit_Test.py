import unittest


def kuadrat(angka):
    if angka >= 0:
        return angka * angka
    else:
        raise ValueError("Angka harus non-negatif")


class TestKalkulator(unittest.TestCase):
    def test_kuadrat(self):
        self.assertEqual(kuadrat(5), 25)
        self.assertEqual(kuadrat(0), 0)
        self.assertRaises(ValueError, kuadrat, -3)


if __name__ == "__main__":
    unittest.main()
