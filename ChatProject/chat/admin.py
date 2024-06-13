from django.contrib import admin
from .models import Chat, Message

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_participants')

    def get_participants(self, obj):
        return ", ".join([participant.username for participant in obj.participants.all()])

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'sender', 'content', 'timestamp')
    list_filter = ('chat', 'sender')
    search_fields = ('content', 'sender__username')

