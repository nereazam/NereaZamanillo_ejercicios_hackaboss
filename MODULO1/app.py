from datetime import date
from user import User, Address

# Lista inicial de usuarios
users = [
    User("Nerea", "nerea@gmail.com", 36, 1.65, False, date(1988, 5, 20), Address("Calle Gran Vía", "Bilbao", "España")),
    User("David", "david@gmail.com", 20, 1.78, True, date(2004, 3, 15), Address("Avenida de los Fueros", "Madrid", "España")),
    User("Laura", "laura@gmail.com", 25, 1.70, False, date(1999, 8, 30), Address("Calle Sabino Arana", "Santander", "España"))
]

# Función 1: Imprimir todos los usuarios
def print_users(users):
    if not users:
        print("No hay ningún usuario.")
        return

    for user in users:
        print(user)
    print("\n")

# Función 2: Imprimir usuarios ordenados por edad
def print_users_sorted_by_age(users):
    if users == []: 
        print("No hay usuarios para ordenar.")
        return
    
    order = input("¿Ordenar por edad ascendente o descendente? introduce (asc/desc): ")

    if order == 'desc':
        reverse = True
    else:
        reverse = False

    users_sorted_by_age = sorted(users, key=lambda u: u.age, reverse=reverse)
    
    print("Usuarios ordenados por edad:")
    for user in users_sorted_by_age:
        print(user)

   

# Función 3: Imprimir usuario por email
def print_user_by_email(users):
    email = input("Introduce el email del usuario: ")
    for user in users:
        if email.lower() == user.email.lower():
            print(user)
            return
    print("Usuario no encontrado.")

# Función 4: Crear nuevo usuario
def create_user(users):
    name = input("Introduce el nombre del usuario: ")
    email = input("Introduce el email del usuario: ")
    age = int(input("Introduce la edad del usuario: "))
    height = float(input("Introduce la altura del usuario: "))
    is_student = input("¿Es estudiante? (sí/no): ") == "sí"

    day = int(input("Introduce el día de nacimiento del usuario: "))
    month = int(input("Introduce el mes de nacimiento del usuario: "))
    year = int(input("Introduce el año de nacimiento del usuario: "))
    birthday = date(year, month, day)

    street = input("Introduce la calle del usuario: ")
    city = input("Introduce la ciudad del usuario: ")
    country = input("Introduce el país del usuario: ")

    address = Address(street, city, country)
    new_user = User(name, email, age, height, is_student, birthday, address)
    users.append(new_user)
    print("Usuario creado correctamente.")
    print(new_user)

# Función 5: Actualizar un usuario
def update_user(users):
    email = input("Introduce el email del usuario a actualizar: ")
    actualizado = False

    for user in users:
        if email.lower() == user.email.lower():
            user.name = input("Introduce el nuevo nombre del usuario: ")
            user.age = int(input("Introduce la nueva edad del usuario: "))
            user.height = float(input("Introduce la nueva altura del usuario: "))
            user.is_student = input("¿Es estudiante? introduce (sí/no): ") == "sí"

            day = int(input("Introduce el nuevo día de nacimiento del usuario: "))
            month = int(input("Introduce el nuevo mes de nacimiento del usuario: "))
            year = int(input("Introduce el nuevo año de nacimiento del usuario: "))
            user.birthday = date(year, month, day)

            user.address.street = input("Introduce la nueva calle del usuario: ")
            user.address.city = input("Introduce la nueva ciudad del usuario: ")
            user.address.country = input("Introduce el nuevo país del usuario: ")

            actualizado = True
            break

    if actualizado:
        print("Usuario actualizado correctamente.")
    else:
        print("No ha sido posible actualizar el producto.")

# Función 6: Eliminar un usuario por email
def delete_user_by_email(users):
    email = input("Introduce el email del usuario a borrar: ")
    for i, user in enumerate(users):
        if email.lower() == user.email.lower():
            del users[i]
            print(f"Usuario {email} eliminado correctamente.")
            return

    print("Usuario no encontrado.")

# Función 7: Borrar todos los usuarios
def delete_all_users(users):
    users.clear()
    print("Todos los usuarios han sido eliminados.")