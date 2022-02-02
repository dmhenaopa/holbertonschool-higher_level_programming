#!/usr/bin/node
const request = require('request');
const argumentsArray = process.argv;

const url = argumentsArray[2];
const object = {};

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    if (response && response.statusCode === 200) {
      const information = JSON.parse(body);
      for (let i = 0; i < information.length; i++) {
        object[information[i].userId] = 0;
      }

      for (let i = 0; i < information.length; i++) {
        if (information[i].completed) {
          if (object[information[i].userId] === undefined) {
            object[information[i].userId] = 1;
          } else {
            object[information[i].userId]++;
          }
        }
      }
      console.log(object);
    } else {
      console.log('code:', response && response.statusCode);
    }
  }
});
