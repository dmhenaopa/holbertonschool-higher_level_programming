#!/usr/bin/node
const args = process.argv;

if (args[2] === undefined || args[3] === undefined) {
  console.log(0);
} else {
  const newArray = [];
  for (let i = 2; i < args.length; i++) {
    newArray.push(args[i]);
  }
  newArray.sort();
  console.log(newArray[newArray.length - 2]);
}
