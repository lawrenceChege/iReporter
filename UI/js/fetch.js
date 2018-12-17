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
        let user = sessionStorage.setItem("user",  document.getElementById('username').value);
        let token = sessionStorage.setItem("token", registerData.data[0].token);
        alert(registerData.message)
        console.log(user, token)
        window.location = "profile.html";
      } else {
        alert(registerData.error)
        alert(registerData.message)
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
        let user = document.getElementById('username').value;
        sessionStorage.setItem('user', user);
        let token = loginData.data[0].token;
        sessionStorage.setItem('token', token)
        alert(loginData.message)
        window.location = "profile.html";
      } else {
        document.getElementById('error').innerHTML = loginData.error;
        alert(loginData.error)
        alert(loginData.message)
      }
    })
}
function helloUser(){
  let user = sessionStorage.getItem('user');
  document.getElementById('user').innerHTML = user;
  console.log(user)
}

const getAllIncidents = () => {
  fetch('https://ireporti.herokuapp.com/api/v2/incidents/', {
    headers: {
      'Content-type' : 'application/json;'
    }
  })
  .then(response => response.json())
  .then(incidentsData => {
    if(incidentsData.message === "All incidents found successfully"){
      let incidents = incidentsData.data[0].RedFlags;
      let incidentslist = document.getElementById('incident-list');
      incidentslist.innerHTML = '';
      for (var i=0; i < incidents.length; i++){
        let title = incidents[i].title;
        let status = incidents[i].status;
        let record_type = incidents[i].record_type;
        let created_on = incidents[i].createdon;
        let modifiedOn = incidents[i].modifiedon
        let comment = incidents[i].comment;

        incidentslist.innerHTML += '<li class="flag-list-item">' +
                                  '<a href="#" id="id1">' +
                                  '<h4 class="flag-title"> Title:' + title + '</h4>' +
                                  '<strong>Status: '+status+'</strong>'+
                                  '<strong> Type: ' +record_type+ '</strong><br>'+
                                  '<small>CreatedOn:'+ created_on +'</small> &nbsp;' +
                                  '<small>modifiedOn:'+ modifiedOn + '</small> &nbsp;' +
                                  '<a href="editrecord.html"><i class="far fa-edit"></i></a>&nbsp;' +
                                  '<a href="#"><i class="fas fa-trash"></i></a>&nbsp;'+
                                  '<a href="editrecord.html"><i class="fas fa-image"></i></a>&nbsp;' +
                                  '<a href="editrecord.html"><i class="fas fa-video"></i></a>'+
                                  '</a>'+
                                  '</li>'
      }
      alert(incidentsData.message)
    }else{
        document.getElementById('message').innerHTML = incidentsData.error;
        alert(incidentsData.message)
        alert(incidentsData.error)
    }
  })
}

function postIncident() {
  let token = sessionStorage.getItem('token')
  t = token
  fetch('https://ireporti.herokuapp.com/api/v2/incidents/', {
    method: 'POST',
    body: JSON.stringify({
      record_type: document.getElementById('record_type').value,
      title: document.getElementById('title').value,
      comment: document.getElementById('comment').value,
      images: document.getElementById('image').value,
      video: document.getElementById('video').value,
      location: document.getElementById('location').value
    }),
    headers: {
      'Authorization': t,
      'Content-type': 'application/json;'
    }
  })
    .then(response => response.json())
    .then(incidentData => {
      console.log(t)
      if (incidentData.message == "Created incident successfully!") {
        alert(incidentData.message)
        getAllIncidents();  openPage('allflags', this, '#f88282');
      }else{
        alert(incidentData.error)
        alert(incidentData.message)
      }
    })
}
