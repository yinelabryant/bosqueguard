# Tutorial para ejecutar Bosqueguard.

1. Una vez haces el pull, en la carpeta del respositorio, desde la terminal vas a ejecutar el siguiente comando:
`python -m venv venv` 
	* Esto crea un ambiente de desarrollo para que las librerias que instales, no se guarden directamente en tu pc, sino que se guarde en el ambiente. Es muy importante crear un ambiente cuando se trabaja con Django, pero se puede usar en cualquier proyecto.
2. Una vez se crep el ambiente, en la misma carpeta del repositorio ejecuta el siguiente comando para activarlo:
` .\venv\Scripts\activate`
	* Cuando actives el ambiente, en tu terminal va a aparecer (venv).
3.  Cuando ya el ambiente esté activado, desde phpMyAdmin vas a crear una BD con nombre `bosqueguard`, no agregues ninguna tabla, solamente la base de datos.
4.  Luego, en la carpeta del repositorio vas a crear un archivo llamado `.env`, aquí vas a agregar lo siguiente:
 ```
 DB_NAME  = bosqueguard

DB_USER  = nombredeusuariodeMySQL

DB_PASSWORD  = contraseñadetuMySQL
```
5.  Luego, desde la carpeta del repositorio, vas a ejecutar el siguiente comando:
`pip install -r requirements.txt`
6.  Por ultimo, entras a la carpeta bosqueguard y ejecutas:
`python manage.py migrate`
7. Para abrir la pagina, debes ejecutar:
`python manage.py runserver`

## Todos estos pasos solamente se ejecutan la primera vez que clonnas el repositorio, en una situación normal donde solo quieres ejecutarlo, solo debes hacer el paso 2 y 7.