from django.db import models

# Create your models here.
'''Тема которую изучает пользователь'''
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        '''Возвразает строковое представление модели.'''
        return self.text