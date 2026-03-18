# itdirr

## Wall

Модуль `wall` позволяет:

- получать посты со стены пользователя
- писать на стену пользователя

----------

## Получить посты со стены

```python
client.get_wall("username")
```

### Параметры

- `username` — username пользователя
- `limit` — количество постов (по умолчанию `20`)
- `cursor` — курсор для пагинации (необязательный)

### Возвращает

Модель `Posts` [подробнее](models/posts.md)

### Пример

```python
wall = client.get_wall("gam5510")

print("Постов на стене:", len(wall))

for post in wall:
    print("Автор:", post.author.username)
    print("Текст:", post.content)
    print("-" * 30)
```

----------

## Написать на стену

```python
client.post_to_wall("username", "Текст поста")
```

### Параметры

- `username` — username пользователя
- `content` — текст поста

### Возвращает

Модель `Post` [подробнее](models/post.md)

### Пример

```python
post = client.post_to_wall("gam5510", "Привет!")

print("Пост создан:", post.id)
```

← [Назад к документации](index.md)
