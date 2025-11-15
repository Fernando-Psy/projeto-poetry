FROM python:3.11-slim

WORKDIR /app

# Instala o Poetry
RUN pip install poetry
ENV PATH="{PATH}:/root/.local/bin"

# Instala as dependências do projeto
RUN poetry config virtualenvs.create false \
    && poetry install --only=main --no-root

RUN apt-get update && apt-get install -y \
    build-essential
    
# Copia apenas o necessário para instalar as dependências
COPY pyproject.toml poetry.lock ./

# Copia o restante do código do projeto
COPY . .

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "bookstore.wsgi:application", "--bind", "0.0.0.0:8000"]