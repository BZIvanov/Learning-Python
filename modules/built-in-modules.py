# it will import the whole module
import random

# with the below line we can import random module and give it a different name to use below in the code
# import random as rnd
# rnd.randint(1, 5)

# with the below line we can import only parts of the module, not the whole module
# from random import randint
# randint(1, 5)

print(random.randint(1, 5))
print(random.choice(["apple", "kiwi", "banana"]))
