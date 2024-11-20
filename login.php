<?php
// login.php

session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Connect to MySQL
    $conn = new mysqli('localhost', 'root', '', 'persons');
    
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Get form data
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Prepare and execute the query to fetch user data
    $stmt = $conn->prepare("SELECT id, email, password FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();
    $stmt->bind_result($id, $db_email, $db_password);

    // Check if email exists and password matches
    if ($stmt->num_rows > 0) {
        $stmt->fetch();
        if (password_verify($password, $db_password)) {
            // Password is correct, start session and redirect
            $_SESSION['user_id'] = $id;
            $_SESSION['email'] = $db_email;
            header('Location:face_Vupdated.php');
            exit();
        } else {
            $error = "Incorrect password!";
        }
    } else {
        $error = "No user found with that email.";
    }

    $stmt->close();
    $conn->close();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="login.css">
</head>
<body>

<div class="form-container">
    <h2>Login</h2>
    <?php if (isset($error)) { echo "<p class='error'>$error</p>"; } ?>
    <form method="POST" action="login.php">
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <a href="signup.php">Sign up here</a></p>
</div>

</body>
</html>
