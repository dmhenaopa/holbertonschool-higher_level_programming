#!/usr/bin/node
const fs = require('fs');
const argumentsArray = process.argv;

try {
  const file = fs.readFileSync(argumentsArray[2], 'utf8');
  console.log(file);
} catch (error) {
  console.error(error);
}
