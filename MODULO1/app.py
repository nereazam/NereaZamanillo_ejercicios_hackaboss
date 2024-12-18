from datetime import date
from user import User, Address

# Lista inicial de usuarios
users = [
    User("Nerea", "nerea@gmail.com", 36, 1.65, False, date(1988, 5, 20), Address("Calle Gran Vía", "Bilbao", "España")),
    User("David", "david@gmail.com", 20, 1.78, True, date(2004, 3, 15), Address("Avenida de los Fueros", "Madrid", "España")),
    User("Laura", "laura@gmail.com", 25, 1.70, False, date(1999, 8, 30), Address("Calle Sabino Arana", "Santander", "España"))
]

# Case 1: Imprimir todos los usuarios
def print_users(users):
    if not users:
        print("No hay ningún usuario.")
        return

    print("Lista de usuarios:")
    for user in users:
        print(user)
    print("\n")

# Case 2: Imprimir usuarios ordenados por edad
def print_users_by_age(users):
    if len(users) == 0:
        print("No hay usuarios para ordenar.")
        return

    order = input("¿Ordenar por edad ascendente o descendente? introduce (asc/desc): ")
    reverse = order == 'desc'

    if reverse:
        print("Usuarios ordenados por edad (descendente):")
    else:
        print("Usuarios ordenados por edad (ascendente):")

    users_sorted_by_age = sorted(users, key=lambda u: u.age, reverse=reverse)
    
    for user in users:
        print(user)

    print("\n")

# Case 3: Imprimir usuario por email
def print_user_by_email(users):
    email = input("Introduce el email del usuario: ")
    for user in users:
        if email == user.email:
            print("Usuario encontrado por email:")
            print(user)
            print("\n")
            return
    print("Usuario no encontrado.")
    print("\n")

# Case 4: Crear nuevo usuario
def create_user(users):
    try:
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
    except:
        print("Error al crear el usuario")
    print("\n")

# Case 5: Actualizar un usuario
def update_user(users):
    email = input("Introduce el email del usuario a actualizar: ")
    for user in users:
        if email == user.email.lower():
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

            print("Usuario actualizado correctamente.")
            print(user)
            print("\n")
            return
    print("Usuario no encontrado.")
    print("\n")

# Case 6: Eliminar un usuario por email
def delete_user_by_email(users):
    email = input("Introduce el email del usuario a borrar: ")
    for i, user in enumerate(users):
        if email == user.email:
            del users[i]
            print(f"Usuario {email} eliminado correctamente.")
            print("\n")
            return
    print("Usuario no encontrado.")
    print("\n")

# Case 7: Borrar todos los usuarios
def delete_all_users(users):
    users.clear()
    print("Todos los usuarios han sido eliminados.")
    print("\n")
