#!/usr/bin/node
const n = process.argv[2];
function recursiveFactorial (n) {
  if (Number.parseInt(n) !== Number(n) || n === 0) {
    return (1);
  }
  return n * (recursiveFactorial(n - 1));
}

console.log(recursiveFactorial(parseInt(n)));
