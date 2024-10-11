Flask Book Management Application
This is a simple Flask application that allows users to manage a collection of books. Users can add new books, list all books, filter by author or genre, and search for books by title or author.

#Features
 . Add a new book with title, author, and genre.
 . List all books with options to filter by author or genre.
 . Search for books by title or author.
 . User-friendly flash messages for feedback.
 
#Requirements
 . Python 3.x
 . Flask
 
#Installation
 1. Install the required packages: pip install Flask

#Usage
 . Run the application: flask run
 . Open your web browser and navigate to http://127.0.0.1:5000/.
 . Use the application to add books, list them, and perform searches.

File Structure
/book-management-app
│
├── app.py                 # Main application file
├── templates/             # Folder for HTML templates
│   ├── index.html         # Home page
│   ├── add_book.html      # Page to add a new book
│   └── list_books.html    # Page to list and search books
└── README.md              # This README file
 
