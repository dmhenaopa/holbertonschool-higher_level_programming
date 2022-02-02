#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const argumentsArray = process.argv;

const url = argumentsArray[2];
const file = argumentsArray[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    if (response && response.statusCode === 200) {
      const content = body;
      try {
        fs.writeFileSync(file, content, 'utf8');
      } catch (error) {
        console.error(error);
      }
    }
  }
});
