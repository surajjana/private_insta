route('/', 'home', function () {
  this.nav = '<p class="" style="float: left; font-size: 20px;">Logo</p><div style="float: right;"><a href="#/post" style="color: #fff;"><i class="fa fa-plus" style="font-size: 25px; margin-right: 25px;"></i></a><i class="fa fa-ellipsis-v" style="font-size: 25px;" id="menu" onclick="toggle_menu();"></i></div>';

  console.log('Root');

  fetch('http://ocl-data-server.herokuapp.com/read/5', {
    method: 'get'
  }).then(function(response) {
    console.log(response.text());
  }).catch(function(err) {
    // Error :(
  });
});
route('/post', 'post', function () {
  this.nav = '<a href="/#" style="color: #fff;"><i class="fa fa-arrow-left" style="float: left; font-size: 25px;"></i></a><p class="" style="float: right; font-size: 20px;">Post</p>';

  console.log('Post');
});
route('/test', 'test', function(){});
route('*', 'error404', function () {});