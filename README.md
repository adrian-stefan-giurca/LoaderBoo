# LoaderBoo
LoaderBoo aims to be a web application used to download anime and music into a directory designed by the user

---

# Idea Inicial

Aplicación web que pueda ser utilizada para la descarga de episodios de anime y canciones de música, siendo esencialmente un wrapper de comandos CLI como yt-dlp y ani-cli. Además de esto se tiene que poder programar descargas futuras especificando dia, hora y cadencia de reintentos (minutos). Interesante mantener un registro de las descargas en forma de historial para mantener persistencia de las operaciones del sistema.

---

# Objetivo real del sistema

Funciones del sistema

1. Programar descargas de episodios de anime que van a salir próximamente especificando dia y fecha. 
2. Buscar y descargar el anime directamente desde la aplicación web. [Funcional versión 0.1]
3. Buscar y descargar canciones de youtube.

---

# Tecnologías

Se consideran las siguientes tecnologías para el desarrollo del sistema: 
1. **Python + FastAPI** para desarrollar backend que conecte el sistema con los comandos yt-dlp y ani-cli de forma adecuada.
2. **APScheduler** como módulo Python para implementar el módulo de *Scheduler* 
3. **SQLite** como base de datos para mantener la persistencia del historial.
4. **Vue** para desarrollar el frontend del sistema y desarrollar la UI.
5. **Nginx** como servidor web para poder exponer la aplicación web hacia la red.
5. **Docker** como entorno de contenedores sobre el cual se va a instalar el sistema.

---

# Arquitectura 

La arquitectura actual del sistema se especifica en el archivo "System_Arquitecture v1.0.excalidraw"

---

# Instalación el proyecto

## Prerequisitos en el sistema

Para instalar y ejecutar LoaderBoo, en necesario tener un sistema que tenga instaladas las siguientes dependencias:
- Manejador de paquetes de Javascript [npm](https://www.npmjs.com/)
- [Docker](https://www.docker.com/) 
- [Docker Compose](https://github.com/docker/compose)

## Instrucciones

Los pasos para instalar el proyecto hasta el momento consisten en:
1. Clonar este repositorio de GitHub
2. Instalar los paquetes del frontend necesarios para buildear LoaderBoo UI
3. Buildear una versión de producción de LoaderBoo UI
4. Buildear el sistema mediante docker compose
5. Ejecutar el sistema mediante docker compose

A continuación se proporcionan las siguientes instrucciones en linea de comandos:

```bash
git clone https://github.com/adrian-stefan-giurca/LoaderBoo.git
cd LoaderBoo/src/loaderboo_ui
npm install 
npm run build
cd ../../
docker compose build
docker compose up -d    # modo detached 
```

## Consideraciones 

Dentro de docker-compose.yaml se pueden modificar los directorios de descarga tanto de anime como de música: 

```yaml
services:
  api:
    build: 
      context: ./src/loaderboo_api/
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ./src/loaderboo_api/src:/code/app
      - ./media/:/media     # <- parte izquierda directorio en el host
      - ./music/:/music     # <- parte derecha directorio dentro del contenedor

...
```

Para ello basta con introducir la ruta que se prefiera a la izquierda de los ':'. 

Por ejemplo, para modificar el directorio original ```./media``` a ```/home/user/Desktop/media```:

```yaml
services:
  api:
    build: 
      context: ./src/loaderboo_api/
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ./src/loaderboo_api/src:/code/app
      - /home/user/Desktop/media:/media     
      - ./music/:/music     

...
```
