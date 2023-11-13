#!/usr/bin/node
const n = process.argv[2];
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    let x = '';
    for (let j = 0; j < n; j++) {
      x = x + 'X';
    }
    console.log(x);
  }
}
