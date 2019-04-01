import unittest
from func_than_i_testing import get_formated_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        '''Проверка, правильности написания имён'''
        formated_name = get_formated_name('Alex', 'Sabadash')
        self.assertEqual(formated_name, 'Alex Sabadash')

unittest.main()