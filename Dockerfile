# Pull base image
FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

RUN apt-get update
RUN apt-get install -y curl

# copy poetry files
COPY poetry.lock pyproject.toml /code/

# install poetry, dependencies, then remove poetry
RUN pip --no-cache-dir install poetry poetry-setup \
    && poetry config virtualenvs.create false \
    && poetry install \
    && pip uninstall poetry -y \
    && rm -rf ~/.config/pypoetry

COPY . /code/

EXPOSE 8000 5433
