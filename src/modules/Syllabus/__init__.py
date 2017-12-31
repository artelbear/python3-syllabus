# Модуль класса "Syllabus" с методами
# ......
# ......

# Описал класс Киселев Николай


import os


class Syllabus:
    # Класс для создания объекта "Расписание" подерживающие создание методом
    # syllabus(dictianary), а также загрузку из файла методом
    # syllabus("./example.syllabus")

    def __init__(self, dict_or_path):
        # Обработка значения, которое должно стать основным параметром этого
        # класса. В конце любого из условий записывает в .raw СЛОВАРЬ (описание
        # в docs). Если это уже составленный "syllabus" в виде словоря, запись
        # происходи мгновенно ( # 1 ). Если это путь, то происходит построение
        # абсолютного пути к файлу, чтение файла и превращение в словарь, затем
        # запись в .raw ( # 2 )

        if type(dict_or_path) is dict:
            # 1
            self.raw = dict_or_path
        elif type(dict_or_path) is str:
            # 2
            s = open(dict_or_path, 'r')
            s_dict = s.read()
            s.close()
            dictionary = eval(s_dict)
            self.raw = dictionary

    def __str__(self):
        # Настройка вывода класса через print(syllabus)
        return str(self.raw)

    # Здесь будет информация описанная ниже
    #   These are the so-called “rich comparison” methods. The correspondence
    #   between operator symbols and method names is as follows: x<y calls
    #   x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y), x!=y calls
    #   x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).

    def __eq__(self, other):
        # Реакция на логическую операцию равенства "=="
        try:
            if self.raw == other.raw:
                return True
            else:
                return False
        except:
            raise ValueError("{} is not syllabus".format(other))

    def __getitem__(self, keys):
        if type(keys) == tuple:
            pass

    def make(self):
        pass

    def read(self):
        pass

    def write(self, path, name):
        syllabus_not_parsed = open(path, 'r')
        sylla_dict = syllabus_not_parsed.read()
        syllabus_not_parsed.close()