class Calculator():

    @classmethod
    def sum(cls,a,b):
        return a+b

    @classmethod
    def subtrack(cls,a,b):
        return a-b
    
    @classmethod
    def multiply(cls,a,b):
        return a*b
    
    @classmethod
    def divide(cls,a,b):
        return a/b
    
OPERATORS_NUM = {"+":Calculator.sum,
     "-":Calculator.subtrack,
     "*":Calculator.multiply,
     "/":Calculator.divide
     }

try:
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    action = (input("Выберите действие (+,-,*,/): "))
    
    result = OPERATORS_NUM[action](x,y)
    print(result)

    if x == 0:
        raise ZeroDivisionError("Не вводи эту чушь!")

except ValueError as exc:
    print (f"Вы ввели некорректное значение:{exc}")
except ZeroDivisionError as exc:
    print (f"Вы ввели некорректное значение:{exc}")
except KeyError as exc:
    print (f"Вы ввели некорректное значение:{exc}")
except EOFError as exc:
    print (f"Вы ввели некорректное значение:{exc}")