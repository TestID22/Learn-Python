import unittest
from test_func02 import get_formated_name

class test_get_formated_name(unittest.TestCase):
    #Тест с намеренной ошибкой
    def test_get_name(self):
        formated_name = get_formated_name('Alex','Sabadash')
        self.assertEqual(formated_name, 'Alex Sabadash')
    def test_with_three_arg(self):
        '''Работают ли имена с Тремя Аргументами c Отчеством'''
        formated_name = get_formated_name('Sabadash', 'Alex', 'Vitalievich')
        self.assertEqual = (formated_name, 'Sabadash Alex Vitalievich')


#Получим ошибку...
unittest.main()