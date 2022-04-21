import unittest
import solution


class Test(unittest.TestCase):

    def setUp(self):
        self.instance = solution.Solution()

    def rotateWrapper(self, nums, k):
        x = nums
        self.instance.rotate(x, k)
        return x

    def testRotate(self):
        self.assertEqual(self.rotateWrapper([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])
        self.assertEqual(self.rotateWrapper([-1, -100, 3, 99], 2), [3, 99, -1, -100])
        self.assertEqual(self.rotateWrapper([1, 2, 3, 4], 1), [4, 1, 2, 3])
        self.assertEqual(self.rotateWrapper([1, 2, 3, 4, 5, 6, 7], 0), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.rotateWrapper([1], 1), [1])


if __name__ == '__main__':
    unittest.main()
