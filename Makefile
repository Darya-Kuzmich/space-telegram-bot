.PHONY:
help:
	@echo 'build-up'
	@echo 'dev-build-up'
	@echo 'redis-cli'
	@echo 'logs'
	@echo 'stop'
	@echo 'start'
	@echo 'restart'
	@echo 'down'
	@echo 'login-bot'
	@echo 'login-redis'
build-up:
	docker-compose -f docker-compose.yml up -d --build
dev-build-up:
	docker-compose -f docker-compose-dev.yml up -d --build
redis-cli:
	docker-compose -f docker-compose.yml exec space-redis redis-cli -h space-redis
logs:
	docker-compose -f docker-compose.yml logs --tail=100 -f $(c)
stop:
	docker-compose -f docker-compose.yml stop $(c)
start:
	docker-compose -f docker-compose.yml start $(c)
restart:
	docker-compose -f docker-compose.yml stop $(c)
	docker-compose -f docker-compose.yml up -d $(c)
down:
	docker-compose -f docker-compose.yml down $(c)
login-bot:
	docker-compose -f docker-compose.yml exec space-bot sh
login-redis:
	docker-compose -f docker-compose.yml exec space-redis sh
