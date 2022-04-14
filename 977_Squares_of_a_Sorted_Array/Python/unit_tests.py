import unittest
import solution


class Test(unittest.TestCase):
    def setUp(self):
        self.instance = solution.Solution()

    def testSortedSquares(self):
        self.assertEqual(self.instance.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(self.instance.sortedSquares([-4, -1, 0, 4, 10]), [0, 1, 16, 16, 100])
        self.assertEqual(self.instance.sortedSquares([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(self.instance.sortedSquares([2, 2, 2, 2, 2]), [4, 4, 4, 4, 4])
        self.assertEqual(self.instance.sortedSquares([-2, -2, -2, -2, -2]), [4, 4, 4, 4, 4])
        self.assertEqual(self.instance.sortedSquares([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])


if __name__ == '__main__':
    unittest.main()
