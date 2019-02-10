class AnonymousSurvey():
    '''Сбор анонимных ответов на вопросы'''
    def __init__(self, question):
        '''Сохраняет вопрос и готовится к сохранению ответов.'''
        self.question = question
        self.responses = []
    
    def show_question(self):
        '''Выводит Вопрос'''
        print(question)
    
    def store_response(self, new_response):
        '''Сохраняeт один ответ на опрос.'''
        self.responses.append(new_response)
    
    def show_results(self):
        '''Выводит все полученные ответы.'''
        print('Покажу результат:')
        for response in responses:
            print('-' + response)
            