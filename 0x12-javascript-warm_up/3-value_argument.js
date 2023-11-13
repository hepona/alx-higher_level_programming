#!/usr/bin/node
const arg = process.argv;
if (arg[2]) {
    console.log(process.argv[2]);
} else {
    console.log('No argument');
}
