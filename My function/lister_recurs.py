import os, sys
#Рекурсивная функция обхода каталогов
def my_lister(curdir):
    print('[' + curdir + ']')
    for file in os.listdir(curdir):
        path = os.path.join(curdir, file)
        if not os.path.isdir(path):
            print(path)
        else:
            my_lister(path)

if __name__ == "__main__":
    my_lister(sys.argv[1])