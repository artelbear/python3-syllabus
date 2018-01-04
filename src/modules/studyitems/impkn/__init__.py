# Описал класс Киселев Николай


class Impkn:
    """Класс impkn"""

    def __init__(self, name):
        # Функция инициализации класса
        self.name = name

    def __str__(self):
        # Настройка вывода класса через print(teacher)
        return "Я - {}".format(self.name)
