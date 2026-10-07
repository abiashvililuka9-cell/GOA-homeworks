class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age



class BankAccount:
    def __init__(self, balance):
        self.__balance = balance



class UserInfo:
    def __init__(self, name, surname, age, address):
        self.name = name
        self.surname = surname
        self._age = age         
        self._address = address  

    def get_age(self):
        return self._age

    def get_address(self):
        return self._address


user = UserInfo("Luka", "Abiashvili", 20, "Tbilisi")


print(user._age)
print(user._address)


print(user.get_age())
print(user.get_address())



class Bank:
    def __init__(self, account_name, balance):
        self._account_name = account_name  
        self.__balance = balance            

    def get_account_name(self):
        return self._account_name


account = Bank("Luka", 1500)


print(account.get_account_name())


print(account._Bank__balance)


# 9) Book class
class Book:
    def __init__(self, author, bookName, pageAmount):
        self._author = author            
        self.__pageAmount = pageAmount  
        self.bookName = bookName

    def get_page_amount(self):
        return self.__pageAmount

    def __display_pages(self):
        return self.__pageAmount


book = Book("George Orwell", "1984", 328)


print(book._author)


print(book.get_page_amount())


print(book._Book__pageAmount)


print(book._Book__display_pages())