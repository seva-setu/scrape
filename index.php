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
    <div class="container-fluid" style="background-color:#eceff1; margin-left: 0.5em;margin-right: 0.5em;">
     <!-- <div class="jumbotron">-->
        <div class="row">
          <div class="col-md-5">
            <a href="http://sevasetu.org/" target="_blank">
            <img src="http://sevasetu.org/disability_care/img/logo.jpg" width="75" height="100" style="postion: relative;left:7%;margin-top: 0.5em;margin-bottom: 0.5em;"></a>
          </div>
          <div class="col-md-6">
            <h1 style="position: relative; margin-top: 3%;font-weight: bold;">Seva Setu</h1>
          </div>
          <div class="col-md-1">
            <br>
            <h4 class="centerify">
              <a class="nav-link" href="http://sevasetu.org/contribute-now/" target="_blank" style="margin-top: 2em;">Donate</a>
            </h4>
            <h4 class="centerify">
              <a class="nav-link" href="http://sevasetu.org/" target="_blank" style="margin-top: .5em;">About Us</a>
            </h4>
          </div>
        </div>
     <!-- </div>-->
    </div>
    <div class="container-fluid" style="margin-top: 0.5em;">
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
          <button type="button" class="btn btn-primary">Download</button>
        </div>
      </div>
      <h2>List of government schemes in India</h2>
      <h5>
        <div class="alert alert-success">
          The ministries of the Government of India have come up with various usefull schemes from time to time. These schemes could be either Central, state specific or joint collaboration between the Centre and the states. They are detailed below:
        </div>
      </h5>
      <table class="table table-bordered" id="myTable">
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
      <div class="pagination">
      </div>
    </div>  
    <?php
      function get_all_counts($data){
        for($i=0; $i<count($data); $i++)
          if($data[$i][2] == '' and $data[$i][3] == '')
            break;
        return ($i+1);
      }
      
      function get_counts($data, $index, $max_count){
        $count    = 0;
        for($i=0; $i<$max_count; $i++){
          if($data[$i][$index] != '')
            $count += 1;
        }
        return $count;
      }
      
      function get_csv_content($spreadsheet_url){
        //if(!ini_set('default_socket_timeout', 15)) 
        echo "<!-- unable to change socket timeout -->";
        if (($handle = fopen($spreadsheet_url, "r")) !== FALSE) {
          while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            $spreadsheet_data[] = $data;
          }
          fclose($handle);
          return $spreadsheet_data;
        }
      }
      
      function validate_data($data){
        return true;
      }

      $dataURI = "https://docs.google.com/spreadsheets/d/1nbx2ENfcXSXe1aUB4n4LsMsj0CMVWtrUadG7MI-Fz9I/pub?gid=407297767&single=true&output=csv";
      $data = get_csv_content($dataURI);
      $is_valid = validate_data($data);
    
      $data_to_publish = array(1014, 817, 93, 6);
      
      if($is_valid){
        $all_count = get_all_counts($data);
        
        $data_to_publish[0] = $all_count;
        $data_to_publish[1] = get_counts($data, 4, $all_count);
        $data_to_publish[2] = get_counts($data, 5, $all_count);
        //$data_to_publish[3] = get_counts($data, 6, $all_count);
      }
    ?>
    <script>
      const searchBox = document.getElementsByClassName('search-text')[0],
            tableBody = document.getElementsByClassName('table-content')[0],
            data = getFilteredData(<?php echo json_encode($data) ?>);

      data.map(el => {
        const row = tableBody.insertRow(-1);

        row.classList.add('content-row');
              
        const serial = row.insertCell(0),
              scheme = row.insertCell(1),
              stateOrCentral = row.insertCell(2),
              dept = row.insertCell(3),
              desc = row.insertCell(4),
              eligiblity = row.insertCell(5),
              docs = row.insertCell(6),
              benifits = row.insertCell(7);
        
        serial.innerHTML = el[0];
        scheme.innerHTML = el[1];
        stateOrCentral.innerHTML = el[2];
        dept.innerHTML = el[3];
        desc.innerHTML = el[4];
        eligiblity.innerHTML = el[5];
        docs.innerHTML = el[6];
        benifits.innerHTML = el[7];
      });

      searchBox.addEventListener('keyup', function($e) {
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

      function download_table_info() {
        const url = decodeURIComponent("<?php echo rawurlencode($dataURI); ?>");

        window.location = url;
      }

      function getFilteredData(dataArray) {
        dataArray = dataArray.slice(2);

        return dataArray.map(e => e.slice(1));
      }
      
      $('button').click(function() {
        download_table_info();
      });
      var $table = document.getElementById("myTable"),
          $n = 20,
          $rowCount = $table.rows.length,
          $firstRow = $table.rows[0].firstElementChild.tagName,
          $hasHead = ($firstRow === "TH"),
          $tr = [],
          $i,$ii,$j = ($hasHead)?1:0,
          $th = ($hasHead?$table.rows[(0)].outerHTML:"");
      var $pageCount = Math.ceil($rowCount / $n);
      
      if ($pageCount > 1) {
        for ($i = $j,$ii = 0; $i < $rowCount; $i++, $ii++) {
          $tr[$ii] = $table.rows[$i].outerHTML;
        }
        $table.insertAdjacentHTML("afterend","<div id='buttons'></div");
        sort(1);
      }

      function sort($p) {
        var $rows = $th,$s = (($n * $p)-$n);
        for ($i = $s; $i < ($s+$n) && $i < $tr.length; $i++) {
          $rows += $tr[$i];
        }

        $table.innerHTML = $rows;

        document.getElementById("buttons").innerHTML = pageButtons($pageCount,$p);
        document.getElementById("id"+$p).setAttribute("class","active");
      }

      function pageButtons($pCount,$cur) {
        var	$prevDis = ($cur == 1)?"disabled":"",
            $nextDis = ($cur == $pCount)?"disabled":"",
            $buttons = "<input type='button' value='&lt;&lt; Prev' onclick='sort("+($cur - 1)+")' "+$prevDis+">";

        for ($i=1; $i<$pCount;$i++) {
          $buttons += "<input type='button' id='id"+$i+"'value='"+$i+"' onclick='sort("+$i+")'>";
        }

        $buttons += "<input type='button' value='Next &gt;&gt;' onclick='sort("+($cur + 1)+")' "+$nextDis+">";

        return $buttons;
      }
    </script>
  </body>
</html>
