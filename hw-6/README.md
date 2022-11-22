# Домашнее задание № 6

В ДЗ нужно будет дописать все недостающие модели и вьюхи, чтобы можно было связать ваш бэкенд и фронтенд.

Подробнее о вьюхах. Нужно релизовать API на функциональных вьюхах, чтобы по запросу на бэкенде можно было:
1) создать чат (минимальный набор полей: название, описание)

2) отредактировать чат по id (минимальный набор полей: название, описание)

3) добавить участника в чат по id человека и id чата (минимальная проверка: то, что человек уже не добавлен в чат)

4) удалить участника из чата по id человека и id чата

5) удалить чат по id

6) отправить сообщение по id чата

7) отредактировать сообщение по id сообщения

8) пометить сообщение прочитанным по id сообщения

9) удалить сообщение по id сообщения

10) получить список всех чатов

11) получить список сообщений по id чата

12) получить информацию о пользователе по id

13) получить информацию о чате по id чата


(Не нужно писать форм и шаблонов, только функциональные вьюхи с ответом в json-формате)

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

curl -X PATCH -v localhost:8000/chats/messages/mark_as_read/1/

curl -X POST -d '{"member": "1", "chat": 19, "privilege": 1}' -H "Content-Type: application/json" localhost:8000/chats/members/create/

curl -X DELETE -v localhost:8000/chats/members/delete/2/19/

curl -v localhost:8000/users/1/

```