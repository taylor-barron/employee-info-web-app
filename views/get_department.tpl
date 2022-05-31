<html><head>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
</head>
<body style="width: 80%; margin: 0 auto;" >

  <nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">Our Website</a>
    </div>
    <div>
       <ul class="nav navbar-nav">
           <li class="active"><a href="/">Home</a></li>
           <li><a href="/getDepartment">View by Department</a></li>
           <li><a href="/editHours">Edit Employee Data</a></li>
       </ul>
    </div>
  </div>
  </nav> <!-- end nav-bar -->
  <h3>WXYZ Corp</h3>
  <h2>Get Payroll by Department</h2><br>
  <form action="/getDepartment" method="post">
    Select Department <select name="dept" id="dept">
        <option value="" disabled selected hidden>Select Department:</option>
        <option value="advertising">Advertising</option>
        <option value="environment">Environment</option>
        <option value="maintenance">Maintenance</option>
        <option value="shipping">Shipping</option>
    </select>
    <input value="Submit" type="submit" />
  </form>
  <br><br><p>We know what we're doing</p>
</body>
</html>