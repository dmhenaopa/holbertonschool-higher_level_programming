#!/usr/bin/node
/* Function that prints the number of arguments printed and the argument value */
const array = [];
exports.logMe = function (item) {
  array.push(item);
  console.log(array.length - 1 + ': ' + item);
};
