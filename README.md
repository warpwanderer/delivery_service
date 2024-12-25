# Инструкция по развертке API-системы службы доставки на FastAPI в Docker

## Описание
Данная инструкция предназначена для развертки простой API-системы, имитирующей деятельность службы доставки. Сервис реализует следующие функции:

- Создание заявки на доставку.
- Получение информации о заявке.
- Удаление заявки (только если товар не передан в доставку).

Заявка может находиться в одном из трёх состояний:
- Создана (created).
- Товар передан в доставку (in_delivery).
- Товар доставлен (delivered).

Данные заявок хранятся в базе данных SQLite.

---

## Требования
Перед началом убедитесь, что на вашей системе установлены:

- **Docker**
- **Docker Compose**

Для проверки выполните команды:
```bash
docker --version
docker-compose --version
```
Если Docker или Docker Compose не установлены, скачайте и установите их с официального сайта [Docker](https://www.docker.com/).

---

## Шаги для развертки проекта

### 1. Клонируйте репозиторий проекта
Склонируйте репозиторий с проектом на локальную машину:
```bash
git clone https://github.com/warpwanderer/delivery_service.git
cd delivery_service
```

---

### 2. Проверьте структуру проекта
Убедитесь, что структура проекта включает следующие файлы:

```
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── data/
```

Папка `data/` используется для хранения базы данных SQLite.
Если папки `data` нет, создайте её.

---

### 3. Соберите и запустите контейнер
Для развертки проекта выполните команду:
```bash
docker-compose up --build
```

После успешного запуска приложение будет доступно по адресу:
```
http://localhost:8000
```

Для фонового запуска используйте:
```bash
docker-compose up -d
```

---

### 4. Проверка работы

Для проверки API можно использовать встроенный интерфейс Swagger:
```
http://localhost:8000/docs
```

---

### 6. Остановка контейнеров
Для остановки контейнеров выполните:
```bash
docker-compose down
```

Эта команда завершит работу контейнеров и освободит порты.

---

### 7. Обновление приложения
Если вы внесли изменения в код или зависимости, выполните следующие шаги:

1. Остановите контейнеры:
    ```bash
    docker-compose down
    ```
2. Пересоберите образ и запустите контейнер:
    ```bash
    docker-compose up --build
    ```

---

## Примечания
- Для управления зависимостями используйте файл `requirements.txt`. Если добавляете новую зависимость, обновите файл:
  ```bash
  pip freeze > requirements.txt
  ```
  Затем пересоберите контейнер.

---

