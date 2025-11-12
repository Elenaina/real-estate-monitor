# =========================
#  STAGE 1: Builder
# =========================

FROM python:3.12-slim AS builder

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false

RUN poetry install --no-root --no-interaction --no-ansi

# =========================
#  STAGE 2: Runtime
# =========================

FROM python:3.12-slim

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local /usr/local
COPY src/ ./src/

ENV PYTHONBUFFERED=1 \
PYTHONWRITERBYTECODE=1 \
PIP_NO_CACHE_DIR=1

CMD ["uvicorn", "src.backend.main:app", "--host", "0.0.0.0", "--port", "800"]