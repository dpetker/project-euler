# Soultion for Project Euler Problem #3 - https://projecteuler.net/problem=3
# Algorithm adapted from - http://stackoverflow.com/questions/23287/largest-prime-factor-of-a-number
# (c) 2016 dpetker

ORIGINAL = 600851475143
test = ORIGINAL
factors = []
divisor = 2

while test > 1:
  while test % divisor == 0:
    factors.append(divisor)
    test /= divisor

  divisor += 1

  if divisor * divisor > test:
    if test > 1:
      factors.append(test)
      break

print('Largest prime factor of {} is {}'.format(ORIGINAL, max(factors)))
