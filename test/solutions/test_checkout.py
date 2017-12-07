import unittest

from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_a_offer(self):
        self.assertEqual(130, checkout('AAA'))

    def test_a_single(self):
        self.assertEqual(0, checkout(""))

    def test_blank(self):
        self.assertEqual(50, checkout("A"))

    def test_b_offer(self):
        self.assertEqual(45, checkout('BB'))

    def test_all(self):
        self.assertEqual(160, checkout('BBABCD'))

    def test_error(self):
        self.assertEqual(-1, checkout('Y'))

    def test_other_error(self):
        self.assertEqual(-1, checkout(2))

    def test_unicode(self):
        self.assertEqual(130, checkout(u'AAA'))

    def test_big_a_offer(self):
        self.assertEqual(200, checkout('AAAAA'))

    def test_be_offer(self):
        self.assertEqual(130, checkout('EEBA'))

    def test_be_double_offer(self):
        self.assertEqual(130, checkout('EEEEBB'))


    def test_both_a_offer(self):
        self.assertEqual(410, checkout('AAAAAAAAAB'))


if __name__ == '__main__':
    unittest.main()
