def greeting(name: str) -> None:
    print(f"Hello, {name}!")

greeting('John')
greeting(name='Bob')

def hello(name: str = 'adam') -> None:
    print(f"Hello, {name}!")

hello()
hello("John")

# middle_name is optional parameter
def get_formatted_name(first_name, last_name, middle_name = '' ):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
musician = get_formatted_name('john', 'lee')
print(musician)

# List will NOT BE MODIFIED in function - we passed copy list
# ---> function_name(list_name[:])

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
(make_pizza('mushrooms', 'green peppers', 'extra cheese'))

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)