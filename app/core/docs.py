class Docs:

    registerV1= """
            Este endpoint permite registrar a un nuevo usuario en el sistema. El usuario debe 
            proporcionar su `name`, `email`, `password`. 

            Si el `email` ya está registrado o si los datos proporcionados son inválidos, se devolverá un error 400 (Bad Request).
            """
    registerV2="""
            Este endpoint permite registrar a un nuevo usuario en el sistema. El usuario debe 
            proporcionar su `name`, `email`, `password` y `age`. El campo `age` es obligatorio 
            en esta versión y debe ser un valor mayor o igual a 18. 

            Si el `email` ya está registrado, si los datos proporcionados son inválidos, se devolverá un error 400 (Bad Request).
            """

    login= """
            Este endpoint permite a un usuario autenticarse en el sistema proporcionando su 
            `email` y `password`. Si las credenciales son válidas, se generarán dos tokens 
            JWT: un `access_token` y un `refresh_token`, los cuales serán almacenados en las 
            cookies del navegador. El `access_token` se utiliza para acceder a recursos protegidos, 
            mientras que el `refresh_token` se utiliza para renovar el `access_token`.

            Si las credenciales son incorrectas, se devolverá un error 401 (Unauthorized).
            """

    
    verify_token="""
                Este endpoint verifica el token de acceso proporcionado en las cookies. 
                Para que este endpoint funcione correctamente, primero debes utilizar el 
                endpoint `/login` para que las cookies `access_token` y `refresh_token` 
                sean almacenadas en el navegador. Una vez que las cookies están guardadas, 
                no es necesario enviar la cookie manualmente en la solicitud. Si el token 
                es válido, se devuelve el correo asociado al token. En caso contrario, se 
                devuelve un error 401."""

    refresh_token = """
                    Este endpoint permite renovar el `access_token` utilizando un `refresh_token` válido, 
                    que debe ser enviado automáticamente en las cookies. 
                    El `refresh_token` debe haber sido obtenido previamente al realizar el login 
                    y almacenado en las cookies del navegador.  Una vez que las cookies están guardadas, 
                    no es necesario enviar la cookie manualmente en la solicitud.

                    Si el `refresh_token` es válido, se generará un nuevo `access_token` y se 
                    almacenará automáticamente en las cookies. En caso de que el `refresh_token` 
                    no sea válido o no se proporcione, se devolverá un error 401.
                    """
    logout="""
            Este endpoint permite al usuario cerrar sesión en el sistema. Al invocar este 
            endpoint, los tokens JWT (`access_token` y `refresh_token`) almacenados en las 
            cookies del navegador serán eliminados. Esto invalida la sesión del usuario, 
            impidiendo que pueda acceder a recursos protegidos hasta que se autentique nuevamente."""


    
