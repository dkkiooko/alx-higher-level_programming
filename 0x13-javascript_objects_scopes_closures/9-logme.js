#!/usr/bin/node
// prints number of arguments printed and new argument value

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
