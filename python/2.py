# Soultion for Project Euler Problem #2 - https://projecteuler.net/problem=2
# (c) 2016 dpetker

sum = 0
fib = [1, 1]
current = 1

while current < 4000000:
  current = fib[-1] + fib[-2]
  fib.append(current)

for i in fib:
  if i % 2 == 0:
    sum += i

print('The sum of all the even Fibonacci terms less than 4 million is {}'.format(sum))
