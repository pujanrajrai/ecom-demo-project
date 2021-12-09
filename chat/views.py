from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.db.models import Q, Count

from accounts.models import MyUser
from .forms import ChatForms
from .models import Chat

# Create your views here.
from shop_profile.models import ShopProfile


@login_required()
def send_messages(request, username):
    if not MyUser.objects.filter(username=username).exists():
        return HttpResponse('no user exist')
    send_to = MyUser.objects.get(username=username)

    chats = Chat.objects.filter(
        Q(
            Q(send_from=request.user) & Q(send_to=send_to)) |
        Q(
            Q(send_from=send_to) & Q(send_to=request.user))
    ).order_by('send_date')
    all_message = Chat.objects.filter(
        Q(send_to=request.user)
    ).order_by('-send_date')

    if request.method == 'POST':
        message = request.POST.get('message')
        images = request.FILES['images'] if 'images' in request.FILES else False
        if not message and not images:
            return HttpResponse('nothing')
        forms = ChatForms(request.POST, request.FILES)
        if forms.is_valid():
            chat = Chat(
                send_from=request.user,
                send_to=send_to,
                message=message,
                image=images,
            )
            chat.save()

    context = {"username": username, "chats": chats, "all_messages": all_message}
    return render(request, 'chat/home.html', context)
