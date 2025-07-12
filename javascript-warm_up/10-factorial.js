#!/usr/bin/node

function factorial (x) {
  if (isNaN(x)) {
    return 1;
  }
  if (x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}

const n = parseInt(process.argv[2]);
console.log(factorial(n));
