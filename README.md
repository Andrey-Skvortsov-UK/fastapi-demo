# fastapi-demo

## Getting started

The purpose of the project to experiment with async FastAPI framework.
- to create simple crud api
- use SQLAlchemy as BD backend
- find how to manage migrations in SQLAlchemy
- simplify SQLAlchemy ORM usage
- run docker over poetry


What is used?
- [poetry] for dependency management.
- [FastAPI] as a web server
- [alembic] as a db migration tool
- [fastapi-sqlalchemy] for integration SQLAlchemy into FastAPI
- [sqlalchemy_mixins] to able use Django-like queries for SQLAlchemy


## How to
### Create Alembic migrations
```
alembic init alembic
alembic revision --autogenerate -m "First migration"
```

### Apply migrations
in docker
```
docker-compose run web alembic upgrade head
```
locally
```
alembic upgrade head
```

### Build docker containers
```
docker-compose run up --build --force-recreate
```

### Run server
in docker
```
docker-compose run web uvicorn demo:app --host 0.0.0.0 --port 8000 --reload
```
locally
```
uvicorn demo:app --reload
```

### Setup Docker on Windows
in PowerShell run:
```
>> [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
>> Invoke-WebRequest "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-Win
dows-x86_64.exe" -UseBasicParsing -OutFile $Env:ProgramFiles\Docker\docker-compose.exe
```


## Test API
http://127.0.0.1:8000/docs#

## Browse Postgres DB
http://localhost:5050/browser/
use these credentials to login: `pgadmin4@pgadmin.org`:`admin`

#### Useful links:
- [FastAPI with SQLAlchemy, PostgreSQL and Alembic and of course Docker](https://medium.com/@ahmed.nafies/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396)
- [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/)
- [Как я SQLAlchemy удобной сделал](https://habr.com/ru/post/324876/)


[poetry]: https://python-poetry.org/docs/
[FastAPI]: https://fastapi.tiangolo.com/
[alembic]: https://alembic.sqlalchemy.org/en/latest/
[fastapi-sqlalchemy]: https://pypi.org/project/FastAPI-SQLAlchemy/
[sqlalchemy_mixins]: https://github.com/absent1706/sqlalchemy-mixins