# setter are use to update a variable
# getter to read a variable


class User:
    name = ""
    __e = "" # private

    def __init__(self,name,email):
        self.name = name
        self.__e = email

    # getter
    @property
    def email(self):
        return self.__e
    
    #setter
    @email.setter
    def email(self,value):
        self.__e = value


user = User("Deepak","deepakkumar.shinde0@gmail.com")
user.email = "Om"
print(user.email)

