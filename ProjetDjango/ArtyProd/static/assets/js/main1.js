const form = document.querySelector('form');
const usernameInput = document.querySelector('#username');
const passwordInput = document.querySelector('#password');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const username = formData.get('username');
  const password = formData.get('password');

  // TODO: add validation here
  // ...

  const xhr = new XMLHttpRequest();

  xhr.open('POST', '/login/');
  xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

  xhr.onload = function() {
    if (xhr.status === 200) {
      const response = JSON.parse(xhr.responseText);
      if (response.success) {
        window.location.href = '/';
      } else {
        const messages = document.querySelector('.messages');
        const li = document.createElement('li');
        li.textContent = response.message;
        li.classList.add('error');
        messages.appendChild(li);
      }
    } else {
      console.log('Error: ' + xhr.status);
    }
  }

  xhr.send(`username=${username}&password=${password}`);
});
