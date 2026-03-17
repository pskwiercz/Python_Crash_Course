alien = {'color': 'red', 'points': 5}
print(alien['color'])
point_value = alien.get('speed', 'No point value assigned.')
print(point_value)

alien['position'] = 3
print(alien)

alien['color'] = 'blue'
print(alien)
del alien['color']
print(alien)

langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
print(langs['phil'].title())

user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, val in user.items():
    print(f'Key: {key} - Value: {val}')
print()

# Keys
for name in langs.keys():
    print(f"Name: {name.title()}")
print()

for name in  sorted(langs.keys()):
    print(f"Name: {name.title()}")
print()

# Values
for val in langs.values():
    print(f"Value: {val.title()}")
print()

# Values without duplicates
for val in set(langs.values()):
    print(f"Value: {val.title()}")

