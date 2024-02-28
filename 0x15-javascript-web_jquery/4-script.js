#!/usr/bin/node
$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('red') === true) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
