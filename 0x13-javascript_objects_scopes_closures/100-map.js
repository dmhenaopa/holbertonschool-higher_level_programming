#!/usr/bin/node
// Imports an array and computes a new array
const list = require('./100-data').list;
const mapList = list.map((value, index) => value * index);
console.log(list);
console.log(mapList);
