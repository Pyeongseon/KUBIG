<?php
require_once __DIR__ . '/includes/config.php';
require_once __DIR__ . '/includes/functions.php';

// 모든 게시글 가져오기
$posts = getAllPosts($conn);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Board</title>
</head>
<body>
    <h1>게시판</h1>
    <a href="create_post.php">새 게시글 작성</a>
    <?php if ($posts->num_rows > 0): ?>
        <ul>
            <?php while($post = $posts->fetch_assoc()): ?>
                <li>
                    <a href="view_post.php?id=<?= $post['id'] ?>"><?= htmlspecialchars($post['title']) ?></a>
                </li>
            <?php endwhile; ?>
        </ul>
    <?php else: ?>
        <p>게시글이 없습니다.</p>
    <?php endif; ?>
</body>
</html>
