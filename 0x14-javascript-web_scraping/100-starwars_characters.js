#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const movie = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movie;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const film = JSON.parse(body);
  for (const character of film.characters) {
    request(character, function (err, res, body) {
      if (err) {
        console.log(err);
      }
      const chr = JSON.parse(body);
      console.log(chr.name);
    });
  }
});
