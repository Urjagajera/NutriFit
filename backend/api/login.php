<?php
include "../config/db.php";
$data = json_decode(file_get_contents("php://input"), true);

$email = $data['email'];
$pass = $data['password'];

$q = $conn->prepare("SELECT * FROM users WHERE email=?");
$q->bind_param("s", $email);
$q->execute();
$res = $q->get_result()->fetch_assoc();

if ($res && password_verify($pass, $res['password'])) {
  echo json_encode(["status"=>"success","user_id"=>$res['id']]);
} else {
  echo json_encode(["status"=>"fail"]);
}
?>
