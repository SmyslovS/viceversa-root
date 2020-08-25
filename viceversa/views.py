from django.shortcuts import render


def get_home_page(request):
    return render(request, 'home.html')


def get_reverse_page(request):
    return render(request, 'reverse.html')
