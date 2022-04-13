import unittest
import solution


class Test(unittest.TestCase):
    def setUp(self):
        self.instance = solution.Solution()

    def testSearch(self):
        self.assertEqual(self.instance.searchInsert([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(self.instance.searchInsert([-1, 0, 3, 5, 9, 12], 3), 2)
        self.assertEqual(self.instance.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(self.instance.searchInsert([1, 3, 5, 6], 1), 0)
        self.assertEqual(self.instance.searchInsert([1, 3, 5, 6], 6), 3)

    def testInsertIndex(self):
        self.assertEqual(self.instance.searchInsert([-1, 0, 3, 5, 9, 12], 2), 2)
        self.assertEqual(self.instance.searchInsert([-1, 0, 3, 5, 9, 12], 6), 4)
        self.assertEqual(self.instance.searchInsert([1, 3, 5, 6], 4), 2)
        self.assertEqual(self.instance.searchInsert([1, 3, 5, 6], -2), 0)
        self.assertEqual(self.instance.searchInsert([1, 3, 5, 6], 8), 4)


if __name__ == '__main__':
    unittest.main()
