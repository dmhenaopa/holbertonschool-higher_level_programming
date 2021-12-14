#!/usr/bin/node
const args = process.argv;

function computeFactorial (number) {
  let result;

  if (isNaN(number) || number <= 1) {
    result = 1;
  } else if (number > 1) {
    result = parseInt(number) * computeFactorial(parseInt(number) - 1);
  }

  return result;
}

console.log(computeFactorial(args[2]));
