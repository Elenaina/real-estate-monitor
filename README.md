# 🏠 Real Estate Monitor

Backend application for collecting and exposing real estate listings data.

The project combines web scraping with a REST API to store and provide structured property data.

---

## 🚀 Features

- Scraping real estate listings from external sources  
- Parsing and normalizing property data  
- Storing data in a database (PostgreSQL + Alembic migrations)  
- REST API for accessing listings  
- Health check endpoint  
- Dockerized setup  

---

## 🛠 Tech Stack

- Python  
- FastAPI  
- asyncio / aiohttp  
- PostgreSQL  
- Alembic  
- Docker & Docker Compose  
- Poetry  

---

## ⚙️ Running the project

### Local (Poetry)

```bash
poetry install
poetry shell
uvicorn app.main:app --reload
```

### Docker
```bash
docker-compose up --build
```

### API Endpoints

GET /health – health check

GET /properties – list of properties

### Project Structure

src/
  app/        # FastAPI backend (API, DB, config)
  
  scrapers/   # scraping logic (fetching, parsing)
  
migrations/   # database migrations (Alembic)

docker/       # Docker configuration

### Purpose

The project was created to practice:

building backend services with FastAPI

working with asynchronous data fetching

designing simple data pipelines (scraping → processing → API)
