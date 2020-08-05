


Github link to push  


Server side AI based chess game.


# Install & Set Up
- Set up virtual environment

- Clone it from the Git, 
- Install the project dependencies,
 
```bash
pip install virtualenv
virtualenv venv
souce venv/bin/activate
pip install requirements.txt 
``` 

## Environment Set Up
Run in project terminal

Local env:
```bash
export DJANGO_SETTINGS_MODULE=django_chess.settings.localdev
```

Production env:
```bash
export DJANGO_SETTINGS_MODULE=django_chess.settings.production
```

## Run 
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
 

 
