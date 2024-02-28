#!/usr/bin/node
const lang = $('INPUT#language_code').val();
const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;

$('INPUT#btn_translate').click(function () {
  $.get(url, function (data) {
    $('DIV#hello').text(data);
  });
});

// $('INPUT#btn_translate').click(hello());
