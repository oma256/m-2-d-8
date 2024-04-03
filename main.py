"""
Задача 1: Фильтрация списка чисел
Напишите функцию, которая принимает список чисел и возвращает 
новый список, содержащий только четные числа из исходного списка.
"""
from random import randint


def generate_random_numbers():
   number_list = []
   for i in range(11):
      number_list.append(randint(1, 101))

   return number_list


def filter_number_list(number_list):
      
   if isinstance(number_list, str) or \
        isinstance(number_list, int) or \
          isinstance(number_list, bool):
      return 'Работаем только со списком чисел'

   result = []

   for number in number_list:
      if number % 2 == 0:
         result.append(number)
   return result


"""
Задача 2: Нахождение общих элементов
Создайте функцию, которая принимает два списка и возвращает список, 
содержащий элементы, общие для обоих списков.
"""

def get_intersection_lists(list_one, list_two):

    if isinstance(list_one, str) or isinstance(list_two, str):
       return 'Работаем только со списками'

    return list(set(list_one).intersection(set(list_two)))


"""
Задача 10: Проверка на палиндром
Создайте функцию, которая проверяет, является ли переданная строка 
палиндромом (читается одинаково в обоих направлениях).
"""


def check_palindr(text):
    if str(text) == str(text)[::-1]:
        return True
    else:
        return False
