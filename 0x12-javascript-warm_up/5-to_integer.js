#!/usr/bin/node
const arg = process.argv;
if (isNaN(arg[2]) === false) {
    console.log('My number: ', parseInt(arg[2]));
} else {
    console.log('Not a number');
}
