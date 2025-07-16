from rest_framework.decorators import api_view
from rest_framework.response import Response

# Hardcoded list of books
BOOKS = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 3, "title": "Deep Work", "author": "Cal Newport"},
]

@api_view(['GET'])
def get_books(request):
    print("GET /books/ called")  # Debug log
    return Response(BOOKS)

@api_view(['POST'])
def place_order(request):
    book_id = request.data.get('book_id')
    customer_name = request.data.get('customer_name')

    book = next((b for b in BOOKS if b['id'] == book_id), None)

    if not book:
        return Response({"error": "Book not found"}, status=400)

    return Response({
        "message": "Order placed successfully!",
        "order": {
            "book": book,
            "customer": customer_name
        }
    })
