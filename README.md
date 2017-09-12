# tdpii-TP1
Trabajo Práctico 1 de taller de proyecto 2

Integrantes:
- Antonella Andreini, 822/9
- Augusto Bonifacio, 751/1
- Brian Flores, 795/4
## Requisitos

- Python 2.7
- Pip
- Mysql

## Instalación

#### Crear la base de datos con sus tablas en mysql

``` sh
$ mysql -u root -p < schema.sql # root = usuario de tu base de datos
``` 

#### Instalar las dependencias (Flask y PyMysql)

``` sh
$ pip install -r requirements.txt
``` 

#### Editar el archivo db_conf.py con usuario y contraseña de la base de datos

#### Correr en ventanas separadas

``` sh
$ python clima.py
``` 

``` sh
$ FLASK_APP=server.py flask run
``` 

## Funcionamiento

Se usa una base de datos para evitar los problemas de concurrencia que pueden existir al leer y escribir un archivo mediante dos procesos independientes

### Clima.py
*Frecuencia de muestreo = segundos entre mediciones*

- Lee la frecuencia de muestreo (por defecto 10 segundos) desde la tabla *Configuracion*. 
- Inserta valores random a la base
- Se duerme tantos segundos como haya leido anteriormente

### Server.py

- **/** devulve el archivo index.html para que pueda ser interpretado por el navegador.

- **/api/clima** devulve la ultima medicion hecha desde la base de datos,

- **/api/frecuencia** [POST] hace un update sobre la tabla *Configuracion*.  

### Index

- El index hace la llamada ajax a **api/clima** cada 1 segundo para actualizar los datos.
- Mediante el formulario se puede cambiar la frecuencia con la que clima.py inserta en la base.
