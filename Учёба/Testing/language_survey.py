from survay import AnonymousSurvey

#Определение вопроса с созданием экземпляра AnonymousSurvey.
question = 'Какой язык ты выучил'
my_survey = AnonymousSurvey(question)

#Выводвопроса и сохранение ответов.
my_survey.show_question()
print('Нажмите q at any time to quit\n')
while True:
    response = input('Язык:')
    if response == 'q':
        break
    my_survey.store_response(response)
my_survey.show_results()