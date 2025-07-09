FROM python:3.11-slim

# Configurar variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VENV_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PORT=8000

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN pip install poetry==$POETRY_VERSION

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock ./

# Configurar Poetry e instalar dependências
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-root \
    && rm -rf $POETRY_CACHE_DIR

# Copiar código da aplicação
COPY . .

# Instalar a aplicação
RUN poetry install --no-dev

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Criar usuário não-root
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expor porta (Heroku define automaticamente)
EXPOSE $PORT

# Comando para iniciar a aplicação
CMD gunicorn bookstore.wsgi:application --bind 0.0.0.0:$PORT --workers 3