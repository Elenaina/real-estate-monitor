# =========================
#  STAGE 1: Builder
# =========================

FROM python:3.12-slim AS builder

WORKDIR /src

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --target=/install -r requirements.txt

RUN find /install -name "tests" -type d -exec rm -rf {} + \
    && find /install -name "__pycache__" -type d -exec rm -rf {} + \
    && rm -rf /install/*.dist-info/*-info/INSTALLER


# =========================
#  STAGE 2: Runtime
# =========================

FROM python:3.12-slim

WORKDIR /src
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local/lib/python3.12/site-packages
COPY src/ ./src/

ENV PYTHONBUFFERED=1 \
PYTHONWRITERBYTECODE=1 \
PIP_NO_CACHE_DIR=1

CMD ["uvicorn", "src.main:src", "--host", "0.0.0.0", "--port", "800"]