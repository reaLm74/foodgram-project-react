![foodgram-project-react Workflow Status](https://github.com/realm74/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master&event=push)
# Продуктовый помощник Foodgram 

После запуска проекта, он будет доступен по адресу http://localhost/
Как запустить и посмотреть в действии описано ниже.

## Описание проекта Foodgram
«Продуктовый помощник»: приложение, на котором пользователи публикуют рецепты кулинарных изделий, подписываться на публикации других авторов и добавлять рецепты в свое избранное.
Сервис «Список покупок» позволит пользователю создавать список продуктов, которые нужно купить для приготовления выбранных блюд согласно рецепта/ов.

## Запуск с использованием CI/CD и Docker

```bash
# В Settings - Secrets and variables создаем переменный с вашими данными
# Это необходимо для работы с CI/CD, DockerHub, GitHub
DB_ENGINE
DB_HOST
DB_PORT
HOST
MY_LOGIN
MY_PASS
PASSPHRASE
POSTGRES_DB
POSTGRES_PASSWORD
POSTGRES_USER
SSH_KEY
USER
TOKEN
```

Необходимо перенести файлы docker-compose.yml и default.conf на сервер, из папки infra в текущем репозитории.

```bash
cd infra
```

```bash
scp docker-compose.yml username@server_ip:
```

```bash
scp default.conf username@server_ip:
```

Далее в папке infra выполняем команду:

```bash
sudo docker-compose up -d --build
```

Проект запустится на ВМ и будет доступен по указанному вами адресу либо IP. Завершение настройки на ВМ:

В папке infra выполняем команду, что бы собрать контейнеры:

Остановить: 

```bash
sudo docker compose stop
```

Удалить вместе с volumes:

```bash
# Все данные удалятся!
sudo docker compose down -v
``` 

Для доступа к контейнеру backend и сборки финальной части выполняем следующие команды:

```bash
sudo docker compose exec backend python manage.py makemigrations
```

```bash
sudo docker compose exec backend python manage.py migrate --noinput
```

```bash
sudo docker compose exec backend python manage.py createsuperuser
```

```bash
sudo docker compose exec backend python manage.py collectstatic --no-input
```

Дополнительно можно наполнить DB ингредиентами и тэгами:

```bash
sudo docker compose exec backend python manage.py load_tags
```

```bash
sudo docker compose exec backend python manage.py load_ingrs
```

Продуктовый помощник запущен!

### Документация к API доступна после запуска

```url
http://127.0.0.1/api/docs/
```
