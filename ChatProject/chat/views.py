# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Chat, Message

def chatPage(request, chat_id, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.filter(chat=chat).order_by('timestamp')
    context = {'chat': chat, 'messages': messages}
    return render(request, "chat/chatPage.html", context)

