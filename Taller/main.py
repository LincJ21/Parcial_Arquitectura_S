from user import User
from invoice import Invoice
from authentication_service import LDAPAuthenticationService
from benefit_manager import BenefitManager
from recommendation_engine import BasicRecommendationEngine
from user_interface import UserInterface
from location import Location

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
    print("5. añadir Ubicación")
    print("6. modificar ubicación")
    print("7. Regresar al Menú Principal")

def register(user_interface):
    username = input("Ingrese su nombre de CC: ")
    password = input("Ingrese su contraseña: ")
    name = input("Ingrese su nombre: ")
    
    # Crear instancia de usuario con los datos ingresados por el usuario
    user = User(username, password, name)
    print("Registro exitoso. Ahora puede iniciar sesión.")

def add_credit_card(user_interface):
    if user_interface.is_authenticated:
        username = input("Ingrese su nombre de usuario: ")
        credit_card_number = input("Ingrese el número de la tarjeta de crédito: ")
        expiry_date = input("Ingrese la fecha de vencimiento (MM/YY): ")
        
        user_interface.benefit_manager.credit_card.add_credit_card_info(credit_card_number, expiry_date)
        print("Tarjeta de crédito añadida exitosamente.")
    else:
        print("Error: Debe iniciar sesión para añadir una tarjeta de crédito.")

def view_credit_card(user_interface):
    if user_interface.is_authenticated:
        user_interface.benefit_manager.credit_card.view_credit_card_info()
    else:
        print("Error: Debe iniciar sesión para ver la información de la tarjeta de crédito.")

def register_location(user_interface):
    if user_interface.is_authenticated:
        city = input("Ingrese la ciudad: ")
        country = input("Ingrese el país: ")
        neighborhood = input("Ingrese el barrio: ")
        street = input("Ingrese la calle: ")

        user = user_interface.benefit_manager.user_interface.user  # Obtiene el usuario actual
        user_location = Location(user)  # Crea una instancia de Location para el usuario
        user_location.set_location(city, country, neighborhood, street)  # Establece la ubicación
    else:
        print("Error: Debe iniciar sesión para registrar una ubicación.")

def modify_location(user_interface):
    if user_interface.is_authenticated:
        user = user_interface.benefit_manager.user_interface.user  # Obtiene el usuario actual
        user_location = Location(user)  # Crea una instancia de Location para el usuario

        # Obtiene la ubicación actual del usuario
        city, country, neighborhood, street = user_location.get_location()
        print(f"Ubicación actual del usuario: Ciudad {city}, País {country}, Barrio {neighborhood}, Calle {street}")

        # Solicita al usuario la nueva información de ubicación
        new_city = input("Ingrese la nueva ciudad (deje en blanco para mantener): ") or city
        new_country = input("Ingrese el nuevo país (deje en blanco para mantener): ") or country
        new_neighborhood = input("Ingrese el nuevo barrio (deje en blanco para mantener): ") or neighborhood
        new_street = input("Ingrese la nueva calle (deje en blanco para mantener): ") or street

        # Establece la nueva ubicación
        user_location.set_location(new_city, new_country, new_neighborhood, new_street)
    else:
        print("Error: Debe iniciar sesión para modificar una ubicación.")

def login(user_interface):
    username = input("Ingrese su nombre de CC: ")
    password = input("Ingrese su contraseña: ")
    user_interface.login(username, password)
    if user_interface.is_authenticated:
        # Modifica esta línea para acceder al nombre de usuario correctamente
        print(f"Bienvenido, {user_interface.benefit_manager.user_interface.user_name}.")
        return False
    return True

def main():
    authentication_service = LDAPAuthenticationService()
    recommendation_engine = BasicRecommendationEngine()
    benefit_manager = BenefitManager(recommendation_engine)  # Asegúrate de que se pase recommendation_engine
    user_interface = UserInterface(authentication_service, benefit_manager)

    while True:
        show_main_menu()
        option = input("Ingrese el número de la opción deseada: ")

        if option == "1":
            register(user_interface)
        elif option == "2":
            
            while login(user_interface) == True:
                show_secondary_menu()
                option = input("Ingrese el número de la opción deseada: ")

                if option == "1":
                    break
                elif option == "2":
                    add_credit_card(user_interface)
                elif option == "3":
                    print("Función no implementada: Hacer una Orden")
                elif option == "4":
                    print("Función no implementada: Solicitar un Préstamo")
                elif option == "5":
                    register_location(user_interface)
                elif option == "6":
                    modify_location(user_interface)
                elif option == "7":
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
