# Cервис Foodgram, "Продуктовый помощник"  

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Описание

Дипломный проект — сайт Foodgram, «Продуктовый помощник». Онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

#### Документация к API доступна по адресу <http://localhost/api/docs/> после локального запуска проекта

#### Технологи

- Python 3.7
- Django 3.2.15
- Django Rest Framework 3.12.4
- Authtoken
- Docker
- Docker-compose
- PostgreSQL
- Gunicorn
- Nginx
- GitHub Actions
- Выделенный сервер Linux Ubuntu 22.04 с публичным IP

#### Запуск проекта

- Склонировать репозиторий и развернуть его 

```bash
git clone git@github.com:VladimirIakushev/foodgram-project-react.git
python -m venv venv
pip install -r requirements.txt
python manage.py migrate
```

- Cоздать в папке backend/foodgram/foodgram файл .env по образцу .envexample

- Запустить проект на удаленном сервере

- В файле nginx.conf установить свои параметры 'server_name ip доменное имя', например:

```bash
server_name 0.0.0.0 example.com
```

- Находясь локально в директории infra/, скопировать файлы docker-compose.production.yml и nginx.conf на удаленный сервер:

```bash
scp docker-compose.production.yml <username>@<host>:/home/<username>/
scp nginx.conf <username>@<host>:/home/<username>/
```

- Запустить из рабочей директории:

```bash
sudo docker compose -f docker-compose.production.yml up -d
sudo docker compose -f docker-compose.production.yml ps
```

- Проверить, что запущена сеть контейнеров:

```bash
✔ Network foodgram-project-react_default       Created                                                             0.1s 
 ✔ Container foodgram-project-react-db-1       Started                                                             5.7s 
 ✔ Container foodgram-project-react-frontend-1 Started                                                             5.8s 
 ✔ Container foodgram-project-react-backend-1  Started                                                              1.8s 
 ✔ Container foodgram-project-react-nginx-1    Started                                                              2.0s 
```

- Далее запустить по очереди команды из рабочей директории:

```bash
sudo docker compose -f docker-compose.production.yml exec backend python manage.py makemigrations
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py load_data
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
```

- Проверить доступ по доменному имени через браузер

#### Проект доступен по адресу

http://158.160.29.235/
http://foodgreat.hopto.org

#### Логин и пароль суперюзера

yc-user
login le-2006@yandex.ru
пароль Numenor07t

#### Владимир Якушев
https://t.me/Vidomir_Crni
le-2006@yandex.ru
