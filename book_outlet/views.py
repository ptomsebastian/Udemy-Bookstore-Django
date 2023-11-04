from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg
# Create your views here.
def index(request):
    book = Book.objects.all().order_by('title')
    num_bk = book.count()
    avg_rat = book.aggregate(Avg("rating"))
    return render(request, 'book_outlet/index.html', {'Book': book, 'total_books': num_bk, 'avg rating': avg_rat})

def book_detail(request, slug):
    # book = Book.objects.get(slug=slug)
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        # 'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling})