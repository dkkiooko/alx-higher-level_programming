const $ = window.$;
$(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (json) {
    for (const movie of json.results) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    }
  });
});
