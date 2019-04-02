import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        '''
        Создание вопроса, самого опроса(объекта класса),
        и вариантов ответов
        '''
        question = 'What first Language do you speak?'

        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish', 'Python']


    '''Тетируем класс'''
    def test_store_single_response(self):
        question = 'What first Language do you speak?'
        #create obj a class AnonymousSurvey
        my_survey = AnonymousSurvey(question)
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.responses)

    def test_store_three_response(self):
        '''тестируем на наличие трёх элементов в списке'''
        #Из списка responses берём Языки и добавляем в список, 
        # при помощи метода my_survey.store_response 
        for response in self.responses:
            self.my_survey.store_response(response)
        #Проверяем есть ли в списке каждый элемент из списка responses - ГАДДЭМ!!!
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses) 
               

unittest.main()