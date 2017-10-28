<!doctype html>
<html lang="en">
  <head>
    <title>Krispy Papad | {{name}}</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="shortcut icon" href="../img/kp_favicon.ico">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">

    <script src="js/wow.min.js"></script>

    <script type="text/javascript">
        $(document).ready(function(){
          new WOW().init();
        })
    </script>

    <style type="text/css">
      .card-1 {
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
        transition: all 0.3s cubic-bezier(.25,.8,.25,1);
      }
      .overlay {
            position: absolute;
            display: block;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0,0,0,0.5);
            z-index: 998;
        }
        .card {
          box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
          transition: 0.3s;
          width: 40%;
          border-radius: 5px;
      }

      .card:hover {
          box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
      }

      /*img {
          border-radius: 5px 5px 0 0;
      }*/

      .card-container {
          padding: 5px 15px 5px 15px;
      }

    </style>
  </head>

  <body style="">
    <div class="container-fluid">
        <div class="row card-1" id="nav" style="display: block; height: 50px; background-color: #2e90cc; position: fixed; top: 0; left: 15px; right: 0; z-index: 999; width: 100%;">

            <div class="col-md-4"></div>
            <div class="col-md-4 text-center">
                <a href="#" style="text-decoration: none;"><img src="../img/kp-logo-dual.png" style="height: 40px; padding-top: 7px; padding-bottom: 0px;"></a>
            </div>
            <div class="col-md-4"></div>
        </div>

        <div class="row" style="margin-top: 50px; padding-left: 25px; padding-right: 25px;">

          <div class="col-lg-8 col-md-8 col-sm-12 col-xs-12" style="margin-top: 15px;">
            <div class="card" style="width: 100%;">
              <div class="">
                <img class="" src="../img/events/{{img}}" style="width: 100%; height: 250px;">
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" style="margin-top: 15px;">
              <div class="card" style="width: 100%;">
                <div class="card-container">
                  <h4><b>{{name}}</b></h4>
                  <h4>{{date}} | {{time}}</h4>
                  <h4><b>Venue :</b> {{venue}}</h4>
                  <h4><b>Price : </b>{{price}}</h4>
                  <h4><b>Organiser</b></h4>
                  <h4>{{organiser}}</h4>
                </div>
              </div>
          </div>


        </div>

        <div class="row" style="padding-top: 25px; padding-bottom: 50px; padding-left: 25px; padding-right: 25px;">
            <div class="col-lg-8 col-md-8 col-sm-12 col-xs-12" style="margin-top: 15px;">
                <div class="card" style="width: 100%;">
                  <div class="card-container">
                    <h4><b>Description</b></h4>
                    <p>{{description}}</p>
                    <h4><b>Speaker</b></h4>
                    % for item in speakers:
                      <div class="row">
                        <div class="col-md-4"></div>
                        <div class="col-md-4 text-center">
                          <img src="../img/speakers/{{item['img']}}" style="width: 100px;">
                          <h4>{{item['name']}}</h4>
                          <a href="//in.linkedin.com/in/surajjana" target="_blank">LinkedIn Profile</a>
                        </div>
                        <div class="col-md-4">
                        <!-- <h4>{{item['name']}}</h4>
                        <p>{{item['description']}}</p> -->
                        </div>
                      </div>
                    % end
                    

                    <!-- <div class="row">
                      <div class="col-md-2">
                        <img src="../img/speakers/suraj.png" style="width: 100px;">
                      </div>
                      <div class="col-md-10">
                      <h4>Suraj Jana</h4>
                      <p></p>
                      </div>
                    </div> -->
                    
                  </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" style="margin-top: 15px;">
                <div class="card" style="width: 100%;">
                  <div class="card-container">
                    <h4><b>Registrations starting soon</b></h4>
                  </div>
                </div>
            </div>
        </div>

        <div class="row" style="padding: 15px; background-color: #eee;">
            <div class="col-md-4">Copyrights 2017-2018, Hello Krispypapad LLP</div>
        </div>
    </div>
  </body>
</html>