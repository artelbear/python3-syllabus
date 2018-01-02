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

        # разметка читаемого сжатого расписания
        self.markup = \
"""# autor: {0}
# created: {1}
# application: https://github.com/artelbear/python3-syllabus
# year: {2}
# semester: {3}

"""

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
        self.cashe = self.write_cashe()

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
            try:
                return self.raw[keys[0]][keys[1]]
            except:
                raise ValueError("[{}] is not valid syllabus key".format(str(keys)))
        elif type(keys) == str:
            return self.raw[keys]
        else:
            raise ValueError("[{}] is not valid syllabus key".format(str(keys)))
        

    def com(self):
        m = self.markup
        s = self.raw
        s = __import__("pprint").pformat(s, depth=2, width=50)
        m = m.format(self["meta", "author"], self["meta", "created"], self["meta", "year"], self["meta", "semester"])
        return m + s

    def make(self):
        pass

    def read(self):
        pass

    def write_cashe(self):
        name = "__cashe.syllabus"
        position = open(name, 'w')
        position.write(self.com())
        position.close()
        cashe_path = "{}/{}".format(os.getcwd(), name)
        self.cashe_path = cashe_path
        return cashe_path

    def write(self, name, path=os.getcwd()):
        try:
            position = open(self.cashe_path, 'w')
            position.write(self.com())
            position.close()
            self.exit()
        except:
            raise FileNotFoundError(
                "Cant create file {}/{}.syllabus\nCan you put valid adress PLEASE!".format(path, name))

    def exit(self):
        # Убираем кэш
        os.remove(self.cashe_path)