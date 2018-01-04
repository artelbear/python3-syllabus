# Описал класс Киселев Николай


class Teacher:
    """Класс учитель - основная часть ТОЛЬКО ВИЗУАЛЬНОЙ СТРУКТУРЫ"""

    def __init__(self, name, surname="", fathername=""):
        # Функция инициализации класса
        self.name = name
        self.surname = surname
        self.fathername = fathername
        self.lessons = {}

    def __str__(self):
        # Настройка вывода класса через print(teacher)
        return "Меня зовут {} {} {}".format(self.surname, self.name, self.fathername)

    def rename(self, name=False, surname=False, fathername=False):
        if name != False:
            self.name = name
        if surname != False:
            self.surname = surname
        if fathername != False:
            self.fathername = fathername

    def addLesson(self, lesson):
        newLesson = lesson
        self.lessons = {}
 