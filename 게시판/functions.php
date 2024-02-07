<?php
require_once 'config.php'; // 데이터베이스 설정 불러오기

// 모든 게시글을 가져오는 함수
function getAllPosts($conn) {
    $sql = "SELECT * FROM posts ORDER BY created_at DESC";
    $result = $conn->query($sql);
    return $result;
}

// 특정 게시글을 ID로 가져오는 함수
function getPostById($conn, $id) {
    $stmt = $conn->prepare("SELECT * FROM posts WHERE id = ?");
    $stmt->bind_param("i", $id);
    $stmt->execute();
    $result = $stmt->get_result();
    return $result->fetch_assoc(); // 한 개의 게시글 반환
}

// 새 게시글을 추가하는 함수
function createPost($conn, $title, $content) {
    $stmt = $conn->prepare("INSERT INTO posts (title, content, created_at) VALUES (?, ?, NOW())");
    $stmt->bind_param("ss", $title, $content);
    $stmt->execute();
}
?>
