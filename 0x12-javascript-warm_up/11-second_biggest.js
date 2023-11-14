#!/usr/bin/node

const t = process.argv.slice(2);
if (t.length === 0 || t.length === 1) {
  console.log('0');
} else {
  console.log(Math.max(...t.map(Number)) - 1);
}
