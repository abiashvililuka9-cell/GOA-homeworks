
class Map:
    def __init__(self, country, city, IP_location):
        self.country = country
        self.city = city
        self._IP_location = IP_location

    def IP_location_show(self):
        return self._IP_location



location = Map('georgia', 'tbilisi', 1294743)

print(location._IP_location)
print(location.IP_location_show())






class User_data:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self._email = email
        self._password = password

    def display_email(self):
        return self._email

    def display_password(self):
        return self._password


user1 = User_data('luka', 'abiashvili', 'lukanor@gmail.com', 1111)

print(user1.display_email())
print(user1.display_password())




        