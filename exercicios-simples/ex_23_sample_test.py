import unittest

class TestSum(unittest.TestCase):

    def testValue_sum(self):

        self.assertEqual(sum([2, 4, 6]), 12, "Should be equal to 12")

    def testValue_sum_tuple(self):

        self.assertEqual(sum((1, 1, 1)), 6, "Should be equal to 6")

if __name__ == '__main__':

    unittest.main()