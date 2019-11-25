 # HOLA USUARIO
 # ADIOS USARIO
import random

class Login():
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password

    def __enter__(self): # SOLO APLICAN CON WITH
        self._check_user_password()
        print('HOLA USUARIO')
        return random.randint(0,10000) 
    
    def __exit__(self, exc_type, exc_value, exc_traceback): # SOLO APLICA CON WITH
        print('ADUIS USUARIO')

    def _check_user_password(self):
        #try exception
        return True # AHORA SIEMPRE COINCIDE :P


datos_entrada = {'nombre': 'jose', 'password':'pythonMolaMucho'}
with Login(datos_entrada.get('nombre'), datos_entrada.get('password')) as number:
    print(number)