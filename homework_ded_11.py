# # Task 1-2

def g_progression (min,n,max):
    import pdb; pdb.set_trace()
    for i in range(min,max + 1):
        result = min * (n ** i)
        yield result
generator = g_progression(1,3,10)
for value in generator:
    print(value)

#  Task3

import re
input = str(input("Введите адрес почты:"))
def input_data(e_mail):
    testmail = r"^(?!\.)(?!.*\.@)(?!.*\.\.)[A-Za-z0-9.!#  %&'*+—/=?^_`{|}~]+@(?!\-)[a-z0-9{63}\-]+\.[a-z]+(?!\-)$"
    result = re.match(testmail,input) is not None
    print(result)
input_data(input)

#  Task4

import random
MY_LIST = ["s", "f", "q", "p", "s", "g"]
def name_generator(numbers):
    for number in range(1,numbers+1):
        name = "".join([random.choice(MY_LIST) for i in range(random.randint(1, 10))])
        yield name + str(number)
for item in name_generator(5):
    print(item)