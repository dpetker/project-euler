# Soultion for Project Euler Problem #5 - https://projecteuler.net/problem=5
# (c) 2016 dpetker

# Start with this as the problem states its the smallest value evenly divisible
# by 1-10
test_val = 2520

def test_divisors(n):
  for i in range(1, 21):
    if n % i != 0:
      return False

  return True

while True:
  test_val += 20
  if test_divisors(test_val):
    break

print('The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {}'.format(test_val))
