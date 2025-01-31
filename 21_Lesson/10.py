import random

A = ["Rejep", "Meret", "Oraz", "Anna"]
print(random.sample(A, 1))
print(random.sample(A, 3))
print(random.sample(A, 1))
print(A)
random.shuffle(A)
print(A)