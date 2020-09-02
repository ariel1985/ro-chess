JWT Authentication
  - [JWT django react auth Tutorial](https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a)
  - [JWT django react auth video](https://www.youtube.com/watch?v=0fb7zvUovPQ)

# About
Server side AI based chess game. Client [_](https://github.com/ariel1985/chess-client)

# Install & Set Up

## Python Virtual Environment Set Up
```bash
pip install virtualenv
virtualenv venv
souce venv/bin/activate
``` 

## Install the project dependencies:
```bash
pip install requirements.txt
```

## Django Environment Configurations
**Run in terminal** inside virtual environment.
 
Local Env:
```bash
export DJANGO_SETTINGS_MODULE=django_chess.settings.localdev
```
Production Env:
```bash
export DJANGO_SETTINGS_MODULE=django_chess.settings.production
```
For a more permenant solution edit file _/manage.py_:
```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_chess.settings.localdev")
```

### Database Set Up
```bash
python manage.py makemigrations
python manage.py migrate
```


# Run 
```bash
python manage.py runserver
```
 

 
