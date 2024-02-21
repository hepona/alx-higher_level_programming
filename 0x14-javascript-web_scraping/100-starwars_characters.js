#!/usr/bin/node
const request = require('request');
const idfilm = process.argv[2];
const urlfilm = 'https://swapi-api.alx-tools.com/api/films/' + idfilm;
const urlchara = 'https://swapi-api.alx-tools.com/api/people/';
request(urlfilm, (err, res, body) => {
  if (err) console.error(err);
  else {
    // let count = 0;
    const idlst = [];
    const ch = JSON.parse(body).characters;
    for (const i in ch) {
      const idchara = ch[i].split('/').slice(-2, -1)[0];
      idlst.push(idchara);
    }
    for (const i in idlst) {
      request(urlchara + i, (err, res, body) => {
        if (err) console.error(err);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
