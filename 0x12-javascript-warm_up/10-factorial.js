#!/usr/bin/node
function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (isNaN(n) || n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(Number(process.argv[2])));
