# Empleados App
App de Empleados con Django

# Get Started:

Instalar dependencias:
```
pipenv install
```

Crear el .env
```
cp .env.dist .env

# Modificar los valores si es necesario
```

Crear migraciones:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Ejecutar servidor local
```
python manage.py runserver --settings=empleados.settings.local
```

##### Made with ❤️ by Leandro Arturi
