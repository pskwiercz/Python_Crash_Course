bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1]) # print last element in table
print(bicycles[-2]) # print second last element in table

print(f"My first bike was {bicycles[0].title()}")

friends = ['Adam', 'Tomek', 'Ziuek']
for f in friends:
    print(f"Hi {f}")

motors = ['honda', 'yamaha', 'suzuki']
motors.append('ducatti')
motors.insert(1, 'wsk')
print(motors)

# Removing elements - del, pop, remove
del motors[1]
print(motors)
el = motors.pop()
print(motors)
print(el)
el = motors.pop(1)
print(motors)
motors.remove('honda')
print(motors)
print()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(cars)

cars.reverse() # NOT SORTED!!!! only reverse

print(len(cars))

# Range
for i in range(1,4):
    print(i)

list1 = list(range(1,5)) # 1-5 == 1,2,3,4 -> NOT 5!
print(list1)

list2 = list(range(2,11,2))
print(list2)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# List Comprehensions
squares1 = [value**2 for value in range(1,11)]
print(squares1)

cubes = [value**3 for value in range(1,11)]
print(cubes)

# Slicing
pl = ['charles', 'martina', 'michael', 'florence', 'eli']
print(pl[0:3]) # ['charles', 'martina', 'michael']
print(pl[0:4:2]) # ['charles', 'michael']
print(pl[:2]) # ['charles', 'martina']
print(pl[2:]) # 'michael', 'florence', 'eli']
print(pl[:-2]) # ['charles', 'martina', 'michael']
print(pl[-2:]) # ['florence', 'eli']

for n in pl[0:3]:
    print(n)


# Copy list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # <------- copy listK

if my_foods is friend_foods:
    print("same list")
else:
    print("not same list")

if my_foods == friend_foods:
    print("list contains the same items")
else:
    print("list not contains the same items")

print('falafel' in my_foods)    # True
print('falafel' not in my_foods) # False

# Check if list is empty
food = []
if food:
    print("Not empty")
else:
    print("Empty")