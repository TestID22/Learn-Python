def order(size_pizza,*orders):
    print('\n Размер вашей пиццы: ',size_pizza)
    print('Добавки к пицце:')
    for order in orders:
        
        print('-',order)

order(12,'Картошка','Кола','Лобстер')