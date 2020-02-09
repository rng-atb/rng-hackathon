"""
	Create an HTML page to report the data

"""

html = """
<html>
<head>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
	<script src="js/aos.js"></script>
	<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
	<script src="http://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>

</head>

<body>
<br>
      <center>
      <form action="gen_data.php" method="POST">
      <!-- <div class="GenerateData"> -->
      <label for="interestLabel"><b>Interest</b></label>
      <select name="interestType">
                <option value="Gaming">Gaming</option>
                <option value="Learning">Learning</option>
                <option value="Wedding">Wedding</option>
                <option value="Outdoors">Outdoors</option>
                <option value="Travel">Travel</option>
        </select>
      <label for="weightLabel"><b>Weight</b></label>
      <input type="text" placeholder="..." name="txtWeight" maxlength="16" required>

    <input type="submit" class="btn btn-primary btn-lg" name="commit" value="Generate">
    </center>
  </form>
	<table class="table">
	  <thead class="thead-dark">
		<tr>
		  <th scope="col">Name</th>
		  <th scope="col">Interest</th>
		  <th scope="col">Weight</th>
		</tr>
	  </thead>
"""

write_row = """
	  <tbody>
		<tr>
		  <td>{_name}</td>
		  <td>{_target}</td>
		  <td>{_interest}</td>
		</tr>
	  </tbody>
"""

html_close = """
	</table>
</body>
</html>
"""

def writeToFile(value):
	with open("/var/www/html/index.php", "a") as f:
		f.write(value)

def beginHTML():
	writeToFile(html)

def createTable(name, target, interest):
	report = write_row.format(_name=name, _target=target, _interest=interest)
	writeToFile(report)

def closeHTML():
	writeToFile(html_close)
