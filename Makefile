default: 
	@echo "Comandos disponíveis"
	@echo "make build           - Cria containers caso não os tenha, ou caso modifique .env.dev"
	@echo "make makemigrations  - Cria migrations"
	@echo "make migrate         - Executa migrations"
	@echo "make createsuperuser - Criar um usuario"
	@echo "make start           - Inicializa container, e executa serviço Django"
	@echo "make stop            - Encerra execução dos containers BD e Django"
	@echo "make test            - Fazer teste com o pytest"
	@echo "make lint            - Organiza o codigo"
	@echo "make black           - Black é um formatador de código Python que segue a PEP 8,"
	@echo "make isort           - Classifica automaticamente as importações em um arquivo de código Python"
	@echo "make flake8          - O Flake8 é um linter de código Python que verifica o estilo e a qualidade do código"
	@echo "make pre             - Pre analise do codigo antes do commit, Isort, Black Flake8 e um teste de coverage"

build:
ifeq ("$(wildcard .env.dev)","") 
	cp .env.dev-example .env.dev
	@echo "#####____________________________________________________________________Novo arquivo .env.dev criado" 
endif
	docker-compose -f docker-compose.yaml --env-file=.env.dev up -d --build

makemigrations:
	docker exec -ti backend_potential_pancake python ./app/manage.py makemigrations

migrate:
	docker exec -ti backend_potential_pancake python ./app/manage.py migrate

start:
	docker-compose -f docker-compose.yaml start
	docker exec -ti backend_potential_pancake python ./app/manage.py runserver 0.0.0.0:8000

stop:
	docker-compose -f docker-compose.yaml stop 

test:
	docker exec -ti web_ingresso_dev  pytest . --cov-report term --cov=. --cov-fail-under=80