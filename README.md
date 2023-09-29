# TIF_Backend_Flaskapp
# Proyecto Integrador: Aplicación de Mensajería Similar a Discord

## Requerimientos Generales 🚀

1.  **Registro de Usuarios:** Este proyecto tiene como objetivo desarrollar una aplicación web para un sistema de mensajería, similar a Discord. La aplicación debe permitir a los usuarios registrarse en la plataforma proporcionando información como nombre de usuario, contraseña y otros datos relevantes. La selección de la imagen de perfil se realizará después del registro. 📝
    
2.  **Inicio de Sesión:** Los usuarios podrán iniciar sesión en sus cuentas de usuario. Si no tienen una cuenta, se les ofrecerá la opción de registrarse.🔐
    
3.  **Pantalla Principal:** Al iniciar sesión, se mostrarán tres columnas en la pantalla principal:
    
    -   **Columna de Servidores:** La primera columna presentará una lista de servidores a los que el usuario pertenece. Si no pertenece a ningún servidor, se mostrará un mensaje indicándolo. Se incluirá un botón para crear un nuevo servidor.🏰
    -   **Columna de Canales:** La segunda columna mostrará una lista de canales del servidor seleccionado (si lo hay). Si no existen canales, se mostrará un mensaje. También incluirá un botón para crear un nuevo canal.📢
    -   **Columna de Mensajes:** La tercera columna mostrará los mensajes en un chat, con los mensajes más recientes en la parte inferior. Si no hay mensajes, se mostrará un mensaje indicando que el chat está vacío. Habrá un cuadro de texto para escribir nuevos mensajes.💬
4.  **Modificación de Mensajes:** Solo el usuario que creó un mensaje podrá modificarlo o eliminarlo.✏️🗑️
    
5.  **Perfil de Usuario:** Los usuarios podrán acceder a su perfil, donde podrán actualizar sus datos personales y su imagen de perfil.🖼️
    
6.  **Manejadores de Errores:** Implementación de manejadores de errores personalizados para los códigos de estado HTTP 400, 404, 403 y 500.🚧
    
7.  **Búsqueda de Servidores:** Búsqueda de servidores por nombre, mostrando resultados coincidentes junto con su descripción (si la tienen) y la cantidad de usuarios registrados en cada servidor.🔍
    
8.  **Gestión de Sesiones:** Gestión de sesiones de usuario y restricción de acceso a endpoints de la API REST solo para usuarios autenticados.🔒
    
9.  **Notificaciones e Invitaciones:** Notificaciones e invitaciones a servidores.📨
    
### DER

![DER](https://i.ibb.co/Dk8Zg1x/derc1g3.png)

## Tecnologías Utilizadas 🛠️

- Lenguaje de programación: Python
- Framework web: Flask
- Base de datos: MySQL
- Frontend: HTML, CSS, JavaScript

## Estructura de Directorios

![ESTRUCTURA](https://i.ibb.co/WFzCpCh/estructuradecarpetas.png)


## Instalación y Ejecución ⚙️

Para ejecutar la aplicación, sigue estos pasos:

1. Clona este repositorio en tu máquina local. 📦
2. Crea un entorno virtual para el proyecto e instala las dependencias del archivo `requirements.txt`. 🐍
3. Configura la base de datos en `configuracion.py`. 🛠️
4. Ejecuta la aplicación utilizando el comando `python run.py`. ▶️



