import unittest

from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_a_offer(self):
        self.assertEqual(130, checkout('AAA'))

    def test_a_single(self):
        self.assertEqual(50, checkout("A"))

    def test_b_offer(self):
        self.assertEqual(45, checkout('BB'))

    def test_all(self):
        self.assertEqual(160, checkout('BBABCD'))

    def test_error(self):
        self.assertEqual(-1, checkout('E'))

    def test_other_error(self):
        self.assertEqual(-1, checkout(2))


if __name__ == '__main__':
    unittest.main()
