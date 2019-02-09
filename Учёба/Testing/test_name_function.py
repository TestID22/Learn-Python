import unittest
from name_function import get_formared_name

class NamesTestCast(unittest.TestCase):
    '''Тест для name_function'''
    def first_test_last_name(self):
        '''Имена работают правильно?'''
        formated_name = get_formared_name('Alex','Shepard')
        self.assertEqual(formated_name,'Alex Shepard')

unittest.main()