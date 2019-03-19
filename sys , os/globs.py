import glob

#возьмём директорию при помощи глобинга
print(glob.glob('Учёба/*'))
my_dir = glob.glob('*')
for line in my_dir:
    print(line)

    