#!/usr/bin/node

$(document).ready(function () {
  $('#btn_translate').click(function () {
    let url = 'https://www.fourtonfish.com/hellosalut/?lang=';
    const lenguaje = $('#language_code').val();
    url = url + lenguaje;
    $.get(url, function (objetos) {
      $('#hello').text(objetos.hello);
    });
  });
});
