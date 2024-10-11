from flask import Flask, request, jsonify
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()  # Create the database tables

@app.route('/')
def index():
    return "Welcome to the Book Library API!"


@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data or 'genre' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_book = Book(title=data['title'], author=data['author'], genre=data['genre'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201


@app.route('/books', methods=['GET'])
def list_books():
    genre = request.args.get('genre')
    author = request.args.get('author')

    query = Book.query
    if genre:
        query = query.filter_by(genre=genre)
    if author:
        query = query.filter_by(author=author)

    books = query.all()
    return jsonify([book.to_dict() for book in books]), 200


@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    books = Book.query.filter((Book.title.contains(query)) | (Book.author.contains(query))).all()
    return jsonify([book.to_dict() for book in books]), 200


# Add other routes here...

if __name__ == '__main__':
    app.run(debug=True)