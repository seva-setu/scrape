<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Seva setu</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <!--<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>-->
    <title>Seva setu</title>
    <style>
      .content-row:hover {
        background: #F5F5F5;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="jumbotron">
        <div class="row">
          <div class="col-md-4">
            <a href="http://sevasetu.org/" target="_blank">
            <img src="http://sevasetu.org/disability_care/img/logo.jpg" width="75" height="100"></a>
          </div>
          <div class="col-md-7">
            <h1>Seva Setu</h1>
          </div>
          <div class="col-md-1">
            <h4 class="centerify">
              <a class="nav-link" href="http://sevasetu.org/contribute-now/" target="_blank">Donate</a>
            </h4>
            <h4 class="centerify">
              <a class="nav-link" href="http://sevasetu.org/" target="_blank">About Us</a>
            </h4>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <form>
            <div class="input-group">
              <input type="text" class="form-control search-text" placeholder="Search this page...">
              <div class="input-group-btn">
                <button class="btn btn-default" type="submit">
                  <i class="glyphicon glyphicon-search"></i>
                </button>
              </div>
            </div>
          </form>
        </div>
        <div class="col-md-8 text-right">
          <a href="localhost:8080/sample_output_format.xlsx"><button type="button" class="btn btn-primary">Download</button></a>

        </div>
      </div>
      <h2>List of government schemes in India</h2>
      <h5>
        <div class="alert alert-success">
          The ministries of the Government of India have come up with various usefull schemes from time to time. These schemes could be either Central, state specific or joint collaboration between the Centre and the states. They are detailed below:
        </div>
      </h5>
      <table class="table table-bordered">
        <thead>
          <tr class="warning">
            <th>#</th>
            <th>Name of scheme</th> 
            <th>whether state/central scheme</th>
            <th>Department(Education,health,....)</th>
            <th>Brief description</th> 
            <th>Eligibility criteria for beneficiary</th>
            <th>Documents Required</th>
            <th>Benefits provided</th>
          </tr>
      </thead>
      <tbody class="table-content"></tbody>
    </table>
  </div>  

  <?php
    error_reporting(E_ALL);
    ini_set('display_errors', TRUE);
    ini_set('display_startup_errors', TRUE);
    
    require('excel_reader2.php');
    require('SpreadsheetReader.php');

    $Reader = new SpreadsheetReader('sample_output_format.xlsx');
    $data = array();
    
    foreach($Reader as $Row)
        {
            array_push($data, $Row);
        }

    $data = array_slice($data, 1, -1);
  ?>

  <script>
  
    const data = <?php echo json_encode($data); ?>;

    const table = document.getElementsByClassName('table-content')[0],
          searchText = document.getElementsByClassName('search-text')[0];

    data.map(el => {
      const row = table.insertRow(-1);
      row.classList.add('content-row');

      const sNo = row.insertCell(0),
            name = row.insertCell(1),
            scheme = row.insertCell(2),
            department = row.insertCell(3),
            description = row.insertCell(4),
            eligibility = row.insertCell(5),
            docs = row.insertCell(6),
            benifits = row.insertCell(7);

      sNo.innerHTML = el[0];
      name.innerHTML = el[1];
      scheme.innerHTML = el[2];
      department.innerHTML = el[3];
      description.innerHTML = el[4];
      eligibility.innerHTML = el[5];
      docs.innerHTML = el[6];
      benifits.innerHTML = el[7];
    });

    searchText.addEventListener('keyup', function($e) {
      let cell;

      const filter = this.value.toLowerCase();
      const rows = document.getElementsByClassName('content-row');

      for(let i=0; i<rows.length; ++i) {
        cell = rows[i].getElementsByTagName("td")[1];
        if (cell) {
          if (cell.innerHTML.toLowerCase().indexOf(filter) > -1) {
            rows[i].style.display = "";
          } else {
            rows[i].style.display = "none";
          }
        }
      }
    });
  </script>
</body>
</html>
