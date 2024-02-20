#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
request(url, (err, res, body) => {
  if (err) console.error(err);
  else {
    const fs = require('fs');
    fs.writeFile(file, body, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
