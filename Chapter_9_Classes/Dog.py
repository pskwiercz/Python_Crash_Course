class Dog:
    """ Class Dog """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")

    def roll_over(self):
        print(f"{self.name} is rolling over")


dog = Dog("Willie", 10)
dog.sit()
dog.roll_over()