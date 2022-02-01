#!/usr/bin/node
const fs = require('fs');
const argumentsArray = process.argv;

const file = argumentsArray[2];
const content = argumentsArray[3];

try {
  fs.writeFileSync(file, content, 'utf8');
} catch (error) {
  console.error(error);
}
