$(document).ready(function() {

    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      method: 'GET',
      dataType: 'json',
      success: function(response) {
  
        if (response && response.results) {
            response.results.forEach(function(movie) {
                $('UL#list_movies').append('<li>' + movie.title+ '</li>')
            });
        }
      },
      error: function(xhr, status, error) {
        console.error('Error: ', status, error);
      }
    });
  });