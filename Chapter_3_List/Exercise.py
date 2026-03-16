persons = ['Adam', 'Tomek', 'Ziutek']
for p in persons:
    print(f"Come {p.title()} to dinner")

persons[1] = 'Basia'
for p in persons:
    print(f"Come {p.title()} to dinner")

persons.insert(0, 'Tomek')
persons.insert(0, 'Kasia')
persons.append('Viola')
print(persons)

persons.pop()
persons.pop()
persons.pop()
persons.pop()
print(persons)

persons.remove('Tomek')
persons.remove('Kasia')
print(persons)

