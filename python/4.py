# Soultion for Project Euler Problem #4 - https://projecteuler.net/problem=4
# (c) 2016 dpetker

curr_max = 0

for i in range(999, 0, -1):
  for j in range(999, 0, -1):
    test = i * j
    test_str = str(test)
    if test_str == test_str[::-1] and test > curr_max:
      curr_max = test

print('The largest palindrome made from the product of two 3-digit numbers is {}'.format(curr_max))
