<?php
// 데이터베이스 연결 설정
$host = 'localhost';  // 데이터베이스 호스트
$dbUser = 'root';     // 데이터베이스 사용자 이름
$dbPass = '';         // 데이터베이스 비밀번호
$dbName = 'simple_board'; // 데이터베이스 이름

// MySQLi를 사용하여 데이터베이스에 연결
$conn = new mysqli($host, $dbUser, $dbPass, $dbName);

// 연결 에러 체크
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
