# Soultion for Project Euler Problem #7 - https://projecteuler.net/problem=7
# (c) 2017 dpetker

from util.primes import is_prime

n = 13
ctr = 6

while True:
  n = n + 2
  if is_prime(n):
    ctr += 1

    if ctr == 10001:
      break

print('The 10 001st prime number is {}'.format(n))
