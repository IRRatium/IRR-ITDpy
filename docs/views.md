# itdirr

## Views

Модуль `views` позволяет отмечать посты как просмотренные — так же как это делает браузер при открытии поста.

----------

## Отметить пост как просмотренный

```python
client.view_post(post_id)
```

### Параметры

- `post_id` — ID поста

### Возвращает

`True` при успехе

### Пример

```python
post = client.get_post("1e919573-cb93-42c6-b9c1-7d35d9484d9e")
client.view_post(post.id)
```

----------

## Отметить несколько постов

```python
client.view_posts([post_id1, post_id2, post_id3])
```

### Параметры

- `post_ids` — список ID постов

### Возвращает

Словарь `{post_id: bool}` — результат для каждого поста

### Пример

```python
posts = client.get_posts(limit=20)
ids = [post.id for post in posts]

results = client.view_posts(ids)

for post_id, success in results.items():
    print(f"{post_id}: {'✅' if success else '❌'}")
```

← [Назад к документации](index.md)
