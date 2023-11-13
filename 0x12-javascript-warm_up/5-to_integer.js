#!/usr/bin/node
const arg = process.argv;
if (isNaN(arg[2]) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ', parseInt(arg[2]));
}
