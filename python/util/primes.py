# Utility functions relating to prime numbers
# (c) 2016 dpetker

def is_prime(n):
  """
  Naive implementation of a primality test. Adapted from:
  https://en.wikipedia.org/wiki/Primality_test#Pseudocode
  """
  if n <= 1:
    return False
  elif n <= 3:
    return True
  elif n % 2 == 0 or n % 3 == 0:
    return False

  i = 5
  while i*i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False

    i += 6

  return True
