from django.shortcuts import render


def gallery(request):
    return render(request, 'greeting/gallery.html')


def contact(request):
    return render(request, 'greeting/contact.html')


def students(request):
    students = [
        {'name': 'Rahul', 'grade': 85, 'passed': True},
        {'name': 'Anu', 'grade': 72, 'passed': True},
        {'name': 'Kiran', 'grade': 45, 'passed': False},
        {'name': 'Meera', 'grade': 90, 'passed': True},
    ]

    return render(request, 'greeting/students.html', {
        'students': students
    })