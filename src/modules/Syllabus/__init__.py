# Модуль класса "Syllabus" с методами
# ......
# ......

# Описал класс Киселев Николай


import os, time


class Syllabus:
    # Класс для создания объекта "Расписание" подерживающие создание методом
    # syllabus(dictianary), а также загрузку из файла методом
    # syllabus("./example.syllabus")

    def __init__(self, dict_or_path):
        # Обработка значения, которое должно стать основным параметром этого
        # класса. В конце любого из условий записывает в .storage СЛОВАРЬ (описание
        # в docs). Если это уже составленный "syllabus" в виде словоря, запись
        # происходи мгновенно ( # 1 ). Если это путь, то происходит построение
        # абсолютного пути к файлу, чтение файла и превращение в словарь, затем
        # запись в .storage ( # 2 )

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
            self.storage = dict_or_path
        elif type(dict_or_path) is str:
            # 2
            s = open(dict_or_path, 'r')
            s_dict = s.read()
            s.close()
            dictionary = eval(s_dict)
            self.storage = dictionary
        self.cashe = self.write_cashe()

    def __str__(self):
        # Настройка вывода класса через print(syllabus)
        return str(self.storage)

    # Здесь будет информация описанная ниже
    #   These are the so-called “rich comparison” methods. The correspondence
    #   between operator symbols and method names is as follows: x<y calls
    #   x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y), x!=y calls
    #   x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).

    def __eq__(self, other):
        # Реакция на логическую операцию равенства "=="
        try:
            if self.storage == other.storage:
                return True
            else:
                return False
        except:
            raise ValueError("{} is not syllabus".format(other))

    def __getitem__(self, keys):
        # Реакция на вызов через syllabus[x] (#1)
        # Добавленна подержка обращения через syllabus[x, y] (#2)
        if type(keys) == str:
            # 1
            return self.storage[keys]
        elif type(keys) == tuple:
            # 2
            try:
                return self.storage[keys[0]][keys[1]]
            except:
                raise ValueError("[{}] is not valid syllabus key. (__getitem__)".format(str(keys)))
        else:
            raise ValueError("[{}] is not valid syllabus key. (__getitem__)".format(str(keys)))
        
    def __setitem__(self, keys, value):
        # Реакция на вызов через syllabus[x] = "data" (#1)
        # Добавленна подержка обращения через syllabus[x, y] = "data" (#2)
        if type(keys) == str:
            # 1
            self.storage[keys] = value
        elif type(keys) == tuple:
            # 2
            try:
                self.storage[keys[0]][keys[1]] = value
            except:
                raise ValueError("[{}] is not valid syllabus key. (__setitem__)".format(str(keys)))
        else:
            raise ValueError("[{}] is not valid syllabus key. (__setitem__)".format(str(keys)))

    def com(self):
        # Компиляция в чистую и красивую таблицу вызываемую через eval("...") возращает обычный словарь
        m = self.markup # обозначение в голове документа
        s = self.storage
        # Загрузка модуля для превода таблиц в читаемую строку (модуль pprint)
        s = __import__("pprint").pformat(s, depth=2, width=50)
        # Времяштамп в приличное время
        time_creation = time.ctime(float(self["meta", "created"]))
        # Введение комментариев для будуещего ффайла (автор и так далее)
        m = m.format(self["meta", "author"], time_creation, self["meta", "year"], self["meta", "semester"])
        return m + s

    def make(self):
        self["meta", "created"] = time.time()
        return self.com()

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

    def write(self, name, path=os.getcwd(), make=True):
        try:
            position = open(self.cashe_path, 'w')
            if make == True:
                position.write(self.make())
            else:
                position.write(self.com())
            position.close()
            self.exit()
        except:
            raise FileNotFoundError(
                "Cant create file {}/{}.syllabus\nCan you put valid adress PLEASE!".format(path, name))

    def exit(self):
        # Убираем кэш
        if self.cashe_path != "allready":
            os.remove(self.cashe_path)
            self.cashe_path = "allready"