set FLASK_APP=api.py
set FLASK_DEBUG=1
set LOGGING_LEVEL=info
set FLASK_ENV=dev

CALL env\Scripts\activate

flask run --host=0.0.0.0 --port=5007