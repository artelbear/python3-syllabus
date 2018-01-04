# Модуль класса "Syllabus" с методами

# Описал класс Киселев Николай


import os
import time


class Syllabus:
    """
    Класс для создания объекта "Расписание" подерживающие создание методом
    syllabus(dictianary), а также загрузку из файла методом
    syllabus("./example.syllabus")
    """

    def __init__(self, dict_or_path):
        # Обработка значения, которое должно стать основным параметром этого
        # класса. В конце любого из условий записывает в .storage СЛОВАРЬ (описание
        # в docs). Если это уже составленный "syllabus" в виде словоря, запись
        # происходи мгновенно ( # 1 ). Если это путь, то происходит построение
        # абсолютного пути к файлу, чтение файла и превращение в словарь, затем
        # запись в .storage ( # 2 )

        # разметка заголовка читаемого сжатого расписания
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
        self.write_cache()

    def __str__(self):
        # Настройка вывода класса через print(syllabus)
        return str(self.storage)

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
                raise ValueError(
                    "[{}] is not valid syllabus key. (__getitem__)".format(str(keys)))
        else:
            raise ValueError(
                "[{}] is not valid syllabus key. (__getitem__)".format(str(keys)))

    def __setitem__(self, keys, value):
        # Реакция на вызов через syllabus[x] = "data" (#1)
        # Добавленна подержка обращения через syllabus[x, y] = "data" (#2)
        self.write_cache()
        if type(keys) == str:
            # 1
            self.storage[keys] = value
        elif type(keys) == tuple:
            # 2
            try:
                self.storage[keys[0]][keys[1]] = value
            except:
                raise ValueError(
                    "[{}] is not valid syllabus key. (__setitem__)".format(str(keys)))
        else:
            raise ValueError(
                "[{}] is not valid syllabus key. (__setitem__)".format(str(keys)))

    def com(self):
        # Компиляция в чистую и красивую таблицу вызываемую через eval("...")
        # возращает обычный словарь
        m = self.markup  # обозначение в голове документа
        s = self.storage
        # Загрузка модуля для превода таблиц в читаемую строку (модуль pprint)
        s = __import__("pprint").pformat(s, depth=2, width=50)
        # Времяштамп в приличное время
        time_creation = time.ctime(float(self["meta", "created"]))
        # Введение комментариев для будуещего ффайла (автор и так далее)
        m = m.format(self["meta", "author"], time_creation, self[
                     "meta", "year"], self["meta", "semester"])
        return m + s

    def make(self):
        # Компиляция в чистую и красивую таблицу вызываемую через eval("...") возращает обычный словарь
        # При этом обновление времени создания (штамп)
        self["meta", "created"] = time.time()
        return self.com()

    def read_cache(self):
        # Выгрузка кэша из кешпути
        self.__init__(self, self.cache_path)

    def write_cache(self):
        # Автосоздание кеша в файл
        name = "__cache.syllabus"
        cache_path = "{}/{}".format(os.getcwd(), name)
        position = open(cache_path, 'w')
        position.write(self.com())
        position.close()
        self.cache_path = cache_path

    def write(self, name, path=os.getcwd(), make=False):
        # Условно безопасная запись файла с выводом в консоль условной ошибки (# error)
        # запись с обновлением времени (#1)
        # запись без надстройки времени (#2)
        try:
            position = open("{}/{}.syllabus".format(path, name), 'w')
            if make == True:
                # 1
                position.write(self.make())
            else:
                # 2
                position.write(self.com())
            position.close()
            self.exit()
        except:
            # error
            raise FileNotFoundError(
                "Cant create file {}/{}.syllabus\nCan you put valid adress PLEASE!".format(path, name))

    def html(self):
        # Преобразование в простой html код (предназначенный для помещения в
        # теге "body")
        body_html = self.com()
        body_html = body_html.replace(" ", "&nbsp;")
        body_html = body_html.replace("\n", "\n\t\t<br>\n\t\t")
        body_html = "\t<p>\n\t\t" + body_html + "\n\t</p>"
        return body_html

    def exit(self):
        # Убираем кэш
        if self.cache_path != "allready":
            os.remove(self.cache_path)
            self.cache_path = "allready"
