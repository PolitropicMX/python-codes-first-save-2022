#uso de random library
import random

print("")

value = random.random()# a number between 0 and 1 but never 0 and 1

print(value)

value1 = random.uniform(1,10)

print(value1)

value2 = random.randint(1,6)# dice

print(value2)

value3 = random.randint(0,1)

print(value3)

greeding = ['Hello','Hi','Hey','Howdy','Hola']

value4 = random.choice(greeding)

print(value4 + ' fer!')

rgb = ['red','blue','green']

value5 = random.choices(rgb, k = 10)

print(value5)

value6 = random.choices(rgb, weights=[18,10,2], k = 10)

print(value6)

cards = list(range(1,53))
print(cards)

random.shuffle(cards)

print(cards)
