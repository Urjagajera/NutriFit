<?php
$conn = new mysqli("localhost", "root", "", "nutrifit");
if ($conn->connect_error) {
  die("DB Error");
}
?>
