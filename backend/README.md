**WiP**
# Potential Pancakes - Backend

Este é o repositório da parte backend do projeto **Potential Pancakes**. O projeto esta em fase inicial de construcao

## Visão Geral

O projeto **Potential Pancakes** é uma plataforma [descreva brevemente o propósito do projeto]. A parte backend é responsável por gerenciar os dados, autenticação, e outras funcionalidades essenciais do sistema.

## Tecnologias Utilizadas

- Python 3.10
- Django Rest Framework
- Docker
- Docker-Compose
- Make

## Como Iniciar

Para iniciar o servidor backend em sua máquina, siga estas etapas:

1. Clone este repositório:

   ```bash
   $ git clone https://github.com/seu-usuario/potential-pancakes-backend.git

2. Garanta que o Make, Docker e o Docker-compose estejam instalados.
   ```bash
   $ docker --version
   $ docker-compose --version
   $ make --version

3. Execute os seguintes comandos:
- Cria containers 
```bash
make build-be
```
- Cria migrations
```bash
make makemigrations  
```
- Executa migrations
```bash
make migrate
```
- Criar um usuario
```bash
make createsuperuser
```
- Inicializa container, e executa serviço Django
```bash
make start
```
- Encerra execução dos containers BD e Django
```bash
make stop
```
##Como rodar no windows 
 https://ubuntu.com/download/desktop