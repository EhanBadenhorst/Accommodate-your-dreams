<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $title = $_POST['title'];
    $price = $_POST['price'];
    $bedrooms = $_POST['bedrooms'];
    $bathrooms = $_POST['bathrooms'];
    $sqft = $_POST['sqft'];
    $location = $_POST['location'];

    // Handle image upload
    $image = $_FILES['image'];
    $imagePath = 'uploads/' . basename($image['name']);
    move_uploaded_file($image['tmp_name'], $imagePath);

    // Save data to a text file
    $data = "Title: $title\nPrice: R$price\nBedrooms: $bedrooms\nBathrooms: $bathrooms\nSquare Footage: $sqft sq ft\nLocation: $location\nImage: $imagePath\n\n";
    file_put_contents('listings.txt', $data, FILE_APPEND);
    
    echo "Listing saved successfully.";
}
?>