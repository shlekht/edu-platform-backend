# Educational Platform Project

<details>
<summary>🇷🇺 Русский</summary>
<br>

Мой первый backend проект на FastAPI. Связанный frontend — [[github](https://github.com/shlekht/edu-platform-frontend)]. Общая идея — аналог сайта Stepik с конструктором курсов, в экосистеме казахского языка.

Я практиковался с синтаксисом Python и философией FastAPI. В проекте использовалась базовая слоистая архитектура. Приложение осознанно сделано синхронным, дабы не усложнять процесс на этапе изучения.

**Используемые библиотеки:**
* **pydantic** — валидация данных и схемы
* **sqlalchemy** — ORM для работы с базой данных
* **openai** — модерация комментариев
* **groq** — запросы к LLM
* **sqladmin** — панель администратора
* **jose, dotenv, bcrypt** — авторизация, окружение и хеширование паролей

**REST API Эндпоинты:**
* **Auth & User:**
  * `GET /user/me`
  * `POST /auth/register`
  * `POST /auth/token`
* **Courses & Comments:**
  * `GET /courses`
  * `GET /courses/{id}`
  * `POST /courses`
  * `DELETE /courses/{id}`
  * `GET /courses/{id}/comments`
  * `POST /courses/{id}/comments`
* **Notes:**
  * `GET /notes`
  * `POST /notes`
  * `PUT /notes/{id}`
  * `DELETE /notes/{id}`
* **AI Chat:**
  * `POST /chat/` — чат с LLM через провайдер Groq API
* **History:**
  * `GET /history` — история посещенных пользователем курсов (таблица `history` со связью many-to-many)

**Слоистая архитектура проекта:**
* `api/` — эндпоинты (роуты) приложения
* `core/` — конфигурация и API-клиенты
* `db/` — инициализация базы данных и управление сессиями
* `services/` — бизнес-логика приложения
* `repositories/` — слой работы с БД (запросы)
* `schemas/` — Pydantic-схемы для валидации данных
* `models/` — SQLAlchemy-модели (структура таблиц)
* `exceptions/` — кастомные исключения
* `admin/` — конфигурация панели администратора

**Рефлексия:**
Стал лучше понимать FastAPI-подход и удобство этого фреймворка, а также то, насколько эффективно взаимодействуют между собой Pydantic, SQLAlchemy и FastAPI. Закрепил на практике принципы построения REST API и разделения ответственности между слоями архитектуры.

---
</details>

<details>
<summary>🇺🇸 English</summary>
<br>

My first backend project built with FastAPI. Connected frontend: [[github](https://github.com/shlekht/edu-platform-frontend)]. The core concept is a Stepik alternative featuring a course builder, tailored for the Kazakh language ecosystem.

I practiced Python syntax and the core philosophy of FastAPI. The project implements a traditional layered architecture. The application is intentionally synchronous to keep the focus on core concepts without adding unnecessary complexity.

**Libraries used:**
* **pydantic** (data validation and schemas)
* **sqlalchemy** (ORM for database interactions)
* **openai** (used for automated comment moderation)
* **groq** (handling requests to LLM)
* **sqladmin** (admin panel interface)
* **jose, dotenv, bcrypt** (authentication, environment variables, and password hashing)

**REST API Endpoints:**
* **Auth & User:**
  * `GET /user/me`
  * `POST /auth/register`
  * `POST /auth/token`
* **Courses & Comments:**
  * `GET /courses`
  * `GET /courses/{id}`
  * `POST /courses`
  * `DELETE /courses/{id}`
  * `GET /courses/{id}/comments`
  * `POST /courses/{id}/comments`
* **Notes:**
  * `GET /notes`
  * `POST /notes`
  * `PUT /notes/{id}`
  * `DELETE /notes/{id}`
* **AI Chat:**
  * `POST /chat/` — interactive AI chat via the Groq API provider
* **History:**
  * `GET /history` — user's course viewing history (backed by a many-to-many `history` table)

**Project Architecture:**
* `api/` — application endpoints and routing
* `core/` — configuration settings and API clients
* `db/` — database initialization and session management
* `services/` — core business logic layer
* `repositories/` — database access layer (data repository pattern)
* `schemas/` — Pydantic data validation schemas
* `models/` — SQLAlchemy database models
* `exceptions/` — custom exception definitions
* `admin/` — admin panel configuration layer

**Reflection / Lessons Learned:**
I gained a solid understanding of the FastAPI ecosystem and discovered how seamlessly FastAPI, Pydantic, and SQLAlchemy integrate with one another. I also reinforced my knowledge of REST API design principles and the separation of concerns across a layered architecture.

---
</details>
