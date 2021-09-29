import unittest

from modelssort import Sorting
from merge_practis import Merge_prac

class TestSort(unittest.TestCase):

    def test_bubble_sort(self):
        instance = Sorting()
        instance.random_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        arr = instance.bubble_sort()
        self.assertEqual(arr,[1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_merge_sort(self):
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        arr = Sorting.merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quick_sort(self):
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        arr = Sorting.quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_Sum(self):
        arr = [-1, 0, 1, 2, -1, -4]
        arr = Sorting.Sum(arr)
        print(arr)

class TestMerge(unittest.TestCase):

    def test_merge_prac(self):
        arr= [-1, 5, 3, 4, 0]
        arr= Merge_prac.merge_prac(arr)
        print(arr)
        self.assertEqual(arr, [-1, 0, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()