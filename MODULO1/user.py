# Clases 

class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"



class User:
    def __init__(self, name, email, age, height, is_student, birthday, address):
        self.name = name
        self.email = email
        self.age = age
        self.height = height
        self.is_student = is_student
        self.birthday = birthday
        self.address = address

    def __str__(self):
        return (f"User(name={self.name}, email={self.email}, age={self.age}, "
                f"height={self.height}m, student={'Sí' if self.is_student else 'No'}, "
                f"birthday={self.birthday}, address={self.address})")