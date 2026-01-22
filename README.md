# FastAPI TODO CRUD API - полноценное REST API для управления задачами. Демонстрация backend-навыков: FastAPI, Pydantic, SQLAlchemy. Готово к продакшену с тестами и Docker.


# Описание
Полноценный CRUD для TODO-задач:

POST /todos/ - создать задачу
GET /todos/ - список задач
GET /todos/{id} - одна задача
PUT /todos/{id} - обновить
DELETE /todos/{id} - удалить

# Стек: 
FastAPI, Pydantic, uvicorn. Покрытие тестами 90%+.

# Быстрый старт
bash
git clone https://github.com/vladbrigman-ops/fastapi-portfolio.git
cd fastapi-portfolio
pip install -r requirements.txt
uvicorn main:app --reload
API Docs: http://localhost:8000/docs (Swagger UI)

# Примеры запросов
bash
Создать задачу:
curl -X POST "http://localhost:8000/todos/" -H "Content-Type: application/json" -d "{\"title\":\"Купить молоко\",\"completed\":false}"

Получить все:
curl http://localhost:8000/todos/

Удалить задачу:
curl -X DELETE "http://localhost:8000/todos/1"

# Технологии
FastAPI 0.115+, Pydantic V2, Uvicorn/ASGI, Pytest, OpenAPI/Swagger

# Тесты
bash
pip install pytest pytest-cov
pytest --cov=main --cov-report=html

# Docker
bash
docker build -t fastapi-crud .
docker run -p 8000:8000 fastapi-crud

# Автор
Влад Бригман 
📧 [vladbrigman@gmail.com] | 💬 Telegram: @manicorny
