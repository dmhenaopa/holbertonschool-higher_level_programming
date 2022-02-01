#!/usr/bin/node
const https = require('https');
const argumentsArray = process.argv;

const url = argumentsArray[2];

const req = https.request(url, res => {
  console.log(`code: ${res.statusCode}`);
});
req.on('error', error => {
  console.error(error);
});
req.end();
