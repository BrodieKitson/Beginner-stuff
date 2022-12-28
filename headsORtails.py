import random

input("Heads or Tails? ")

random_side = random.randint(0, 1)

if random_side == 0:
  print("Tails")
else:
  print("Heads")
