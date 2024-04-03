import unittest

from main import (
    filter_number_list, 
    get_intersection_lists, 
    check_palindr
)


class TestFilterNumberListFunc(unittest.TestCase):

    def test_success(self):
        number_list = [1, 4, 2, 8, 9, 54, 56, 13]
        self.assertEqual(filter_number_list(number_list), [4, 2, 8, 54, 56])

    def test_with_string(self):
        string = 'programming'
        self.assertEqual(filter_number_list(string), 
                         'Работаем только со списком чисел')
    
    def test_with_int(self):
        number = 34
        self.assertEqual(filter_number_list(number),
                         'Работаем только со списком чисел')

    def test_with_bool(self):
        number = True
        self.assertEqual(filter_number_list(number),
                         'Работаем только со списком чисел')


class TestGetIntesectionListsFunc(unittest.TestCase):

    def test_success(self):
        numbers_one = [1, 2, 3, 4, 2, 456, 7, 5, 6]
        numbers_two = [4, 5, 6, 7, 8, 9, 56, 34, 78]

        numbers = get_intersection_lists(numbers_one, numbers_two)
        result = [4, 7, 6, 5]
        self.assertCountEqual(numbers, result)
        for number in numbers:
            self.assertIn(number, result)
    
    def test_empty_lists(self):
        numbers_one = []
        numbers_two = []
        numbers = get_intersection_lists(numbers_one, numbers_two)
        self.assertEqual(numbers, [])

    def test_with_string(self):
        numbers_one = 'programming'
        numbers_two = 'programm'
        numbers = get_intersection_lists(numbers_one, numbers_two)
        self.assertEqual(numbers, 'Работаем только со списками')


class TestCheckPalindrFunc(unittest.TestCase):

    def test_result_true(self):
        name = 'aziza'
        self.assertTrue(check_palindr(name))

    def test_result_false(self):
        name = 'iman'
        self.assertFalse(check_palindr(name))

    def test_with_number_true(self):
        number = 1001
        self.assertTrue(check_palindr(number))

    def test_with_number_false(self):
        number = 1234
        self.assertFalse(check_palindr(number))
