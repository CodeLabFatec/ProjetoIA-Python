export FLASK_APP=api.py
export FLASK_DEBUG=1
export LOGGING_LEVEL=info
export FLASK_ENV=dev

source env/bin/activate

flask run --host=0.0.0.0 --port=5007