# База отзывов о фильмах, книгах и музыке.

REST API сервис, где пользователи могут:
- пополнять базу данных различным контентом;
- комментировать и оценивать имеющиеся наименования;
- получать доступ к функциональности приложения в зависимости от установленных прав доступа.

## Установка

Склонировать репозиторий, разместить .env в директории с проектом.

```python
SECRET_KEY=******
EMAIL_HOST_USER=******
DB_ENGINE=******
DB_NAME=******
POSTGRES_USER=******
POSTGRES_******
DB_HOST=******
DB_PORT=******
```

Запустить docker-compose

```bash
docker-compose up
```

## Usage

Документация к проекту:
```
localhost/redoc
```

## Технологии

1. Django Rest Framework
2. PostgreSQL
3. Docker
4. Nginx и Gunicorn
4. GitHub Actions

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)

## Статус workflow

![yamdb](https://github.com/dmitriibogomolov/yamdb_final/workflows/yamdb_final%20workflow/badge.svg?branch=master)
