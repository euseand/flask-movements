# flask-movements
flask based money movements app

## DB setup:

```
$ psql -U postgres
postgres=# create user <username> with createdb;
postgres=# CREATE DATABASE money_movements OWNER <username>;
postgres=# GRANT ALL PRIVILEGES ON DATABASE money_movements TO <username>;
```

# Inside of flask-movements/ dir:

## Install dependencies & activate virtualenv

```
$ mkdir .venv
$ pipenv install
$ pipenv shell
```

## Run migrations

```
$ bash db.sh
```

## Start app:

```
$ python3 wsgi.py
```
