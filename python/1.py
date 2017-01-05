# Soultion for Project Euler Problem #1 - https://projecteuler.net/problem=1
# (c) 2016 dpetker

sum = 0

for i in range(1, 1000):
  if i % 3 == 0 or i % 5 == 0:
    sum += i

print('The sum of all the multiples of 3 and 5 less than 1000 is {}'.format(sum))
