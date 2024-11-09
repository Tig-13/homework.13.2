from django.shortcuts import render, redirect
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes_list')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})

def quotes_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes_list.html', {'quotes': quotes})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})
