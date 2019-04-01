from survey import AnonymousSurvey
''' create a question'''
quest = 'What first languge do you speak?'

'''create a new object with our question'''
my_survey = AnonymousSurvey(quest)
#Вывод вопроса
my_survey.show_question()
print('Enter "q" for exit')
while True:
    response = input('Language: ')
    if response == 'q': 
        break
    my_survey.store_response(response)

#Show Result
print('Thanks for all, who participated in survey')
my_survey.show_result()
