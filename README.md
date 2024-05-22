### CRUD для Yatube - api_yatube

Для взаимодействия с ресурсами доступны следующие эндпоинты:
* ```api/v1/api-token-auth/``` (POST): передаём логин и пароль, получаем токен.
* ```api/v1/posts/``` (GET, POST): получаем список всех постов или создаём новый пост.
* ```api/v1/posts/{post_id}/``` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
* ```api/v1/groups/``` (GET): получаем список всех групп.
* ```api/v1/groups/{group_id}/``` (GET): получаем информацию о группе по id.
* ```api/v1/posts/{post_id}/comments/``` (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
* ```api/v1/posts/{post_id}/comments/{comment_id}/``` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.

### Технологии:
* Python 3.11
* Django 3.2.16
* Django REST framework 3.12.4


### Запуск проекта

Клонировать проект c GitHub:

```bash
git clone git@github.com:chrnmaxim/api_yatube.git
```

Перейти в папку с проектом:

```bash
cd api_yatube
```
Установить виртуальное окружение:
```bash
python -m venv venv
```
Активировать виртуальное окружениe:
```bash
. venv/Scripts/activate
```
Обновить менеджер пакетов pip:
```bash
python -m pip install --upgrade pip
```
Установить зависимости из requirements.txt:
```bash
pip install -r requirements.txt
``` 
Перейти в директорию с файлом manage.py и применить миграции:
```bash
cd yatube_api
python manage.py migrate
``` 
Создать супер пользователя:

```bash
python manage.py createsuperuser
```
Запустить сервер разработки (виртуальное окружение должно быть активно):
```bash
python manage.py runserver 
```
