# select chap 4 exercises
print('exercise 4-3: use for loop to print numbers from 1 to 20')
for val in range(1,21):
    print(val)

print('exercise 4-4: use for loop to print numbers from 1 to 100,000,000')
print('(commented out for now)')
#for val in range(1,100000001):
#    print(val)

print('exercise 4-5: sum numbers from 1 to a million')
numbers = list(range(1,100000001))
print(f"numbers min: {min(numbers)}")
print(f"numbers max: {max(numbers)}")
print(f"numbers sum: {sum(numbers)}")

print('exercise 4-6: list odd numbers from 1 to 20')
odd_numbers = list(range(1,20,2))
for odd_number in odd_numbers:
    print(odd_number)

print('exercise 4-7: make a list of multiples of 3 from 3 to 30')
three_multiples = list(range(1,31,3))
for three_multiple in three_multiples:
    print(three_multiple)

print('exercise 4-8: print cubes of 1-10')
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

print('exercise 4-9: make the same list of cubes with a list comprehension')
cubes = [value**3 for value in range(1,11)]
print(cubes)

print('exercise 4-10-1: print first three items of an existing list')
print(f"the first three odd numbers are {odd_numbers[:3]}")

print('exercise 4-10-2: print three middle items of an existing list')
print(f"three middle odd numbers are {odd_numbers[1:4]}")

print('exercise 4-10-3: print the last three items of an existing list')
print(f"three last numbers to a million: {numbers[-3:]}")

print('exercise 4-11: pizza list manipulation')
my_pizzas = ['pepperoni', 'cheese', 'sausage']
friend_pizzas = my_pizzas[:]
my_pizzas.append('mushroom')
friend_pizzas.append('olive')
for pizza in my_pizzas:
    print(f'I like {pizza} pizza')
for pizza in friend_pizzas:
    print(f'My friend likes {pizza} pizza')

print('exercise 4-13-1: print buffet tuple')
buffet_foods = ('cheeseburgers','turkey','fries','gravy','soda')
for food in buffet_foods:
    print(f"buffet food: {food}")

print ('exercise 4-13-2: tuple change rejected (commented out)')
#buffet_foods[0] = 'spaghetti'

print ('exercise 4-13-3: replace buffet tuple')
buffet_foods = ('spaghetti','turkey','pizza','gravy','soda')
for food in buffet_foods:
    print(f"buffet food: {food}")
