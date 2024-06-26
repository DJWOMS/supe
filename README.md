# Таск менеджер СУП (Система управления проектами)

Собственная система ведения задач.

## Инструменты
- Python 3.12
- Esmerald
- Edgy
- Postgres
- Alembic
- Docker


## Старт
    переименовать
    .env.example на .env

### Запустить сборку
```
docker-compose up --build
```

### Перейти по адресу
```
http:\\127.0.0.1:8000\docs\swagger
```

## Alembic создание migrations
Не выключая контейнеры выполнить команду
```
docker exec -it sup_back-api-1 edgy init

docker exec -it sup_back-api-1 edgy makemigrations -m 'название модели или миграции'
docker exec -it sup_back-api-1 edgy migrate
```

### Создать администратора
```
docker exec -it sup_back-api-1 esmerald run --directive createadmin --username admin --email admin@example.com --password Test123!
```

### Способ организации кода
- Для выборок данных используем паттерн репозиторий.
- Бизнес-логика и операции создания/изменения моделей выносим в UseCase-классы. 
UseCase классы не хранят свое состояние, что позволяет их переиспользовать без повторной 
инициализации.
- Для того чтобы не зависеть от Request в сервисы передаем либо одиночные параметры, 
либо DTO (Pydantic Model). 
Это позволяет переиспользовать код вне контроллеров (например, команда создания нового 
пользователя и т.д.).
- Стараемся, чтобы модели оставались максимально тонкими. В основном содержат в себе связи 
(relations).
- Все relation_ship lazy должны быть raise_on_sql
