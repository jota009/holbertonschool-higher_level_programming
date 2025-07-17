const addItemBtn = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

addItemBtn.addEventListener('click', () => {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  list.appendChild(newLi);
});
