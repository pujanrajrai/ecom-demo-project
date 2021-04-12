from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.db.models import Q

from accounts.models import MyUser
from .forms import ChatForms
from .models import Chat

# Create your views here.
from shop_profile.models import ShopProfile


@login_required()
def send_messages(request, username):
    if not ShopProfile.objects.filter(shop_user_name=username).exists():
        return HttpResponse('no user exist')
    send_to = ShopProfile.objects.get(shop_user_name=username)
    chats = Chat.objects.filter(
        Q(
            Q(send_from=request.user) & Q(send_to=send_to.owner)) |
        Q(
            Q(send_from=send_to.owner) & Q(send_to=request.user))
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
                send_to=send_to.owner,
                message=message,
                image=images,
            )
            chat.save()

    context = {"username": username, "chats": chats}
    return render(request, 'chat/home.html', context)
