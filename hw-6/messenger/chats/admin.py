from django.contrib import admin

from .models import Chat, Message, ChatType, ChatMember, MemberPrivilege


class ChatAdmin(admin.ModelAdmin):
    list_display = ('title','chat_type', 'creator',)
    list_filter = ('chat_type', 'creator',)
    raw_id_fields = ('creator',)
    search_fields = ('title',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'chat', 'created_at',)
    raw_id_fields = ('sender', 'chat',)
    search_fields = ('sender__username', 'chat__title')


class ChatTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ChatMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'chat', 'privilege',)
    list_filter = ('member', 'chat', 'privilege',)
    raw_id_fields = ('member', 'chat',)
    search_fields = ('member__username', 'chat__title',)


class MemberPrivilegeAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(ChatType, ChatTypeAdmin)
admin.site.register(ChatMember, ChatMemberAdmin)
admin.site.register(MemberPrivilege, MemberPrivilegeAdmin)
