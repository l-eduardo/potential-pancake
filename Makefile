BE := ./backend
FE := ./frontend
default: 
	@echo "Comandos disponíveis"
	@echo "make build-be           - Cria containers caso não os tenha, ou caso modifique .env"
	@echo "make makemigrations-be  - Cria migrations"
	@echo "make migrate-be         - Executa migrations"
	@echo "make createsuperuser-be - Criar um usuario"
	@echo "make start-be           - Inicializa container, e executa serviço Django"
	@echo "make stop-be            - Encerra execução dos containers BD e Django"backend 

### BACKEND ###
build-be:
	docker-compose -f ${BE}/docker-compose.yaml --env-file=${BE}/.env up -d --build

makemigrations-be:
	docker exec -ti backend_potential_pancake python manage.py makemigrations

migrate-be:
	docker exec -ti backend_potential_pancake python manage.py migrate

createsuperuser-be:
	docker exec -ti backend_potential_pancake python manage.py createsuperuser

start-be:
	docker-compose -f docker-compose.yaml start
	docker exec -ti backend_potential_pancake python manage.py runserver backend 0.0.0.0:8000

stop-be:
	docker-compose -f ${BE}/docker-compose.yaml stop

### FRONTEND ###
build-fe:
	docker-compose -f ${FE}/docker-compose.yaml up -d --build

start-fe:
	docker-compose -f ${FE}/docker-compose.yaml start
	docker exec -ti frontend_potential_pancake npm run dev

stop-fe:
	docker-compose -f ${FE}/docker-compose.yaml down

## GENERAL ##

build:
	${MAKE} build-fe && ${MAKE} build-be

start:
	${MAKE} start-fe && ${MAKE} start-be

start:
	${MAKE} stop-fe && ${MAKE} stop-be
