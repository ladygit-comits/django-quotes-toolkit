from django.shortcuts import render
import random
# This function handles the homepage
def home(request):
    # A list of motivational quotes to display randomly
    quotes = [
        {"text": "Stay consistent.", "author": "You"},
        {"text": "Keep going.", "author": "Unknown"},
        {"text": "You’ve got this.", "author": "Motivation"},
    ]

    quote = random.choice(quotes)
    # Render the home.html template and pass the chosen quote
    return render(request, 'home.html', {'quote': quote})
