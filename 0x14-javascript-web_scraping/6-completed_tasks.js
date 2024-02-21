#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
console.log(url)
request(url, (err, res, body) => {
  if (err) console.error(err);
  for (const i of body) {
    console.log(body[i])
  }

  })