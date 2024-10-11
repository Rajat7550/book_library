from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# In-memory storage for books
books = []

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a new book
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        genre = request.form.get('genre')

        if not title or not author or not genre:
            flash('Title, author, and genre are required!')
            return redirect(url_for('add_book'))

        book = {
            'id': len(books) + 1,
            'title': title,
            'author': author,
            'genre': genre
        }
        books.append(book)
        flash('Book added successfully!')
        return redirect(url_for('list_books'))

    return render_template('add_book.html')

# Route to list all books or filter by genre or author
@app.route('/books', methods=['GET'])
def list_books():
    author = request.args.get('author')
    genre = request.args.get('genre')

    filtered_books = books
    if author:
        filtered_books = [book for book in filtered_books if book['author'] == author]
    if genre:
        filtered_books = [book for book in filtered_books if book['genre'] == genre]

    return render_template('list_books.html', books=filtered_books)

# Route to search for books by title or author
@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    if not query:
        flash('Query parameter is required!')
        return redirect(url_for('list_books'))

    results = [book for book in books if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
    return render_template('list_books.html', books=results)

if __name__ == '__main__':
    app.run(debug=True)
