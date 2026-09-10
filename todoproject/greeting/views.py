from django.shortcuts import render


def gallery(request):
    return render(request, 'greeting/gallery.html')


def contact(request):
    return render(request, 'greeting/contact.html')