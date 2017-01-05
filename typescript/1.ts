// Soultion for Project Euler Problem #1 - https://projecteuler.net/problem=1
// (c) 2017 dpetker

let sum: number = 0;

for (let i: number = 1; i < 1000; i++) {
  if ((i % 3) === 0 || (i % 5) === 0) {
    sum += i
  }
}

console.log(`The sum of all the multiples of 3 and 5 less than 1000 is ${sum}.`);
