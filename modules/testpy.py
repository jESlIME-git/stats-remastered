# Импорт встроенных функций
# Импортируются из директории Func
from Func.menu import menu
from Func.inp import inp

# Так-же можно импортировать сторонние и встроеные модули 
from time import sleep

def mod():
    options = [
        "Опция #1",
        "Опция #2",
        "Опция #3"
    ] 
    
    # Создание базового меню
    # Возвращает цифру номера опции(начаная с нуля)
    answer = menu(options, "Выберите опцию")
    
    print(f"Вы выбрали {options[answer]}({answer} опция)")
    sleep(2)
    
    # Создание инпута
    answer2 = inp("Какой ваш возвраст:")
    print(f"Вам {answer2} лет")
    
    print(f"{answer} {answer2}")
    sleep(2)