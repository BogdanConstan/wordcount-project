from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordcounter = {}
    for word in wordlist:
        if word in wordcounter:
            wordcounter[word] += 1
        else:
            wordcounter[word] = 1
            
    sorted_words = sorted(wordcounter.items(), key=operator.itemgetter(1), reverse = True)
    
    return render(request, 'count.html', {'fulltext': fulltext,'count': len(wordlist), 'sorted_words': sorted_words})# -*- coding: utf-8 -*-

def about(request):
    return render(request, 'about.html')