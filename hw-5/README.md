# Домашнее задание № 5

## Создать свою модель пользователя

Если еще не создали, то теперь точно нужно создать свою модель пользователя, настоятельно рекомендую сделать для пользователей отдельное приложение. Модель должна наследываться от AbstractUser и не переписывать существующие поля пользователя, а только добавлять новые поля. Подумайте, чтобы вы добавили, из того, что может пользователь указать при регистрации в вашем мессенджере

## Переписать вью так, чтобы создавались и отдавались реальные объекты (CRUD)


Как минимум у вас должны быть реализованы:

1. Создание чата/сообщения
2. Получение детальной информации о чате/сообщении по его id
3. Получение списка чатов пользователя/сообщений пользователя по id чата
4. Редактирование чата/сообщения по id
5. Удаление чата/сообщения по id

## Подключить все созданные модели в админку

Также стоит максимально кастомизировать подключаемые в админке модели, помимо этого, пожалуйста, кастомизируйте ваши модели:

- verbose_name у полей
- verbose_name и verbose_name_plural у моделей
- поменять дефолтную сортировку там, где это уместно
- добавить related_name к связям

*N.B.*

- не называйте поля-связи author_id -> нужно author
- называйте поля ManyToMany во множественном числе


### Примеры запросов через curl:
```
curl -v localhost:8000/

curl -v localhost:8000/chats/

curl -v localhost:8000/chats/13/

curl -X POST -d '{"title": "VK_Edu", "description": "Education", "chat_type": 2, "creator": 1}' -H "Content-Type: application/json" -v localhost:8000/chats/create/

curl -X DELETE -v localhost:8000/chats/delete/20/

curl -X PATCH -d '{"title": "Bmstu communication", "description": "Hello"}' -H "Content-Type: application/json" -v localhost:8000/chats/edit/19/

curl -v localhost:8000/chats/19/messages/

curl -X POST -d '{"body": "Hello", "sender": 1, "chat": 19}' -H "Content-Type: application/json" -v localhost:8000/chats/messages/create/

curl -v localhost:8000/chats/messages/3/

curl -X PATCH -d '{"body": "How are you?"}' -H "Content-Type: application/json" -v localhost:8000/chats/messages/edit/3/

curl -X DELETE -v localhost:8000/chats/messages/delete/3/
```