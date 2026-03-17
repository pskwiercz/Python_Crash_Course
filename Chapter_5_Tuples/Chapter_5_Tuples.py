point = (1, 20)
print(point[1])

meals = ('mushrooms', 'onions', 'pineapple', 'onions')
print("onions" in meals)
print(meals.count('onions')) # 2 - two times onions in tuples
print(meals.count('mushrooms')) # 1
print(meals.index('pineapple')) # 2

# len, max, min, sum, sorted, reversed

print(list(meals)) # ['mushrooms', 'onions', 'pineapple', 'onions']
print(set(meals)) # {'onions', 'mushrooms', 'pineapple'}
print(tuple([1,2,3])) # (1, 2, 3)

for index, meal in enumerate(meals):
    print(index, meal)

print(any(meal == "pineapple" for meal in meals)) # True
print(any(meal.startswith("p") for meal in meals)) # True

print(all("o" in meal for meal in meals)) # False
print(all(meal == "onions" for meal in meals)) # False
