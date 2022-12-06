from rest_framework import serializers

from chats.models import Chat, ChatMember, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'title', 'description', 'chat_type', 'creator', 'created_at']


class ChatUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'title', 'description', 'chat_type', 'creator', 'created_at']
        extra_kwargs={
            'chat_type': {'read_only': True},
            'creator': {'read_only': True},
        }


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'body', 'created_at', 'chat', 'sender', 'read']
        extra_kwargs={
            'sender': {'required': True, 'allow_null': False},
            'read': {'read_only': True}
        }


class MessageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'body', 'created_at', 'chat', 'sender', 'read']
        extra_kwargs={
            'chat': {'read_only': True},
            'sender': {'read_only': True},
            'read': {'read_only': True}
        }


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMember
        fields = ['member', 'chat', 'joined_at', 'privilege']
