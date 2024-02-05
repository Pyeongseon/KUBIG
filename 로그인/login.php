<?php
// 사용자 이름과 비밀번호 정의 -> 데이터베이스에서 정보 검색
$valid_username = "admin";
$valid_password = "password";

// GET 요청으로 전송된 사용자 이름과 비밀번호를 가져옴
$username = $_POST['username'];
$password = $_POST['password'];

// 사용자 이름과 비밀번호가 유효한지 검증
if ($username === $valid_username && $password === $valid_password) {
    // 로그인 성공: success.php로 리디렉션
    header("Location: success.php");
    exit();
} else {
    // 로그인 실패: error.php로 리디렉션
    header("Location: error.php");
    exit();
}
?>
