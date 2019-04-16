import os
#create dir
#os.makedirs('d:\\Example')
file = os.listdir('d:\\')
print(file)

totalsize = 0

for file in os.listdir('d:\\'):
    try:
        totalsize = totalsize + os.path.getsize(os.path.join('d:\\', file))
        print(file, totalsize)
    except:
        totalsize += 0
print(totalsize)