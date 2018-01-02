# Модуль класса "Teacher" с методами
# ......
# ......

# Описал класс Киселев Николай


class Teacher:
    """Класс для создания объекта "препод" со всеми вытекающими."""


    def __init__(self, name):
        # Функция, которая пускается на объявлении функции
        # Например:
        # A = Teacher("Ленин")
        # print(A.name)
        # вернет "Ленин"
        self.name = name

    def __repr__(self):
        # Когда вызовут переменную через print(...) будет возращена строка
        # Например:
        # A = Teacher("Ленин")
        # print(A)
        # вернет Здравствуйте, я Teacher. Меня зовут Ленин"
        return "Здравствуйте, я {}. Меня зовут {}".format(self.type, self.name)

    # Здесь будет информация описанная ниже
    #   These are the so-called “rich comparison” methods. The correspondence
    #   between operator symbols and method names is as follows: x<y calls
    #   x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y), x!=y calls
    #   x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).

    def addLesson(self, lesson_name):
        pass
