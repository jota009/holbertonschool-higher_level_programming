document.addEventListener('DOMContentLoaded', () => {
  const helloDiv = document.querySelector('#hello');
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      // Insert translated greeting
      helloDiv.textContent = data.hello;
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
});
