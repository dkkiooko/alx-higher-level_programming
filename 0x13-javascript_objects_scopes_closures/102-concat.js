#!/usr/bin/node
// concats 2 files

const files = process.argv;
const fs = require('fs');
fs.readFile(files[2], 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  fs.appendFile(files[4], data, function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
fs.readFile(files[3], 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  fs.appendFile(files[4], data, function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
