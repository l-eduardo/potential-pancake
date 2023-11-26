# Use uma imagem oficial de Python como base
FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

RUN groupadd app && useradd app -g app 

# Instala as dependências do PostgreSQL
RUN apt-get update \
  && apt-get install -y gcc \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Atualiza o pip
RUN pip install --upgrade pip

# Copia o arquivo de requerimentos e instala as dependências
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copia o projeto
COPY . /app

EXPOSE 8000:8000

RUN python manage.py makemigrations \
  python manage.py migrate