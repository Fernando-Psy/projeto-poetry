FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

# Debug: Listar arquivos antes da cópia
RUN ls -la .

# Copiar apenas o necessário primeiro
COPY pyproject.toml poetry.lock ./

# Debug: Listar arquivos após a cópia
RUN ls -la /app

# Instalar dependências
RUN set -eux; \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Agora copiar o restante do código
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]