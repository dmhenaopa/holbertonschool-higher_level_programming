$('DIV#toggle_header').addClass('red');
$('DIV#toggle_header').click(function () {
  if ($('DIV#toggle_header').hasClass('red')) {
    $('DIV#toggle_header').removeClass('red');
    $('DIV#toggle_header').addClass('green');
  } else if ($('DIV#toggle_header').hasClass('green')) {
    $('DIV#toggle_header').removeClass('green');
    $('DIV#toggle_header').addClass('red');
  }
});
