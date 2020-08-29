from django.http import HttpResponse
from django.shortcuts import render
import time
import pandas as pd


def homepage(request):
    return render(request, 'index.html')


def analyze(request):
    ftext = request.POST.get('userinput', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    ticker = time.asctime(time.localtime(time.time()))

    if removepunc == 'on':
        punctuation = '''!@#$%^&*(),./;':"<>?'''
        analyzed = ""
        for char in ftext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'analyzed': analyzed, 'ticker': ticker}
        ftext = analyzed
        # return render(request, 'analyze.html', params)

    if uppercase == 'on':
        analyzed = ""
        for char in ftext:
            analyzed = analyzed + char.upper()
        params = {'analyzed': analyzed, 'ticker': ticker}
        ftext = analyzed

        # return render(request, 'analyze.html', params)

    if newlineremover == 'on':
        analyzed = ""
        for char in ftext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'analyzed': analyzed, 'ticker': ticker}
        ftext = analyzed
        # return render(request, 'analyze.html', params)

    if spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(ftext):
            if not (ftext[index] == " " and ftext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'analyzed': analyzed, 'ticker': ticker}
        # ftext = analyzed

    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")


def contactus(request):
    return render(request, 'contact.html')


def aboutus(request):
    return render(request, 'about.html')


