# Soultion for Project Euler Problem #6 - https://projecteuler.net/problem=6
# (c) 2017 dpetker

n = 100

sum_of_squares = (n * (n + 1) * ((2 * n) + 1)) / 6
square_of_sum = pow(((n * (n + 1)) / 2), 2)

test_val = abs(sum_of_squares - square_of_sum)

print('The difference between the sum of the squares of the first 100 natural numbers and the square of the sum is {}'.format(test_val))
