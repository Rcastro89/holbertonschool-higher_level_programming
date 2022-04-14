#!/usr/bin/node

$(document).ready(function () {
  $('#toggle_header').click(function () {
    if ($('header').hasClass('red') === true) {
      $('header').addClass('green');
      $('header').removeClass('red');
    } else {
      $('header').addClass('red');
      $('header').removeClass('green');
    }
  });
});
