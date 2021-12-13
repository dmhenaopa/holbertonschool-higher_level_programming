#!/usr/bin/node
const args = process.argv;

switch (args[2]) {
  case undefined:
    console.log('No argument');
    break;
  default:
    console.log(args[2]);
    break;
}
