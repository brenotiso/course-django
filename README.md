# Mini curso de Django
Mini curso apresentado aos trainees 2019/2 da Emakers Júnior.

## Tecnologias utilizadas
* Django 2.2
* Python 3.5+
* Postgres 9+

## Instalação

- Executando no Linux:

```sh
virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

- Executando no Windows:

```sh
virtualenv -p py env

env/Scripts/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```
