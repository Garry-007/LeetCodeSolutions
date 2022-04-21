import unittest
import solution


class Test(unittest.TestCase):
    def setUp(self):
        self.instance = solution.Solution()

    def moveZeroesWrapper(self, nums):
        x = nums
        self.instance.moveZeroes(x)
        return x

    def testMoveZeroes(self):
        self.assertEqual(self.moveZeroesWrapper([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(self.moveZeroesWrapper([0]), [0])
        self.assertEqual(self.moveZeroesWrapper([0, 0]), [0, 0])
        self.assertEqual(self.moveZeroesWrapper([0, 1, 0]), [1, 0, 0])
        self.assertEqual(self.moveZeroesWrapper([0, 5, 0, 3, 0]), [5, 3, 0, 0, 0])
        self.assertEqual(self.moveZeroesWrapper([1, 5, 0, 3, 0, 4, 8, 0]), [1, 5, 3, 4, 8, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
