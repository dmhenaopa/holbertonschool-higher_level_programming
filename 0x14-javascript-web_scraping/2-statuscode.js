#!/usr/bin/node
const request = require('request');
const argumentsArray = process.argv;

const url = argumentsArray[2];
request(url, function (error, response) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
