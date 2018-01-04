# Описал класс Киселев Николай


class teacher:
    """Класс учитель - основная часть ТОЛЬКО ВИЗУАЛЬНОЙ СТРУКТУРЫ"""

    def __init__(self, name, surname, fathername):
        # Функция инициализации класса
        self.name = name
        self.surname = surname
        self.fathername = fathername

    def __str__(self):
        # Настройка вывода класса через print(teacher)
        return "Меня зовут {} {} {}".format(self.surname, self.name, self.fathername)

    # Здесь будет информация описанная ниже
    #   These are the so-called “rich comparison” methods. The correspondence
    #   between operator symbols and method names is as follows: x<y calls
    #   x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y), x!=y calls
    #   x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).

    def addLesson(self, lesson):
        pass
