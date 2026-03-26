from django.shortcuts import render
import random

def home(request):
    quotes = [
        {"text": "Stay consistent.", "author": "You"},
        {"text": "Keep going.", "author": "Unknown"},
        {"text": "You’ve got this.", "author": "Motivation"},
    ]

    quote = random.choice(quotes)
    return render(request, 'home.html', {'quote': quote})
