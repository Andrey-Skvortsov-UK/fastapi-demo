# fastapi-demo

## Getting started


### Create Alembic migrations
```
alembic init alembic
alembic revision --autogenerate -m "First migration"
```

### Apply migrations
run
```
docker-compose run web alembic upgrade head
```
or run locally
```
alembic upgrade head
```

## Run server
```
uvicorn demo:app --reload
```

## Test API
http://127.0.0.1:8000/docs#

## Browse Postgres DB
http://localhost:5050/browser/
use these credentials to login: `pgadmin4@pgadmin.org`:`admin`


### Setup Docker on Windows
in PowerShell run:
```
>> [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
>> Invoke-WebRequest "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-Win
dows-x86_64.exe" -UseBasicParsing -OutFile $Env:ProgramFiles\Docker\docker-compose.exe
```
