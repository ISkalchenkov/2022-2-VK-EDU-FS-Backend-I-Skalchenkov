from django.db import models

from application.settings import AUTH_USER_MODEL


class ChatType(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название типа чата')

    class Meta:
        verbose_name = 'Тип чата'
        verbose_name_plural = 'Типы чата'

    def __str__(self):
        return self.title


class Chat(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название чата')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание чата')
    chat_type = models.ForeignKey(
        ChatType,
        null=True,
        on_delete=models.SET_NULL,
        related_name='chattype_chats',
        verbose_name='Тип чата'
    )
    creator = models.ForeignKey(
        AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='creator_chats',
        verbose_name='Создатель чата'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания чата')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return self.title


class MemberPrivilege(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название привелегии')

    class Meta:
        verbose_name = 'Привелегия участника чата'
        verbose_name_plural = 'Привелегии участника чата'

    def __str__(self):
        return self.title


class ChatMember(models.Model):
    member = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='member_chatmembers',
        verbose_name='Участник'
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='chat_chatmembers',
        verbose_name='Чат'
    )
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время присоединения')
    privilege = models.ForeignKey(
        MemberPrivilege,
        null=True,
        on_delete=models.SET_NULL,
        related_name='privelege_chatmembers',
        verbose_name='Привелегия'
    )
    
    class Meta:
        verbose_name = 'Участник чата'
        verbose_name_plural = 'Участники чата'

    def __str__(self):
        return f"member: {self.member} chat: {self.chat}"


class Message(models.Model):
    body = models.TextField(verbose_name='Тело сообщения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    chat = models.ForeignKey(
        Chat,
        null=True,
        on_delete=models.CASCADE,
        related_name='chat_messages',
        verbose_name='Чат сообщения'
    )
    sender = models.ForeignKey(
        AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='sender_messages',
        verbose_name='Отправитель'
    )
    read = models.BooleanField(default=False, verbose_name='Прочитано')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f"sender: {self.sender} chat: {self.chat}"
