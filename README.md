# Avito

## Run database (docker)

docker run --name hunting_db -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=user -e POSTGRES_DB=hunting -p 5432:5432 -d postgres:13.0-alpine