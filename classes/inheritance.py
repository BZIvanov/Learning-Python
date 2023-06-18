class Animal:
    color = "colorful"

    def make_sound(self, sound):
        print(f"Animay says: {sound}")


class Cat(Animal):
    pass


my_cat = Cat()
my_cat.make_sound("Meow")  # Meow
print(isinstance(my_cat, Animal))  # True
print(isinstance(my_cat, Cat))  # True
