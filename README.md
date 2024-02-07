# Test PG Vector

## Setup environment variables

Create a `.env` file including these variables:

```
POSTGRES_DRIVER=psycopg
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=test
POSTGRES_USER=example
POSTGRES_PASSWORD=example
OPENAI_API_KEY=<KEY>
```

## Start a PG Vector database

Using PG Vector Database from https://hub.docker.com/r/ankane/pgvector

Commands:

```
docker-compose up
```

## Run test

Commands:

```
virtualenv venv
source venv/bin/activate
pip install --upgrade pip
pip install --requirement requirements.txt
python main.py
```
