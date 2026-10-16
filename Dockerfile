# Usa uma imagem oficial do Python, versão slim para ser mais leve
FROM python:3.12-slim

# Evita a criação de arquivos .pyc e força o log direto no terminal (sem buffer)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala dependências do sistema operacional necessárias (como o compilador para o psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o requirements.txt e instala as dependências do Python
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante do código do projeto para o diretório de trabalho
COPY . /app/