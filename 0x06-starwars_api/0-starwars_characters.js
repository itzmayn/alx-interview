#!/usr/bin/node

const request = require('request');

const fetchCharacterName = async (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

const getMovieCharacters = async (movieId) => {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

  try {
    const movieData = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    const characters = movieData.characters;

    for (const characterUrl of characters) {
      try {
        const characterName = await fetchCharacterName(characterUrl);
        console.log(characterName);
      } catch (error) {
        console.error(`Error fetching character data: ${error}`);
      }
    }
  } catch (error) {
    console.error(`Error fetching movie data: ${error}`);
  }
};

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
