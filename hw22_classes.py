class Animal():

    def __init__(self, name='', weight=0, state='голодный', eggs=0):
        self.name = name
        self.weight = weight
        self.state = state
        self.eggs = eggs

    def feed(self):
        self.state = 'сытый'
        print(self.state)


class Cattle(Animal):
    def milk(self):
        print('надой неплох')

    def voice_cow(self):
        print('муууу')

    def voice_goat(self):
        print('бееее')


class Sheep(Animal):
    def wool(self):
        print('шерсть настригли')

    def voice_sheep(self):
        print('мееее')


class Poultry(Animal):
    def get_eggs(self, eggs):
        print('яиц собрано ', eggs)


class Geese(Poultry):
    def voice_geese(self):
        print('га-га-га')


class Hens(Poultry):
    def voice_hen(self):
        print('кукареку')


class Ducks(Poultry):
    def voice_duck(self):
        print('кря')


total_weight = 0
max_weight = 0
list_animals = list()

cow0 = Cattle('Манька', 500)
print('корова', cow0.name, '-', cow0.weight, 'кг')
cow0.feed()
cow0.milk()
cow0.voice_cow()
list_animals.append(cow0)

goose0 = Geese('Серый', 6)
print('гусь', goose0.name, '-', goose0.weight, 'кг')
goose0.feed()
goose0.get_eggs(0)
goose0.voice_geese()
list_animals.append(goose0)

goose1 = Geese('Белый', 7)
print('гусь', goose1.name, '-', goose1.weight, 'кг')
goose1.feed()
goose1.get_eggs(2)
goose1.voice_geese()
list_animals.append(goose1)

sheep0 = Sheep('Барашек', 25)
print('баран', sheep0.name, '-', sheep0.weight, 'кг')
sheep0.feed()
sheep0.wool()
sheep0.voice_sheep()
list_animals.append(sheep0)

sheep1 = Sheep('Кудрявый', 30)
print('баран', sheep1.name, '-', sheep1.weight, 'кг')
sheep1.feed()
sheep1.wool()
sheep1.voice_sheep()
list_animals.append(sheep1)

hen0 = Hens('Ко-Ко', 1)
print('курица', hen0.name, '-', hen0.weight, 'кг')
hen0.feed()
hen0.get_eggs(3)
hen0.voice_hen()
list_animals.append(hen0)

hen1 = Hens('Кукареку', 2)
print('петух', hen1.name, '-', hen1.weight, 'кг')
hen1.feed()
hen1.get_eggs(0)
hen1.voice_hen()
list_animals.append(hen1)

goat0 = Cattle('Рога', 50)
print('козел', goat0.name, '-', goat0.weight, 'кг')
goat0.feed()
goat0.voice_goat()
list_animals.append(goat0)

goat1 = Cattle('Копыта', 55)
print('козочка', goat1.name, '-', goat1.weight, 'кг')
goat1.feed()
goat1.milk()
goat1.voice_goat()
list_animals.append(goat1)

duck0 = Ducks('Кряква', 3)
print('утка', duck0.name, '-', duck0.weight, 'кг')
duck0.feed()
duck0.get_eggs(2)
duck0.voice_duck()
list_animals.append(duck0)

for creature in list_animals:
    total_weight += creature.weight
    if max_weight < creature.weight:
        max_weight = creature.weight

print('общий вес - ', total_weight)
print('максимальный вес - ', max_weight)