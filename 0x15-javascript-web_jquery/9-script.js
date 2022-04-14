#!/usr/bin/node

$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, function (objetos) {
    $('#hello').text(objetos.hello);
  });
});
