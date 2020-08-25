from django.shortcuts import render


def get_home_page(request):
    return render(request, 'home.html')


def get_reverse_page(request):
    user_text = request.GET['user-text']
    reversed_text = user_text[::-1]
    amount_of_words = len(user_text.split())
    return render(request, 'reverse.html',
                  {'amount_of_words': amount_of_words,
                   'user_text': user_text,
                   'reversed_text': reversed_text,
                   })
