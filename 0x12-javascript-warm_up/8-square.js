#!/usr/bin/node
const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  let row = '';
  for (let i = 0; i < parseInt(args[2]); i++) {
    for (let j = 0; j < parseInt(args[2]); j++) {
      row += 'X';
    }
    console.log(row);
    row = '';
  }
}
