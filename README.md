## flask-movements
flask based money movements app

# DB setup:

```
$ psql -U postgres
postgres=# create user <username> with createdb;
postgres=# CREATE DATABASE money_movements OWNER <username>;
postgres=# GRANT ALL PRIVILEGES ON DATABASE money_movements TO <username>;
```

# Inside of flask-movements/ dir:

```
$ mkdir .venv
$ pipenv install
$ pipenv shell
$ bash db.sh
```

# Start app:

```
$ bash start.sh
```
