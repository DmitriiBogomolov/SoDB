# YaMDb

REST API с базой отзывов о фильмах, книгах и музыке.


### Зависимости

Для запуска приложения должны быть установлены Python3 и Docker.

### Установка

1) поместить .env в дирректорию с проектом.
2) запустить docker-compose
```
docker-compose up
```
3) в списке запущеных контейнеров найти id контейнера api_yamdb_web
```
docker container ls
```
4) применить миграции
```
docker exec -it <api_yamdb_web container id> python manage.py migrate
```
5) создать пользователя
```
docker exec -it <api_yamdb_web container id> python manage.py createsuperuser
```
6) для заполнения БД начальными значениями применить фикстуры
```
docker exec -it <api_yamdb_web container id> python manage.py loaddata fixtures.json
```

## Развертывание

Аналогично с установкой запустить docker-compose. Настроить на веб-сервере проксировние и статику.

## Использовались

* Django, DRF
* Docker
* Gunicorn
* PostgreSQL
