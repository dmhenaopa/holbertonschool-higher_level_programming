#!/usr/bin/node
const request = require('request');
const argumentsArray = process.argv;

const movieID = argumentsArray[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    if (response && response.statusCode === 200) {
      const information = JSON.parse(body);
      const characters = information.characters;

      characters.sort();
      for (let i = 0; i < characters.length; i++) {
        request(characters[i], function (error, response, body) {
          if (error) {
            console.error('error:', error);
          } else {
            if (response && response.statusCode === 200) {
              const informationCharacter = JSON.parse(body);
              console.log(informationCharacter.name);
            }
          }
        });
      }
    }
  }
});
