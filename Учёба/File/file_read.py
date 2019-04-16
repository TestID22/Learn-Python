f =  open('Zona_stalker.txt')
hello = f.read().split()
print('Количество слова в книге "Сталкер"', len(hello))
input('Нажмите Enter для выхода')