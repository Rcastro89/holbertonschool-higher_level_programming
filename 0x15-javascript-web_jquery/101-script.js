#!/usr/bin/node

$(document).ready(function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
  $('#clear_list').click(function () {
    $('li').remove();
  });
  $('#remove_item').click(function () {
    $('li:last').remove();
  });
});
