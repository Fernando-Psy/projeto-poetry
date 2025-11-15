FROM python:3.12-slim

WORKDIR /app

# Instala dependências do sistema (se precisar)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instala o Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Adiciona o poetry ao PATH (caso necessário)
ENV PATH="/root/.local/bin:${PATH}"

COPY pyproject.toml poetry.lock ./

# Instala libs sem criar virtualenv
RUN poetry config virtualenvs.create false
RUN poetry install --only=main --no-root

# Copia o restante
COPY . .

CMD ["gunicorn", "seu_projeto.wsgi"]
