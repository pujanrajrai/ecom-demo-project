from django.shortcuts import render


# Create your views here.

def send_messages(request):
    return render(request, 'messages/home.html')
