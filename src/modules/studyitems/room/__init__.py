# Описал класс Киселев Николай


class Room:
    """Класс room"""

    def __init__(self, name):
        # Функция инициализации класса
        self.name = name

    def __str__(self):
        # Настройка вывода класса через print(teacher)
        return "Я - {}".format(self.name)
