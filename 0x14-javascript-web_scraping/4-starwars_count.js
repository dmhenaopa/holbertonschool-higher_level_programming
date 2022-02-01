#!/usr/bin/node
const request = require('request');
const argumentsArray = process.argv;

const url = argumentsArray[2];
let counter = 0;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    if (response && response.statusCode === 200) {
      const information = JSON.parse(body);
      for (const [key, value] of Object.entries(information)) {
        if (key === 'results') {
          value.forEach(function (element, index, array) {
            const characters = element.characters;
            for (const [, valuechar] of Object.entries(characters)) {
              if (valuechar.includes('18')) {
                counter++;
              }
            }
          });
          console.log(counter);
        }
      }
    } else {
      console.log('code:', response && response.statusCode);
    }
  }
});
