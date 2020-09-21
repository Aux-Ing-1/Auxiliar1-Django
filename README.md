# Auxiliar2-Django
## Configuración del ambiente de trabajo
El primer paso en esta auxiliar será crear un ambiente virtual donde estará toda la configuración de Python 
para este proyecto en específico. 
Dado que DjangoGirls explica muy bien cómo hacer esto, debes seguir los pasos de [este tutorial](https://tutorial.djangogirls.org/es/django_installation/) hasta donde activan el ambiente virtual. 
Al tener el ambiente virtual activado, vuelve aquí para el siguiente paso. 

## Descargar e instalar TODO Project 
En la auxiliar de hoy no vas a comenzar un proyecto de Django desde 0 
sino que usarás un proyecto que ya está configurado con lo básico para crear el **TODO Project**.  

1. 
    La primera tareas es hacer Fork y Clone de [este repositorio](https://github.com/Aux-Ing-1/Auxiliar2-Django). 
    > Si no recuerdas como hacerlo puedes revisar la [auxiliar de GIT](https://github.com/Aux-Ing-1/Auxiliar1-GIT). 
2. 
    Para entrar a la carpeta donde está el proyecto hay que hacer `cd Auxiliar2-Django` en la consola. 
3. 
    Para poder utilizar esta app hay que instalar los paquetes que el proyecto requiere. 
    Para esto instalaremos la lista de paquetes que viene en el archivo `requirements.txt` con el siguiente comando: 
    ```
   pip install -r requirements.txt
   ```
4. 
    Habiendo configurado el proyecto en tu computador deberías poder acceder a la aplicación web con el siguiente comando:
    ```
   python manage.py runserver
   ```   
   Al entrar a `http://127.0.0.1:8000/` deberías ver lo siguiente: 
   ![Proyecto instalado](proyecto_instalado.png) 

5. 
    La estructura de las carpetas debería quedar así:
    ``` 
    Auxiliar2-Django
    ├───manage.py
    ├───TODOproject
    │   │ settings.py
    │   │ urls.py
    │   │ wsgi.py
    │   │ __init__.py
    ├───db.sqlite3
    ├───README.md
    └───requirements.txt 

    ```    
          
## Crear una nueva app: todoapp 
Como se explicó en la clase Django está compuesto por apps que forman las diferentes partes de la aplicación web. 
Para esta auxiliar solo haremos una app con toda la funcionalidad. Esta se llamará **todoapp**. 

1. **Crear la app**

    Lo primero será crear la app. Para eso haremos el siguiente comando en la consola: 
    ```
   python manage.py startapp todoapp
   ```
   > Dato: se recomienda que en el nombre de la app solo hayan minúsculas, 
   >y se puede utilizar _ para hacer el nombre mas legible.  
   >Para mas guías de estilo para python puedes revisar [PEP 8](https://www.python.org/dev/peps/pep-0008/)
    *  
        La estructura de las carpetas debería quedar así:
        ```
        Auxiliar2-Django
        ├───manage.py
        ├───TODOproject
        │   ├───settings.py
        │   ├───urls.py
        │   ├───wsgi.py
        │   ├───__init__.py
        ├───todoapp
        │   ├───admin.py
        │   ├───apps.py
        │   ├───models.py
        │   ├───tests.py
        │   ├───views.py
        │   ├───__init__.py
        ├───db.sqlite3
        ├───README.md
        └───requirements.txt 
        ```                                                                                                                                                                
2. **Agregar la app a installed_apps**

    Para que el project sepa que existe esta nueva app hay que agregarla a `installed_apps` en el archivo `settings.py` de `TODOproject`. 
    
    Primero tienes que importar la app al inicio del archivo `settings.py` así : 
        ```import todoapp```
    
    Y luego agregarla a la variable `installed_apps` para que quede así:
    ```
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todoapp',
    ]
   ```        
3. 
   
                                                                                                                                                          