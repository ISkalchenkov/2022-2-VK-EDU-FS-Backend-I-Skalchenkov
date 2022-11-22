# Generated by Django 4.1.3 on 2022-11-22 19:01

from django.db import migrations

from chats.models import MemberPrivilege


def populate_member_privileges(apps, schema_editor):
    MemberPrivilege.objects.create(title='user')
    MemberPrivilege.objects.create(title='moderator')
    MemberPrivilege.objects.create(title='admin')


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20221122_0245'),
    ]

    operations = [
        migrations.RunPython(populate_member_privileges),
    ]
