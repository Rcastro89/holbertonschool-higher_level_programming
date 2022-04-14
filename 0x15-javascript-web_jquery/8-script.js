#!/usr/bin/node

$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (objetos) {
    $(objetos.results).each(function (index, conte) {
      $('#list_movies').append('<li>' + index + ' ' + conte.title + '</li>');
    });
  });
});
