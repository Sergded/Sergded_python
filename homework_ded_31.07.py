# Task 1

func = lambda x=int(input('Введите число')): print('чётное') if x % 2 == 0 else print('нечётное')
func()

# Task 2

a = [1,2,3,4,5,6,7,25,16]
def change(a:list) -> list:
    """меняет числа в списке на строки"""
    result = list(map(lambda x:str(x),a))
    print(result)
    print (change.__doc__)
change (a)

# Task 3

a = ('мадам','собака','кот','бабка','казак')
def polindr(a:tuple) -> tuple:
    """фильтрует полиндромы"""
    res = tuple(filter(lambda x: str(x) == str(x)[::-1], a))
    print(res)
    print (polindr.__doc__)
polindr(a)

# Task 4

# example 1

import datetime
 
def timelapse(func):
    def wrapper(a,b):
        start = datetime.datetime.now()
        result = func(a,b)
        finish = datetime.datetime.now()
        total_time = finish - start
        print(f"Total time: {total_time}")
    return wrapper

@timelapse
def some_function(text, text_1):
    print("Меня зовут", text, text_1)
some_function("Иван","Петрович")

# example 2

import datetime
 
def timelapse(func):
    def wrapper(a,b,c):
        start = datetime.datetime.now()
        result = func(a,b,c)
        finish = datetime.datetime.now()
        total_time = finish - start
        print(f"Total time: {total_time}")
    return wrapper

@timelapse
def function (x,y,z):
    result = (f"Скажу тебе: {x} {y} {z}")
    print(result)
function(1,2,3)

# Task 5

def converter (value : str):
    """Принимает строку, переводит в число, анализирует тип числа"""
    dotIndex = value.find(".") 
    if dotIndex > -1: 
        left = value[:dotIndex] 
        right = value[dotIndex+1:] 
        if left.isdigit() and right.isdigit(): 
            print("Вы ввели положительное дробное число :", float(value)) 
        elif left[1:].isdigit() and left[0] == "-" and right.isdigit(): 
            print("Вы ввели отрицательное дробное число :", float(value)) 
        else: 
            print("Вы ввели некоректное число!") 
    elif value.isdigit(): 
        print("Вы ввели положительное целое число :", int(value)) 
    elif value[0] == "-" and value[1:].isdigit(): 
        print("Вы ввели отрицательное целое число :", int(value)) 
    else: 
        print("Вы ввели некоректное число!")
converter('-5.4')