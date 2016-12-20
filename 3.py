# Soultion for Project Euler Problem #3 - https://projecteuler.net/problem=3
# (c) 2016 dpetker

from util.primes import is_prime

TEST = 600851475143
curr_factor = int(round(TEST / 2, 2))

while curr_factor > 1:
  if TEST % curr_factor == 0 and curr_factor % 2 != 0 and is_prime(curr_factor):
    break

  curr_factor -= 1

print('Largest prime factor of {} is {}'.format(TEST, curr_factor))
