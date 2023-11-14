#!/usr/bin/node
const n = process.argv[2];
function recursive_factorial (n) {
  if (Number.parseInt(n) !== Number(n) || n === 0) {
    return (1);
  }
  return n * recursive_factorial(n - 1);
}

console.log(recursive_factorial(parseInt(n)));
