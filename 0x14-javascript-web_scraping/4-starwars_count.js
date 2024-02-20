#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  else {
    let count = 0;
    const ch = JSON.parse(body).results;
    for (let i = 0; i < ch.length; i++) {
      if ((ch[i].characters).includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
