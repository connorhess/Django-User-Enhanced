"""
Views for the example project.
"""
from django.shortcuts import render


def home(request):
    """Simple home page view."""
    return render(request, 'home.html')
