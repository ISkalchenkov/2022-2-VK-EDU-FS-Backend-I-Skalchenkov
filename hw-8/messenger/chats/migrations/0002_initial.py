# Generated by Django 4.1.3 on 2022-12-01 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender_messages', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
        ),
        migrations.AddField(
            model_name='chatmember',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_chatmembers', to='chats.chat', verbose_name='Чат'),
        ),
        migrations.AddField(
            model_name='chatmember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_chatmembers', to=settings.AUTH_USER_MODEL, verbose_name='Участник'),
        ),
        migrations.AddField(
            model_name='chatmember',
            name='privilege',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='privelege_chatmembers', to='chats.memberprivilege', verbose_name='Привелегия'),
        ),
        migrations.AddField(
            model_name='chat',
            name='chat_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chattype_chats', to='chats.chattype', verbose_name='Тип чата'),
        ),
        migrations.AddField(
            model_name='chat',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_chats', to=settings.AUTH_USER_MODEL, verbose_name='Создатель чата'),
        ),
    ]
