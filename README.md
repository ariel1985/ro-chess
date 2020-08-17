


Github link to push  


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
Local env:
```bash
export DJANGO_SETTINGS_MODULE=django_chess.settings.localdev
```
Production env:
```bash
export DJANGO_SETTINGS_MODULE=django_chess.settings.production
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
 

 
