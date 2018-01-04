# Описал класс Киселев Николай


class Lesson:
    """Класс lesson"""

    def __init__(self, name, hours=0):
        # Функция инициализации класса
        self.name = name
        self.hours = hours

    def __str__(self):
        # Настройка вывода класса через print(teacher)
        return "Я - {}".format(self.name)

    def setCountTimer(self, hours):
        # Установка количества необходимого числа часов
        self.hours = hours
