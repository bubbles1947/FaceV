<?php
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}
$email = $_SESSION['email'];

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
    <link rel="stylesheet" href="profile.css">
</head>
<body>

<div class="profile-container">
    <h2>User Profile</h2>
    <p><strong>Email:</strong> <?php echo htmlspecialchars($email); ?></p>
    
    <a href="logout.php" class="logout-button">Logout</a>
</div>

</body>
</html>
