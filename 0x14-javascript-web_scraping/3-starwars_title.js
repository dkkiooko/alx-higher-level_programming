#!/usr/bin/node
// prints title of Star Wars movie id is argv[2]

const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
