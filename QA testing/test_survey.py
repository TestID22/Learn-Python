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

unittest.main()