
# a = ('мадам','собака','кот','бабка','казак')
# def polindr(a:tuple) -> tuple:
#     """фильтрует полиндромы"""
#     res = tuple(filter(lambda x: str(x) == str(x)[::-1], a))
#     print(res)
#     print (polindr.__doc__)
# polindr(a)

# def decor(func):
#     def wrapper(x):
#         result = list(map(lambda a: a * 2 + 10, x))
#         print(result)

#     return wrapper


# @decor
# def calc_1(list_obj: list):
#     print(list_obj)

# calc_1(list_obj)

# a=4
# def dec(func):
#     def wrapper (x):
#         print('привет')
#         result = x*2
#         print (result)
#         print (input(str('медвед')))
#     return wrapper

# @dec
# def bred (a):
#     print (a)

# bred (a)

# from datetime import datetime
# time = datetime.now()
# print(time)


# import datetime
 
# def timelapse(func):
#     def wrapper(a,b,c):
#         start = datetime.datetime.now()
#         result = func(a,b,c)
#         finish = datetime.datetime.now()
#         total_time = finish - start
#         print(f"Total time: {total_time}")
#     return wrapper

# @timelapse
# def function (x,y,z):
#     result = (f"Скажу тебе: {x} {y} {z}")
#     print(result)
# function(1,2,3)


def converter (value : str): 
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









