from datetime import datetime
from dataclasses import dataclass

# from colorama import Fore
'''
Написати клас User, який буде зберігати інформацію про користувача онлайн магазину

(first name, last name, email, phone)
'''

class Human:
    def __init__(self, full_name):
        self.full_name = full_name

    def print_full_name(self):
        print(self.full_name)

    def run(self):
        print("Human runs")

class Animal:
    def run(self):
        print("Animal runs")


# class UserFactory:
#     def __init__(self):
#         pass

#     def set_name(self, full_name)
#         self.full_name = full_name

    # def build_user(self):
    #     return User(first_name, last_name, )


class User(Human, Animal):
    # def __init__(self, settings: dict):
    def __init__(self, first_name, last_name, email, phone, password):
        super().__init__(f'{first_name} {last_name}')
        # super().__init__('')
        # self.__dict__ = kwargs
        # self.email = settings['email']
        # print(kwargs)
        self.__password = password
        self.email = email
        self._phone = None
        self.phone = phone

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, new_value):
        if len(new_value) < 10:
            raise ValueError
        self._phone = new_value

    @property
    def password(self):
        raise KeyError
    
    @password.setter
    def password(self, new_value):
        self.__password = new_value

    def print_user_info(self) -> None:
        print(f'{self.full_name}: {self.email}, {self.phone} {self.__password}')


@dataclass(frozen=True)
class UserAlternative:
    name: str
    age: int
    email: str

# def print_user_info(user: User) -> None:
#     print(f'{user.full_name}: {user.email}, {user.phone}')


user_john = User(first_name="John", last_name="Smith", email="mail@gmail.com", phone="1234567890", password="my_password")
# print(user_john.email)
# print(dir(user_john))
# print(user_john.__dict__)
# user_john = User(**{'first_name':"John", 'last_name':"Smith", 'email':"mail@gmail.com", 'phone':"1234567890", 'password':"my_password"})
# print(dir(user_john))
# print(user_john._User__password)
# user_john.run()
# print_user_info(user_john)
# user_john.print_user_info()
# print(user_john.__password)
# user_john.__password = "hello_world"
# print(user_john.__password)
# user_john.__password = "hello_world"
# user_john.print_user_info()
# print(dir(user_john))

# print(user_john.password)
# user_john.print_user_info()
# user_john.password = "hello_world"
# user_john.print_user_info()

# try:
#     user_john.phone = '09876'
# except ValueError:
#     print('Phone number is not valid')
# user_john.print_user_info()

user_alternative = UserAlternative("John Smith", 29, "mail@gmail.com")
# user_alternative.name = "Jane"
# print(user_alternative)

try:
    ...
except ValueError:
    print()


