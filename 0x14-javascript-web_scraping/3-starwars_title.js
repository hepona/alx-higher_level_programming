#!/usr/bin/node
const request = require('request');
const idmovie = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + idmovie;
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
