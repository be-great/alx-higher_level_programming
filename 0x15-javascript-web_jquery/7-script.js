$(document).ready(function() {

  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function(response) {

      $('#character').text(response.name);

    },
    error: function(xhr, status, error) {
      console.error('Error: ', status, error);
    }
  });
});