"""
Author = Francisco Gomes and Jymmy Barreto
Date = 18/02/2022
Version = 1.0
File description = Importing libraries and create functions logical
"""

# ------------------------------------------------------------
# Importing libraries of render, requests and random
# render = Generate content about page
# requests = call requests of server
# random = generate aleatory values
from django.shortcuts import render
from django.http import HttpResponse
import random
# ------------------------------------------------------------

# Create your views here.

# Creating page main (Principal)
def home(request):
    return render(request, "generator/home.html") # Request for route in "urls"

def about(request):
    return render(request, "generator/about.html")

# Create function for parameters in characters, letters uppercase and lowercase, character special and numbers
def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz") # first list of characters
    if (request.GET.get("uppercase")):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSUVWXYZ")) # Method of extends values in lists
    if (request.GET.get("special")):
        characters.extend(list("!@#$%¨&*()")) # Method of extends values in list
    if (request.GET.get("numbers")):
        characters.extend(list("0123456789")) # Method of extends values in list

    length = int(request.GET.get("length")) # Define size of content
    thepassword = "" # variable of completed password
    for x in range(length):
        thepassword+=random.choice(characters)

    return render(request, "generator/password.html", {"password":thepassword}) # Route reference of page HTML and return the password generated
