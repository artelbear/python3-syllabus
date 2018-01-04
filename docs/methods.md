# Краткое описание методов модулей

1. `module syllabus > class Syllabus(dict_or_path)`
	1. `= self.storage ` - словарь в сыром формате
	2. `= self.com()` - компилировать в eval(словарь-строка)
	3. `= self.make()` - аналог self.com, только с обновлением времени
	4. `= self.html()` - компилировать в html-код
	5. `self.__eq__(other)` `self == other`
	6. `self.__str__()` `str(self)`
	7. `self.__getitem__(x)` `self[x]` `self[x, y]` - взять значение по индексу
	8. `self.__setitem__(x, value)` `self[x] = z` `self[x, y] = z` - назначить значение по индексу
	9. `self.read_cache()` - переписать `self` из кеша
	10. `self.write_cache()` - написать `self` в кеш
	11. `self.write(name, path=os.getcwd(), make=False)` - записать файл по имени `name`, по пути `path` (по умолчанию текущая рабочая директория), с перезаписью времени `make` (`boolean`)
	12. `self.exit()` - стереть кеш
2. 