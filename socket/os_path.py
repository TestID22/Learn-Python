import os 

user = os.path.join('user','bin') 
print(user)

file_paths = ['bin', 'user']
for i in file_paths:
    print(os.path.join('C:/users\\'), i.strip())