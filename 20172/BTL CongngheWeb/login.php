<!DOCTYPE html>
<html>
<head>
	<title>Login</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="dinhdang.css">
	<?php
		include "modul.php";
	?>
</head>
<body>
	<div id="cover">
		<form action="login.php" id="form_login" method="post">
			<caption>Login</caption>
			<div>
				<b>Username: </b><input type="text" name="username" placeholder="Username">
			</div>
			<div>
				<b>Password: </b><input type="text" name="password" placeholder="Password">
			</div>
			<div><input type="submit" name="Login" value="Login"></div>
			<div><form><input type="submit" name="Dangki" value="Create account"></form></div>
		</form>
	</div>
</body>
</html>