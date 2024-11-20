<?php
// Start the session to access session variables
session_start();

// Prevent caching of this page
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Face Verification</title>
    <link rel="stylesheet" href="face_Vupdated.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>

    <div class="header">
        <div class="container">
            <div class="navbar">
                <div class="logo">
                    <!-- Logo here -->
                </div>
                <div class="graphy-logo">
                    <h1>Face_<span style="color: aquamarine;">V</span></h1>
                </div>

                <ul class="navcolor">
                    <li><a href="face_Vupdated.php">Home</a></li>
                    <li class="dropdown">
                        <a class="dropbtn" href="#">Features</a>
                        <div class="dropdown-content">
                            <?php if (isset($_SESSION['user_id'])): ?>
                                <a href="subscription1.html">Real-Time Verification</a>
                            <?php else: ?>
                                <a href="login.php">Real-Time Verification</a>
                            <?php endif; ?>
                            <a href="features1.html">Accuracy & Performance</a>
                        </div>
                    </li>
                    <li><a href="payment.html">Subscriptions</a></li>
                  <!--  <li class="dropdown">
                        <a class="dropbtn" href="#">Subscription</a>
                        <div class="dropdown-content">
                            <a href="#">Monthly Package</a>
                            <a href="#">Yearly Package</a>
                        </div>
                    </li>
                    <li class="dropdown">
                        <a class="dropbtn" href="#">Support</a>
                    </li>-->
                    <li><a href="about.html">About Us</a></li>

                    <li class="dropdown">
                        <a class="dropbtn" href="#">Accounts</a>
                        <div class="dropdown-content">
                            <?php if (isset($_SESSION['user_id'])): ?>
                                <a href="profile.php">Profile</a>
                               <!-- <a href="logout.php">Logout</a> -->
                            <?php else: ?>
                                <a href="login.php">Login</a>
                            <?php endif; ?>
                        </div>
                    </li>
                    <li class="accLogo"><i class="fas fa-user-circle"></i></li>
                </ul>
            </div>

            <div class="contents">
                <h1>Empowering Identity with Advanced Recognition</h1>
            </div>

            <div class="content2">
                <p>"This project works for accurate and secure face verification technology for seamless identity authentication and fraud prevention."</p>
                <div>
                    <!-- <button class="button">Explore Us</button> -->
                </div>
            </div>
        </div>
    </div>

    <main>

        <div class="testimonial">
            <div class="small-container">
                <h1>Features</h1>
                <div class="row">

                    <div class="col-3">
                        <img src="PicforFeatures/5064259.jpg">
                        <h3>Real-Time Verification</h3>
                        <i class="fas fa-quote-left"></i>
                        <p>Instantly verify a user's identity through live video or image comparison.</p>
                        <div class="logoo">
                            <i class="fa-solid fa-circle-check"></i>
                        </div>
                    </div>

                    <div class="col-3">
                        <img src="PicforFeatures/3123033.jpg">
                        <h3>User-Friendly Dashboard</h3>
                        <i class="fas fa-quote-left"></i>
                        <p>A simple dashboard to manage verifications, view logs, and track user data.</p>
                        <div class="logoo">
                            <i class="fa-solid fa-table-columns"></i>
                        </div>
                    </div>

                    <div class="col-3">
                        <img src="PicforFeatures/3d-internet-secuirty-badge.jpg">
                        <h3>Secure Data Encription</h3>
                        <i class="fas fa-quote-left"></i>
                        <p>End-to-end encryption of all facial data to ensure privacy and security.</p>
                        <div class="logoo">
                            <i class="fa-solid fa-lock"></i>
                        </div>
                    </div>

                </div>
            </div>
        </div>

        <div class="popular">
            <div class="topic">
                <h1>Visit Our Page</h1>
                <p>You can visit our page and choose services that you need.<br>
                We are always open.</p>
                <div>
                    <button class="button2">Visit Here</button>
                </div>
            </div>
        </div>

    </main>

    <footer>
        <p>&copy; 2024 Face Recognition NSU</p>
    </footer>

</body>
</html>
