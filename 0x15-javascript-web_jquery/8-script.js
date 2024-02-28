#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  const movie = data.results;
  for (let i = 0; i <= movie.length; i++) {
    $('UL#list_movies').append('<li>' + movie[i].title + '</li>');
  }
});
