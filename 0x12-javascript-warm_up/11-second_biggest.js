#!/usr/bin/node

const t = process.argv.slice(2);
if (t.length === 0) {
  console.log('0');
} else if (t.length === 1) {
  console.log('1');
} else {
  console.log(Math.max(...t.map(Number)) - 1);
}
