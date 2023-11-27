**WiP**
# Potential Pancakes


Este repositório contém o trabalho final da disciplina de Programação Web (INE5646), que se trata de um sistema de gerenciamento de listas de tarefas. No contexto desse sistema, os usuários têm a capacidade de criar "cards", nos quais podem adicionar e gerenciar as tarefas a serem concluídas. Além disso, o sistema incorpora as seguintes funcionalidades:
 - Autenticação e autorização de usuários; 
 - Compartilhamento de listas de tarefas entre os usuários baseado em grupos de permissões (roles);
 - Disponibilidade em um servidor 24/7: https://potential-pancake-production.up.railway.app/;
 - Layout responsivo.

## Integrantes
 - Abmael Batista da Silva (22203744)
 - Henrique Silveira Sato (22201631)
 - Jader Theisges (22215141)
 - Luiz Eduardo da Silva (22202683)
 - Vitor Werle Rempel (22201643)

## Tecnologias Utilizadas

- Python 3.10
- Django
- Docker
- Docker-Compose
- Make

## Como Iniciar

Para iniciar a aplicação em sua máquina, siga as etapas a seguir:

1. Clone este repositório:

   ```bash
   $ git clone https://github.com/seu-usuario/potential-pancakes-backend.git

2. Garanta que o Make, Docker e o Docker-compose estejam instalados.
   ```bash
   $ docker --version
   $ docker-compose --version
   $ make --version

3. Inicialize a aplicação:
   ```bash
   $ make build
   ```
  
## Comandos de configuração
- Cria as migrações
    ```bash
    $ make makemigrations
    ```
- Executa as migrações
    ```bash
    $ make migrate
    ```
- Criar um usuario admin
    ```bash
    $ make createsuperuser
    ```
- Encerra execução dos containers
    ```bash
    $ make stop
    ```
- Remove os containers
    ```bash
    $ make down
    ```

## Como rodar no windows 
 https://ubuntu.com/download/desktop