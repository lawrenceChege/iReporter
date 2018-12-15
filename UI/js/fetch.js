const registerUser = () => {
  fetch('https://ireporti.herokuapp.com/api/v2/auth/signup/', {
    method: 'POST',
    body: JSON.stringify({
      username: document.getElementById('username').value,
      email: document.getElementById('email').value,
      phoneNumber: document.getElementById('phoneNumber').value,
      password: document.getElementById('password').value
    }),
    headers: {
      'Content-type': 'application/json;'
    }
  })
    .then(response => response.json())
    .then(registerData => {
      console.log(registerData)
      if (registerData.message == "User created Succesfully.") {
        window.location = "profile.html";
        sessionStorage.setItem("token", registerData.data[0].token);
        document.getElementById('message').innerHTML = registerData.message;
      } else {
        document.getElementById('error').innerHTML = registerData.error;
      }
    })
}

const loginUser = () => {
  fetch('https://ireporti.herokuapp.com/api/v2/auth/login/', {
    method: 'POST',
    body: JSON.stringify({
      username: document.getElementById('username').value,
      password: document.getElementById('password').value
    }),
    headers: {
      'Content-type': 'application/json;'
    }
  })
    .then(response => response.json())
    .then(loginData => {
      console.log(loginData)
      if (loginData.message == "successful") {
        window.location = "profile.html";
        sessionStorage.setItem("token", loginData.data[0].token);
        document.getElementById('message').innerHTML = loginData.message;
      } else {
        document.getElementById('error').innerHTML = loginData.error;
      }
    })
} 
