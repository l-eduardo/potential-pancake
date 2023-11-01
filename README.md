# Instruções para Executar a Aplicação Django e React

Este README fornece instruções para executar sua aplicação que utiliza Django como backend e React como frontend. O processo de execução é simplificado usando um Makefile.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas e dependências instaladas em seu sistema:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Make

## Configuração

1. Clone o repositório da aplicação para o seu computador.

2. Navegue até o diretório raiz da aplicação.

3. Renomeie o arquivo `.env.example` em `backend` para `.env` e configure as variáveis de ambiente necessárias para a configuração do Django.


## Rodar a aplicação

```bash
make run
```

## Comandos backend

- Builda imagem e cria container
```bash
make build-be
```

- Cria e executa as migrations
```bash
make makemigrations-be
make migrate-be
```

- Cria um usuário de administração
```bash
make createsuperuser-be  # (Opcional: criar um superusuário)
```

- Para o container
```bash
make stop-be
```

- Para e deleta o container
```bash
make down-be
```
## Comandos Frontend
### Para criar e executar o servidor de desenvolvimento

- Builda imagem e cria container
```bash
make build-fe
```

- Starta o container
```bash
make start-fe
```

- Para o container
```bash
make stop-fe
```

- Deleta o container
```bash
make down-fe
```

# Recomendações p/ rodar no Windows
- Instale o [WSL]https://learn.microsoft.com/pt-br/windows/wsl/install
- Siga os passos descritos anteriormente.