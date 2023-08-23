# Tasks 1-3

class Testmethod:
    @staticmethod
    def sum(a,b):
        return a + b

    @staticmethod
    def multiply(*args):
        res = 1
        for num in args:
            res *= num
        return res

    @classmethod
    def calculate(cls,*args):
        if len(args) >= 2:
            return cls.sum(args[0],args[1])+cls.multiply(*args[2:])

args = [1,2,3,4,5,6]
result = Testmethod.calculate(*args)
print(result)

# Task 4

class Meta(type):
    def __new__(cls,name,base,attrs):
        attrs.update({"Min_row": 1, "Max_row" : 10})
        return type.__new__(cls,name,base,attrs)

class Row(metaclass=Meta):
    def get_data(self):
        return(0, 0)

row = Row()
print(row.Min_row)