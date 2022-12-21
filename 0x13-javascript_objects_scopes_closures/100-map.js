#!/usr/bin/node
// imports array computes a new array

const array = require('./100-data').list;
const map1 = array.map((x, index) => x * index);
console.log(array);
console.log(map1);
