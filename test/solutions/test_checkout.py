import unittest

from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_a_offer(self):
        self.assertEqual(130, checkout(['A', 'A', 'C']))


if __name__ == '__main__':
    unittest.main()