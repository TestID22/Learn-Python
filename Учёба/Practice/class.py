class infected():
    total = 0
    def status():
        print("всего инфецированных " , infected.total)
    def __init__(self,name,sname):
        print("Поиск выживших")
        self.name = name
        self.sname = sname
        infected.total += 1
    def __str__(self):
        n = "Объект класса Заражённые\n"
        n += "Имя: \n\t" + self.name + "\n Фамилия:\n\t" + self.sname + "\n Статус: \n\tУбивать СРОЧНО!"
        return n
    def talk(event):
        print("Я ранен") 

John = infected("Вини ","Джонс")
Cory = infected("Кори","Тейлор")
Sara = infected("Сара","Конор")
Sara.talk()
infected.status()
