'''
Компонент Расписатора
Консольный Интерфейс
'''

print("Привет, Консоль.")

def question(srting="вас устраивает?\n"):
    # Короткий запрос на логику
    answer = input(srting)
    return True, answer
