filename = 'D:\Code\Python\Учёба\File\\text.txt'
with open(filename) as r_object:
    lines = r_object.readlines()
    string = ' '
    for line in lines:
        string += line.strip()
    print(string)
    print(len(string))