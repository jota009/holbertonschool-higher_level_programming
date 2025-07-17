const listMovies = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`Network response was not ok (status: ${response.status})`);
    }
    return response.json();
  })
  .then(data => {
    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      listMovies.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Fetch error:', error);
  });
