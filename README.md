# FastAPI - API con Versiones y Autenticación JWT en Cookies

Este proyecto es una API RESTful construida con FastAPI, que implementa un sistema de autenticación utilizando JSON Web Tokens (JWT) almacenados en cookies. La API permite la gestión de sesiones de usuario, renovación de tokens y validación de los mismos, con soporte para múltiples versiones de la API. La versión 2 añade un campo adicional al modelo de usuario para permitir la inclusión de información extra durante el registro.

## Estrategia Utilizada

La arquitectura de la aplicación sigue los principios SOLID para asegurar una correcta separación de responsabilidades y una estructura escalable. Las principales estrategias utilizadas son:

- Autenticación JWT: Se utiliza JWT para gestionar la autenticación y las sesiones de usuario. Los tokens de acceso y actualización se almacenan en cookies seguras.
- Versionado de la API: Se implementa un sistema de versionado para que los cambios en la API no afecten a los clientes existentes. Actualmente, se soportan las versiones v1 y v2.
- Separación de responsabilidades: Se sigue el principio de Responsabilidad Única para dividir las funciones en servicios, modelos, api lo que facilita el mantenimiento y la escalabilidad.

## Endpoints

### La API ofrece los siguientes endpoints:

### POST /api/v1/auth/register (v1)

* Descripción: Registra un nuevo usuario.
* Parámetros: name, email, password
* Respuesta: Devuelve los datos del usuario registrado.

### POST /api/v2/auth/register (v2)

* Descripción: Registra un nuevo usuario.
* Parámetros: name, email, password, age
* Respuesta: Devuelve los datos del usuario registrado.

### POST /api/v1/auth/login

* Descripción: Inicia sesión y devuelve los tokens JWT (access token y refresh token).
* Parámetros: email, password
* Respuesta: Devuelve el id, name y email del usuario autenticado.

### POST /api/v1/auth/refresh_token

* Descripción: Renueva el access token utilizando el refresh token almacenado en las cookies.
* Parámetros: refresh_token (en cookie)
* Respuesta: Devuelve un nuevo access token.

### GET /api/v1/auth/verify_token

* Descripción: Verifica la validez del access token.
* Parámetros: access_token (en cookie)
* Respuesta: Devuelve un mensaje de validación y el email del usuario.

### POST /api/v1/auth/logout

* Descripción: Cierra la sesión eliminando los tokens de las cookies.
* Respuesta: Devuelve un mensaje de éxito.

## Instalación y Ejecución

### Requisitos
Docker y Docker Compose instalados.
Python 3.11 (si deseas ejecutar localmente sin Docker).

### 1. Clonar repositorio 
`git clone https://github.com/KirvanRdz/fastapi-rest.git`
`cd fastapi-rest.git`

### 2. Crea la carpeta para la persistencia de datos 
`mkdir -p database`

### 3. Configurar las variables de entorno
crea un archivo .env en la raíz del proyecto y pega el contenido del archivo .example_env

### 4. Levantar la aplicación con Docker
Para levantar la aplicación y ejecutar las pruebas unitarias antes de iniciar el servidor, usa el siguiente comando:

`docker-compose up --build`

Este comando construirá la imagen de Docker, ejecutará las pruebas unitarias y, si todo es exitoso, iniciará el servidor FastAPI en el puerto 8000.

### 5. Acceder a la API
La documentación interactiva de la API estará disponible en Swagger en la siguiente URL:

http://localhost:8000/docs

