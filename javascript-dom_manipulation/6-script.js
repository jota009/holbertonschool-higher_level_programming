const characterDiv = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`Network response was not ok (status: ${response.status})`);
    }
    return response.json();
  })
  .then(data => {
    characterDiv.textContent = data.name;
  })
  .catch(error => {
  console.error('Fetch error:', error);
  });

