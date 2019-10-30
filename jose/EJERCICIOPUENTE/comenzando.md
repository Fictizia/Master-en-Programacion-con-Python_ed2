## Enunciado

-  Al entrar, `prompt` entre login y register.
    - Si register, pedir user y password.
        - si user ya existe, lanzar error y salir.
        - si user no existe, crear con el password.
    
    
## SI ELIGE LOGIN
- pide user y pass
- si pass incorrecto o user no existe, error y salir
- si todo va bien entrar.
- si tiene una solicitud de amistad, mostrar:
    `XX quiere ser tu amigo, ¿aceptas? S/N`
    - si elige S, se agrega como amigo
- mostrar lista de comandos disponibles:

## COMANDOS DISPONIBLES
- listar todos los usuarios
    - si listar todos los usuarios, mostrar y dejar elegir uno, para solicitud de amistad
    con la pregunta `¿A quien quieres enviar solicitud de amistad?`
    - si elige a un usuario , mostrar el mensaje `¿Estas seguro que quieres ser amigo de XXX?` y actuar en consecuencia
    - tener una opcion para volver al menu anterior sin invitar a nadie

- salir
sale del programa

### por solucionar

- un usuario puede invitar 14 veces a la misma persona.
- el que envia la solicitud, en este flujo no recibe feedback si ha sido aceptada.
- se hace con ficheros a drede, pa sufrir un poquitin de nah.
- solucionar como se pueda, y ya se refactorizará A MVC.