# ITDpy

Python SDK для социальной сети ITD.
Упрощает работу с SDK API и позволяет быстро писать ботов и автоматизации.

> ⚠️ Библиотека ориентирована на безопасное и ответственное использование.

## Установка pip
```bash
pip install itdpy
```

### Через git

```bash
git clone https://github.com/Gam5510/ITDpy
cd itdpy
pip install -r requirements.txt
pip install -e .
```

## Быстрый старт

> Blockquote ![Получение токена](https://i.ibb.co/DH1m8GL7/Assistant.png)
Как получить токен

```python
from  itdpy.client  import  ITDClient

client  =  ITDClient(refresh_token="Ваш refresh token")

me  =  client.get_me()
print(me.id)
print(me.username)
```

### Скрипт на обновление имени

```python
from  itdpy.client  import  ITDClient
from  datetime  import  datetime
import  time

client = ITDClient(refresh_token="Ваш_токен")


while  True:
	client.update_profile(display_name=f"Фазлиддин |{datetime.now().strftime('%m.%d %H:%M:%S')}|")
	time.sleep(1)
```

### Скрипт на обновление баннера 
```python
from  itdpy.client  import  ITDClient
from  datetime  import  datetime
import  time

client  =  ITDClient(refresh_token="Ваш_токен")

file  =  client.upload_file("matrix-rain-effect-animation-photoshop-editor.gif")
print(file.id)
update  =  client.update_profile(banner_id=file.id)
print(update.banner)
```

## ITDpy теперь поддерживает удобное форматирование текста через HTML.
Больше не нужно вручную рассчитывать offset и length.
| HTML             | Формат        |
| ---------------- | ------------- |
| `<b>` `<strong>` | Жирный        |
| `<i>` `<em>`     | Курсив        |
| `<u>`            | Подчёркивание |
| `<s>` `<del>`    | Зачёркнутый   |
| `<code>`         | Моноширинный  |
| `<spoiler>`      | Спойлер       |
```python
from  itdpy.client  import  ITDClient

client  =  ITDClient(refresh_token="Ваш_токен")
client.create_post(
    content="""
Обновление <b>ITDpy</b> уже в процессе 🚀

Добавлен <i>HTML → spans</i> парсер.
""",
    parse_html=True
)

```



# Костомные запросы  

## ✅ Базовый пример кастомного GET
```python
response = client.get("/api/users/me")
data = response.json() 
print(data)
```
### Можно добавить любой эндпоинт
----------

## ✅ POST с JSON
```python
response = client.post( 
		"/api/posts",
    json={ "content": "Привет из кастомного запроса" }
) 
print(response.status_code) 
print(response.json())
```
----------

## ✅ PUT / PATCH
```python
response = client.patch( "/api/profile",
    json={ "displayName": "Фазлиддин 😎" }
)
```
----------

## ✅ DELETE
```python
client.delete("/api/posts/POST_ID") 
```
----------

## ✅ Передача query-параметров
```python
response = client.get( "/api/posts",
    params={ "limit": 50, "sort": "popular" }
)
```

## Планы

- Улучшенная обработка и форматирование ошибок
- Логирование (через `logging`)
- Дополнительные API-эндпоинты по мере появления
- Улучшение документации и примеров


## Прочее

Проект активно развивается.
Если у вас есть идеи или предложения — создавайте issue или pull request.
