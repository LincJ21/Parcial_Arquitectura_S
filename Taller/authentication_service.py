import json
import requests
from ldap3 import Server, Connection, ALL, SIMPLE

import os

class AuthenticationService:
    def __init__(self):
        # Obtener la ruta completa al archivo JSON
        current_directory = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_directory, "users.json")
        
        # Cargamos los datos de usuario desde el archivo JSON
        with open(json_file_path, "r") as file:
            self.users_data = json.load(file)["usuarios"]

    def authenticate(self, username, password):
        # Verificamos si el usuario y la contraseña coinciden con los datos cargados desde el archivo JSON
        for user_data in self.users_data:
            if user_data["username"] == username and user_data["password"] == password:
                return True  # Autenticación exitosa
        return False  # Autenticación fallida

class LDAPAuthenticationService(AuthenticationService):
    def authenticate(self, username, password):
        # Simulamos la autenticación exitosa para este ejemplo
        return True

    # Implementación específica para autenticación LDAP
    def authenticate_ldap(self, username, password):
        # Conectarse al servidor LDAP
        server = Server('ldap://your-ldap-server.com', get_info=ALL)
        conn = Connection(server, user='cn=admin,dc=example,dc=com', password='admin_password', authentication=SIMPLE)

        # Autenticar al usuario
        if conn.bind():
            return True  # Autenticación exitosa
        else:
            return False  # Autenticación fallida

class OAuthAuthenticationService(AuthenticationService):
    def authenticate(self, username, password):
        # Implementación específica para autenticación OAuth
        # Simularemos la autenticación exitosa devolviendo siempre True
        return True

    # Implementación específica para autenticación OAuth real
    def authenticate_oauth(self, username, password):
        
        oauth_url = 'https://oauth-provider.com/authenticate'

        # Parámetros de autenticación
        params = {
            'username': username,
            'password': password
        }

        # Realizar la solicitud de autenticación OAuth
        response = requests.post(oauth_url, data=params)

        # Verificar si la autenticación fue exitosa (código de estado 200)
        if response.status_code == 200:
            return True
        else:
            return False