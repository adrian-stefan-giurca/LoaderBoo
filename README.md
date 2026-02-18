# LoaderBoo
LoaderBoo aims to be a web application used to download anime and music into a directory designed by the user

---

# Idea Inicial

Aplicación web que pueda ser utilizada para la descarga de episodios de anime y canciones de música, siendo esencialmente un wrapper de comandos CLI como yt-dlp y ani-cli. Además de esto se tiene que poder programar descargas futuras especificando dia, hora y cadencia de reintentos (minutos). Interesante mantener un registro de las descargas en forma de historial para mantener persistencia de las operaciones del sistema.

---

# Objetivo real del sistema

Funciones del sistema

1. Programar descargas de episodios de anime que van a salir próximamente especificando dia y fecha. 
2. Descargar el anime directamente desde la aplicación web. 
3. Buscar y descargar canciones de youtube

---

# Tecnologías

Se consideran las siguientes tecnologías para el desarrollo del sistema: 
1. **Python + FastAPI** para desarrollar backend que conecte el sistema con los comandos yt-dlp y ani-cli de forma adecuada.
2. **APScheduler** como módulo Python para implementar el módulo de *Scheduler* 
3. **SQLite** como base de datos para mantener la persistencia del historial.
4. **React [No defenitivo]** para desarrollar el frontend del sistema y desarrollar la UI.
5. **Nginx** como servidor web para poder exponer la aplicación web hacia la red local.
5. **Docker** como entorno de contenedores sobre el cual se va a instalar el sistema.

---

# Arquitectura 

La arquitectura actual del sistema se especifica en el archivo "System_Arquitecture v1.0.excalidraw"

---

# Nivel de complejidad estimado de las tareas

**Leyenda:**
🟢 Fácil
🟡 Media
🟠 Avanzadillo

1. 🟡 Bloque Anime Downloader a través de anipy-api: Desarrollo módulos anime_search() y anime_downloader()
2. 🟢 Bloque Music Downloader a través de yt-dlp: Desarrollo módulo music_downloader()
3. 🟢 Exponer los bloques de Backend a través de FastAPI
3. 🟢 Bloque Scheduler
4. 🟡 UI en React básica (Únicamente módulos descargas)
5. 🟠 Terminar UI React (Módulo Scheduler + extras)

# Secuencia de eventos en la aplicación

El flujo básico de la aplicación es el siguiente: 
## Caso descarga de Anime

1. Iniciar aplicación: Acceder IP_server:80 en un navegador
2. Seleccionar opción Anime Downloader
3. Buscar y seleccionar anime y rango de episodios 
4. Descargar anime

## Caso descarga de canción de YouTube

1. Iniciar aplicación: Acceder IP_server:80 en un navegador
2. Seleccionar opción Music Downloader
3. Pegar link en la app 
4. Descargar canción

## Caso Extra: Visualización de historial 

1. Iniciar aplicación: Acceder IP_server:80 en un navegador
2. Seleccionar opción Music Downloader
3. Se mostrarán los registros de la base de datos en la app

