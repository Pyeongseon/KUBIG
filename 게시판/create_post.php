<?php
require_once __DIR__ . '/includes/config.php';
require_once __DIR__ . '/includes/functions.php';

// 폼이 제출되었는지 확인
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // 폼 데이터 가져오기
    $title = $_POST['title'];
    $content = $_POST['content'];

    // 게시글 추가
    createPost($conn, $title, $content);

    // 목록 페이지로 리다이렉트
    header("Location: index.php");
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>새 게시글 작성</title>
</head>
<body>
    <h1>새 게시글 작성</h1>
    <form action="create_post.php" method="post">
        <div>
            <label for="title">제목:</label>
            <input type="text" id="title" name="title" required>
        </div>
        <div>
            <label for="content">내용:</label>
            <textarea id="content" name="content" required></textarea>
        </div>
        <button type="submit">게시글 작성</button>
    </form>
    <a href="index.php">목록으로 돌아가기</a>
</body>
</html>
