# Thegame: Página de Videojuegos - Consolas Retro y Juegos Indie

## 🎮 Descripción del Proyecto

Este proyecto es una página web dedicada a los **videojuegos retro** y **juegos indie**. La plataforma permite a los usuarios explorar una colección curada de títulos clásicos y descubrir nuevas joyas dentro del mundo de los juegos independientes. Además, cuenta con **salas de chat temáticas** donde los usuarios pueden discutir sobre sus juegos favoritos y conectar con otros fanáticos.

## 🚀 Características

- **Catálogo de Juegos Retro**: Navega por una colección de juegos de consolas retro como NES, SNES, Sega Genesis, entre otros.
- **Juegos Indie**: Descubre y juega a títulos indie únicos creados por desarrolladores independientes.
- **Perfil de Usuario**: Los usuarios pueden crear un perfil, agregar sus juegos favoritos y dejar reseñas.
- **Sistema de Comentarios y Likes**: Interactúa con la comunidad dejando comentarios y dando likes a tus juegos preferidos.
- **Upload de Juegos Indie**: Los desarrolladores pueden subir sus propios juegos indie para que la comunidad los descubra.
- **Salas de Chat Temáticas**: Únete a conversaciones en tiempo real sobre tus juegos y consolas favoritas en nuestras salas de chat.

## 🛠️ Tecnologías Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (con uso de JQuery para interacción dinámica).
- **Backend**: Django con Python.
- **Base de Datos**: sqlite3.
- **Autenticación**: Django Allauth para la gestión de usuarios.
- **Websockets**: Django Channels para soporte de chats en tiempo real.
- **Despliegue**: Render para la aplicación y Google Cloud Storage para archivos estáticos y multimedia.

## 📦 Instalación y Configuración

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/xXJuanDavidXx/Thegame.git
    ```

2. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Realiza las migraciones de la base de datos:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Inicia el servidor de desarrollo:**

Recuerda primeramente configurar el `ALLOW_HOSTS` en settings
   

```bash
    python manage.py runserver
```

5. **Iniciar un servidor redis para la cominicación websocket**
	```bash
   sudo docker run -d -p 6379:6379 --name redis redis 
	```


## 🚧 Estado del Proyecto

Actualmente, el proyecto está en desarrollo activo. Planeo agregar nuevas características como:

- **Implementación de juegos web con js** para juegos indie.

## 📧 Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

- **Email**: [juandavidjaramillo456@gmail.com](mailto:juandavidjaramillo456@gmail.com)

¡Gracias por visitar mi proyecto!

