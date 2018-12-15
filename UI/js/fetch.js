const registerUser = () => {
    fetch('https://ireporti.herokuapp.com/api/v2/auth/signup/', {
      method: 'POST',
      body: JSON.stringify({
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value
      }),
      headers: {
        'Content-type': 'application/json;'
      }
      })
      .then(response => response.json())
      .then(registerData => {
        if(registerData.message === "User created successfully"){
          window.location.href = "./login.html";
        }else{
            document.getElementById('error').innerHTML = registerData.message;
        }
      })
  }