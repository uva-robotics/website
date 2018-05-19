


particlesJS.load('particles-js', '/static/assets/particles.json', function() {
  console.log('particles.js loaded - callback');
});

var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
  socket.emit('connected', {data: 'Still connected'});
});

socket.on('pong', function() {
  // socket.emit('ping', {data: 'Still connected'});
});


socket.on('update', function(data) {
  update(JSON.parse(data));
});


function update(data) {
  $("#version").text(data.version);
  $("#time").text(data.time);
}



$(document).ready(function(){
  var typed = new Typed('#typed', {
    strings: ['Hi there!', 'Welcome to the website of the UvA Intelligent Robotics Lab'],
    stringsElement: null,
    typeSpeed: 10,
    fadeOut: true,
    fadeOutClass: 'typed-fade-out',
    fadeOutDelay: 500,
  });
  console.log("TYPED");
});
