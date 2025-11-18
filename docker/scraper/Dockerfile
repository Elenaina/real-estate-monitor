FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1


WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    ca-certificates \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libdrm2 \
    libxcb1 \
    libxkbcommon0 \
    libxdamage1 \
    libxfixes3 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libasound2 \
    fonts-unifont \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry "playwright==1.49.0"

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --only scraper --no-interaction --no-ansi

RUN playwright install chromium

COPY . .

CMD ["poetry", "run", "python", "src/scrapers/main.py"]