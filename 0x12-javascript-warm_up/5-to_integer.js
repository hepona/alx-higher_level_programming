#!/usr/bin/node
const arg = process.argv[2];
if (Number.parseInt(arg) !== Number(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ', parseInt(arg));
}
