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
