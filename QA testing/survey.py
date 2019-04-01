class AnonymousSurvey():
    '''Сбор анонимных ответов на вопросы'''
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        '''Выводит вопрос'''
        print(self.question)

    def store_response(self, new_response):
        #СОХРАНЯЕТ ОТВЕТ В СПИСКЕ
        self.responses.append(new_response)

    def show_result(self):
        #Выводит все результаты
        print('Результат опроса')
        for response in self.responses:
            print(' +',response)       

