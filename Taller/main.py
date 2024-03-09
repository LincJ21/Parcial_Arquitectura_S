from user import User
from invoice import Invoice
from authentication_service import LDAPAuthenticationService
from benefit_manager import BenefitManager
from recommendation_engine import BasicRecommendationEngine
from user_interface import UserInterface

def show_main_menu():
    print("Menú Principal")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Salir")

def show_secondary_menu():
    print("\nMenú Secundario")
    print("1. Cerrar Sesión")
    print("2. Añadir Tarjeta de Crédito")
    print("3. Hacer una Orden")
    print("4. Solicitar un Préstamo")
    print("5. Ubicación")
    print("6. Regresar al Menú Principal")

def register(user_interface):
    username = input("Ingrese su nombre de CC: ")
    password = input("Ingrese su contraseña: ")
    name = input("Ingrese su nombre: ")
    
    # Crear instancia de usuario con los datos ingresados por el usuario
    user = User(username, password, name)
    print("Registro exitoso. Ahora puede iniciar sesión.")

def login(user_interface):
    username = input("Ingrese su nombre de CC: ")
    password = input("Ingrese su contraseña: ")
    user_interface.login(username, password)

def main():
    authentication_service = LDAPAuthenticationService()
    recommendation_engine = BasicRecommendationEngine()
    benefit_manager = BenefitManager(recommendation_engine)
    user_interface = UserInterface(authentication_service, benefit_manager)

    while True:
        show_main_menu()
        option = input("Ingrese el número de la opción deseada: ")

        if option == "1":
            register(user_interface)
        elif option == "2":
            login(user_interface)
            while user_interface.is_authenticated:
                show_secondary_menu()
                option = input("Ingrese el número de la opción deseada: ")

                if option == "1":
                    user_interface.logout()
                elif option == "2":
                    print("Función no implementada: Añadir Tarjeta de Crédito")
                elif option == "3":
                    print("Función no implementada: Hacer una Orden")
                elif option == "4":
                    print("Función no implementada: Solicitar un Préstamo")
                elif option == "5":
                    print("Función no implementada: Ubicación")
                elif option == "6":
                    break
                else:
                    print("Opción no válida. Por favor, ingrese una opción válida.")
        elif option == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
