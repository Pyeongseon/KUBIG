<?php
// 성공 메세지

$host  = $_SERVER['HTTP_HOST'];
$uri   = rtrim(dirname($_SERVER['PHP_SELF']), '/\\');
$loginPage = 'index_login.php'; // 로그인 페이지 파일 이름
$loginUrl  = 'http://' . $host . $uri . '/' . $loginPage;

echo "Welcome! but this site has NOT data :( just Enjoy!<br>
<strong>Warning</strong>: Undefined array key \"user\" in <a href='$loginUrl'>$loginUrl</a>";
?>
