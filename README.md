# Invera ToDo-List Challenge (Python/Django Jr-SSr)


> **_IMPORTANTE!!!:_**  EN EL ARCHIVO Consultas Insomnia.json SE ENCUENTRAN TODAS LAS CONSULTAS EN FORMATO JSON PARA IMPORTAR DIRECTAMENTE EN INSOMNIA Y HACER TODAS LAS CONSULTAS DESDE LA HERRAMIENTA DE PETICIONES

---

# Lenguaje y librerias usadas :notebook_with_decorative_cover:

<ol>
  <li>Python</li>
  <li>djangorestframework</li>
</ol>

# ¿Como levantar la api? :rocket:

Se debe crear un virtual env con las librerias colocadas en el archivo requirements.txt. 

Luego ejecutar estos comandos:

`python manage.py makemigration`
`python manage.py migrate`
`python manage.py runserver`

# ¿Como probar la api? :test_tube:

Se dejo un archivo .json con las consultas ya hechas en Insomnia. Solo debe importarse ese archivo en insomnia y las consultas pueden generarse desde ahi.

Tambien se pueden probar utilizando curl, estos son algunos ejemplos:

### Get list
`curl http://127.0.0.1:8000/todoList/`

### Insert List

`curl http://127.0.0.1:8000/todoList/ --request POST --header "Content-Type: application/json" --data "{\"description\":\"prueba\"}"`

### Delete Lista

`curl http://localhost:8000/deleteTodoList/1/ --request DELETE`


# ¿Como testear la aplicacion? :alembic:

Se debe ejecutar el comando 

`python manage.py test`

Dentro del archivo test que se encuentra en la carpeta todoList, se encuentran tests unitarios.

# ¿Como ejecutar el dockerfile? :whale:

Se dejo un Dockerfile para poder ejecutar la api en cualquier SO.
Se deben ejecutar los siguientes comandos:
`docker run -it nombreimagen .`
`docker build -t nombre_imagen`


# ¿Donde ver los logs? :notebook_with_decorative_cover:

Luego de ejecutar se vera un archivo debug.log



# ¿Donde ver la documentacion? :books:

Se documento siguiendo el esquema de OpenApi si se ingresa desde el navegador se puede ver la documentacion. Dentro del endpoint \doc se puede ver el esquema general de la api.