# About
Server side AI based chess game.

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
 

 
