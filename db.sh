export FLASK_APP=wsgi.py
export FLASK_ENVIRONMENT=development
export FLASK_DEBUG=1

flask db init
flask db migrate
flask db upgrade
