# Task 1,2

import time
class Auto:
    def __init__(self,brand,age,mark,color = None,weight = None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight
    def move(self):
        print("move")
    def stop(self):
        print("stop")
    def birthday(self):
        self.age += 1
        print(self.age)

class Truck(Auto):
    def __init__(self,brand,age,mark,max_load,color = None,weight = None):
        super().__init__(brand,age,mark,color,weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()
    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

class Car(Auto):
    def __init__(self,brand,age,mark,max_speed,color = None,weight = None):
        super().__init__(brand,age,mark,color,weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("max speed is <max_speed>")

truck = Truck("peterbild",1967,"duck",10,"black",2000)
truck.move()
truck.stop()
truck.birthday()
truck.load()
print(f"Brand:{truck.brand},Age:{truck.age},Mark:{truck.mark},Max load:{truck.max_load},Color:{truck.color},Weight:{truck.weight}")



car = Car("toyota",2000,"landcruiser",80,"gray",1500)
car.move()
car.stop()
car.birthday()
print(f"Brand:{car.brand},Age:{car.age},Mark:{car.mark},Color:{car.color},Weight:{car.weight}")

# Task 3

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def __sub__(self,other):
        radius_difference = abs(self.radius - other.radius)
        if radius_difference == 0:
            return Point(0,0)
        return radius_difference


class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b

circle_1 = Circle(20)
circle_2 = Circle(40)

print(circle_1 - circle_2)
print(circle_1.get_area())