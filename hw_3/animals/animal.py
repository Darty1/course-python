import json
import csv

# import food as food

total_eat = [
    {
        "type": "seed",
        "quantity": 10
    },
    {
        "type": "meat",
        "quantity": 6
    },
    {
        "type": "fish",
        "quantity": 2
    }
]

cat = []

dog = []

conor = []

cat_count = int(input('input cat count '))
dog_count = int(input('input dog count '))
conor_count = int(input('input conor count '))


# def csv_reader(file_obj):
#   reader = csv.reader(file_obj)
#  for row in reader:
#         print(" ".join(row))
# csv_path = "food.csv"
# with open(csv_path, "r") as f_obj:
#   csv_reader(f_obj)
# with open("food.json", "r") as read_file:
#    f = json.loads(food, read_file)


class Animal(object):

    def __init__(self, count, type_eat, dead_line):
        self.type_eat = type_eat
        self.dead_line = dead_line
        self.count = count

    def eat(self, type_eat, dead_line):
        self.type_eat = type_eat
        self.dead_line = dead_line
        for row in total_eat:
            if row["type"] == self.type_eat and row["quantity"] > 0:
                row["quantity"] -= 1
            elif row["type"] == self.type_eat and row["quantity"] == 0:
                self.dead_line -= 1

    def dead(self, dead_line, count):
        self.dead_line = dead_line
        self.count = count
        print('dead_line', self.dead_line)
        if dead_line == 0:
            print('im ok ')
            self.count -= 1
            print('COUNT', cat_count, ' ', dog_count, ' ', conor_count)
            print('1 animal is dead')


class Cat(Animal):

    def __init__(self, dead_line):
        self.dead_line = dead_line
        self.count = cat_count
        self.type_eat = "fish"


class Dog(Animal):

    def __init__(self, dead_line):
        self.dead_line = dead_line
        self.count = dog_count
        self.type_eat = "meat"


class Conor(Animal):

    def __init__(self, dead_line):
        self.dead_line = dead_line
        self.count = conor_count
        self.type_eat = "seed"


for i in range(0, cat_count - 1):
    cat.append(Cat(1))

for i in range(0, dog_count - 1):
    dog.append(Dog(1))

for i in range(0, conor_count - 1):
    conor.append(Conor(1))

day = 1
while day <= 15:
    print('day : ', day)
    for i in reversed(cat):
        i.eat(i.type_eat, i.dead_line)
        i.dead(i.dead_line, cat_count)
        if i.dead_line == 0:
            del i

    for i in reversed(dog):
        i.eat(i.type_eat, i.dead_line)
        i.dead(i.dead_line, dog_count)
        if i.dead_line == 0:
            del i

    for i in reversed(conor):
        i.eat(i.type_eat, i.dead_line)
        i.dead(i.dead_line, conor_count)
        if i.dead_line == 0:
            del i

    day += 1

    print('cat: ', cat_count, '|dog: ', dog_count, '|conor: ', conor_count)
    print(total_eat)

print('all is dead')
