import unittest
import solution


class Test(unittest.TestCase):
    def setUp(self):
        self.instance = solution.Solution()

    def testSearch(self):
        self.assertEqual(self.instance.search([-1, 0, 3, 5, 9, 12], 9), 4)

    def testNoAnswer(self):
        self.assertEqual(self.instance.search([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == '__main__':
    unittest.main()
