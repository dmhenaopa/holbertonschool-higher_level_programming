#!/usr/bin/node
// Function that converts a number from base 10 to another base
exports.converter = function (base) {
  return function numberConverter (number) {
    return number.toString(base);
  };
};
