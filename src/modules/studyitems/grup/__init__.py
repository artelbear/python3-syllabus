# Описал класс Киселев Николай


class Grup:
    """Класс grup"""

    def __init__(self, name):
        # Функция инициализации класса
        self.name = name

    def __str__(self):
        # Настройка вывода класса через print(teacher)
        return "Я - {}".format(self.name)
