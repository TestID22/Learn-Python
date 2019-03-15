#Практика работы со словорями
elliot = {'name':{'first':'Elliot','second':'Anderson'},
          'age': 42,
          'pay': (40000,60000),
          'job':['CyberSecurity', 'Hacker']
          }

print(elliot['job'][0])
elliot['job'].append('fsocietyleader')
elliot['name']['hidden'] = 'Mr.Robot'
print(elliot)
