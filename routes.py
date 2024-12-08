from flask import Blueprint, request, jsonify
from utils.auth import require_auth
from utils.pagination import paginate
import json

routes = Blueprint("routes", __name__)
DATABASE = "data/database.json"

def load_data():
    with open(DATABASE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATABASE, "w") as file:
        json.dump(data, file)

@routes.route('/books', methods=['GET'])
@require_auth
def get_books():
    data = load_data()
    books = data['books']
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))
    paginated_books, total = paginate(books, page, per_page)
    return jsonify({
        "books": paginated_books,
        "total": total,
        "page": page,
        "per_page": per_page
    })

@routes.route('/books/<int:book_id>', methods=['GET'])
@require_auth
def get_book(book_id):
    data = load_data()
    book = next((book for book in data['books'] if book['id'] == book_id), None)
    if book:

        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@routes.route('/books', methods=['POST'])
@require_auth
def add_book():
    data = load_data()
    new_book = request.json
    new_book['id'] = len(data['books']) + 1
    data['books'].append(new_book)
    save_data(data)
    return jsonify(new_book), 201

@routes.route('/books/<int:book_id>', methods=['PUT'])
@require_auth
def update_book(book_id):
    data = load_data()
    book = next((book for book in data['books'] if book['id'] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    updated_data = request.json
    for key, value in updated_data.items():
        book[key] = value
    save_data(data)
    return jsonify(book)

@routes.route('/books/<int:book_id>', methods=['DELETE'])
@require_auth
def delete_book(book_id):
    data = load_data()
    book = next((book for book in data['books'] if book['id'] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    data['books'] = [b for b in data['books'] if b['id'] != book_id]
    save_data(data)
    return jsonify({"message": "Book deleted successfully"})

@routes.route('/search', methods=['GET'])
@require_auth
def search_books():
    query = request.args.get("query", "").lower()
    data = load_data()
    results = [book for book in data['books'] if query in book['title'].lower() or query in book['author'].lower()]
    return jsonify(results)
