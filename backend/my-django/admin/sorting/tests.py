from django.test import TestCase

# Create your tests here.
import unittest

from admin.sorting.models import MySum,Palindrome

class TestMySum(unittest.TestCase):

    def test_one_to_ten_sum_1(self):
        intstance = MySum()
        intstance.start_number = 1
        intstance.end_number = 11
        res = intstance.one_to_ten_sum_2()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)

    def test_reverse_str(self):
        ints = Palindrome()
        ints.input_string = "hellow"
        res3 = ints.reverse_string()
        res2 = ints.str_to_list()
        print(f'reverse : {res3}')
        print(f'palindrome : {res2}')


if __name__ == '__main__':
    unittest.main()