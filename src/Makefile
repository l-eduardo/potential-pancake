BE := backend
FE := frontend
default: 
	@echo "Comandos disponíveis"
	@echo "make build           - Cria containers caso não os tenha, ou caso modifique .env"
	@echo "make makemigrations  - Cria migrations"
	@echo "make migrate         - Executa migrations"
	@echo "make createsuperuser - Criar um usuario"
	@echo "make start           - Inicializa container, e executa serviço Django"
	@echo "make stop            - Encerra execução dos containers BD e Django"backend 

### BACKEND ###
build:
	docker-compose -f docker-compose.yaml --env-file=.env up -d --build

makemigrations:
	docker exec -ti backend_potential_pancake python manage.py makemigrations

migrate:
	docker exec -ti backend_potential_pancake python manage.py migrate

createsuperuser:
	docker exec -ti backend_potential_pancake python manage.py createsuperuser

start:
	docker-compose -f docker-compose.yaml start
	docker exec -ti backend_potential_pancake python manage.py runserver 0.0.0.0:8000

stop:
	docker-compose -f docker-compose.yaml stop

down:
	docker-compose -f docker-compose.yaml down