# Generated by Django 4.1.3 on 2022-12-01 19:49

from django.db import migrations

from chats.models import ChatType, MemberPrivilege


def populate_chat_types(apps, schema_editor):
    ChatType.objects.create(title='dialog')
    ChatType.objects.create(title='group')


def populate_member_privileges(apps, schema_editor):
    MemberPrivilege.objects.create(title='user')
    MemberPrivilege.objects.create(title='moderator')
    MemberPrivilege.objects.create(title='admin')


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(populate_chat_types),
        migrations.RunPython(populate_member_privileges),
    ]
