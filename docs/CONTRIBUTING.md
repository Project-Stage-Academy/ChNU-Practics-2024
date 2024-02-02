# Contributing Guide

### Development setup

This will ensure your Django project is ready to be used locally.

## Table of Contents
- [Repository Setup](#repository-setup)
- [Dependency Setup](#dependency-setup)
- [Database Setup](#database-setup)
- [Run Docker locally](#run-docker-locally)
- [Testing Setup](#testing-setup)

### Repository Setup

As a first step, you'll need to clone the repository to your local machine:

```bash
git clone git@github.com:ivtka/Test-ChNU-Practics-2024.github
```

### Dependency Setup

After you've cloned the repository, you'll need to create and activate a git-ignored virtual env (venv or .venv), e.g.:

```bash
python3 -m venv .venv
source .venv/bin/activate # or .venv\Scripts\activate on Windows
```

Then, you'll need to install the dependencies, we using pyproject.toml for this:

```bash
pip install pip --upgrade
pip install -e .[dev] # Install dev dependencies
```

### Database Setup

As a first step, you'll need to create .env file in root directory and add there:

```bash
cp .env.example .env # or copy .env.example .env on Windows
```

Make sure you create `.env` and fill it the following variables:
```env
DJANGO_SECRET_KEY=fix_this_someday # Django secret key
DJANGO_SUPERUSER_EMAIL=hello@example.com # Django superuser email
DJANGO_SUPERUSER_USERNAME=admin # Django superuser username
DJANGO_SUPERUSER_PASSWORD=12345678 # Django superuser password
DJANGO_DEBUT=True # Enable Django debug mode

POSTGRES_DB=mydb # Postgres database
POSTGRES_USER=myuser # Postgres user
POSTGRES_PASSWORD=mysecretpassword # Postgres password
POSTGRES_HOST=localhost # Postgres host
POSTGRES_PORT=5432 # Postgres port
```

Once you have the above `.env` file, run the following command to start the database:
```bash
docker compose up -d db
```

This will create a postgresql database that's running in the background for you. To bring this database down just run:

```bash
docker compose down
```

### Run App locally with Docker

Run the following command to start the Django server:
```bash
docker compose up -d
```

Manually apply migrations:

```bash
docker compose exec -it djangoapp /app/migrate.sh
```

And go to the following URL to see the Django project running:
```bash
xdg-open http://localhost/
```

On windows you can use:
```powershell
start http://localhost/
```

### Testing Setup

Run tests:

```bash
pytest
```
