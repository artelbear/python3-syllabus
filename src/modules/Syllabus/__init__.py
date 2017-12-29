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
        if type(dict_or_path) is str:
            # 2
            path = os.getcwd()
            example = os.path.join(path, dict_or_path)
            syllabus_not_parsed = open(example, 'r')
            sylla_dict = syllabus_not_parsed.read()
            syllabus_not_parsed.close()
            dictionary = eval(sylla_dict)
            self.raw = dictionary

    def __repr__(self):
        # Настройка вывода класса через print(syllabus)
        return str(self.raw)
