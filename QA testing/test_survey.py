import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''Тетируем класс'''
    def test_store_single_response(self):
        question = 'What first Language do you speak?'
        #create obj a class AnonymousSurvey
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        '''тестируем на наличие трёх элементов в списке'''
        question = 'What first Language do you speak?'
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Python']
        #Из списка responses берём Языки и добавляем в список, 
        # при помощи метода my_survey.store_response 
        for response in responses:
            my_survey.store_response(response)
        #Проверяем есть ли в списке каждый элемент из списка responses - ГАДДЭМ!!!
        for response in responses:
            self.assertIn(response, my_survey.responses) 
               

unittest.main()