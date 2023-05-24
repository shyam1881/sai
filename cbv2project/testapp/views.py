from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
#from django.urls import reverse_lazy
# Create your views here.
class BookListView(ListView):
    model = Book
    #template_name = 'testapp/book_list.html'
    #context_object_name = 'books'

class BookListView2(ListView):
    model = Book
    template_name = 'testapp/book.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    #template_name = 'testapp/book_detail.html'
    #context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

from django.urls import reverse_lazy
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('listbooks')