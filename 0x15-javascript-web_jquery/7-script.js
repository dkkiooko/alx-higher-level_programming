const $ = window.$;
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (json) {
  $('DIV#character').html(json.name );
});
