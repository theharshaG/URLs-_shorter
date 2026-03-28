# URLs_shorter

## Overview
This project is a simple command-line URL Shortener built using Python. It allows users to convert long URLs into short codes and retrieve the original URLs using those codes. The application uses an in-memory dictionary to store mappings between short codes and long URLs.

## Features
Generate short URLs from long URLs
Retrieve original URLs using short codes
Display all stored URL mappings
Simple and interactive command-line interface

## Technologies Used
Python
Standard Libraries (random, string)
Dictionary data structure

## How to Run
Clone the repository:
git clone https://github.com/your-username/url-shortener.git
Navigate to the project directory:
cd url-shortener

Run the program:
python main.py

## How It Works
The program generates a random 5-character code using letters and digits.
Each generated code is mapped to a long URL and stored in a dictionary.
Users can retrieve the original URL by entering the corresponding short code.

The shortened URL format follows:
short.ly/<code>
Example:
# Input:
Enter long URL: https://www.example.com/page

# Output:
Short URL: short.ly/aB3dE

## Limitations
Data is not persistent (lost after program exits)
No validation for duplicate short codes
No URL format validation
No expiration or deletion of links

## Future Improvements
Add file or database storage for persistence
Implement collision handling for duplicate codes
Add URL validation
Build a web-based version using Flask
Add custom short codes

## Author
Harsha G 
Learning Python | Embedded Systems | IoT
