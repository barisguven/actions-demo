import random

num = random.random()

with open('numbers.txt', 'a') as file:
  file.write(f'{str(num)}\n')