#!/usr/bin/node

$(document).ready(function () {
  function ejecutar () {
    let url = 'https://www.fourtonfish.com/hellosalut/?lang=';
    const lenguaje = $('#language_code').val();
    url = url + lenguaje;
    $.get(url, function (objetos) {
      $('#hello').text(objetos.hello);
    });
  }
  $('#btn_translate').click(function () {
    ejecutar();
  });
  $('#language_code').keyup(function (e) {
    if (e.keyCode === 13) {
      ejecutar();
    }
  });
});
