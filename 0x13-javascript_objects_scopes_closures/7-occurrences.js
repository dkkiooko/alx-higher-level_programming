#!/usr/bin/node
// returns the number of occurrences in a list

exports.nb0occurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
