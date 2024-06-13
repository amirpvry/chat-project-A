# chat/views.py

from django.shortcuts import render, redirect
from .models import Chat, Message
from django.http import HttpResponse


def chatPage(request, chat_id):
    if not request.user.is_authenticated:
        return redirect("login-user")
    
    try:
        chat = Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        # Handle the case where Chat object does not exist
        return HttpResponse("Chat does not exist!", status=404)
    
    messages = Message.objects.filter(chat=chat).order_by('timestamp')
    context = {'chat': chat, 'messages': messages}
    return render(request, "chat/chatPage.html", context)