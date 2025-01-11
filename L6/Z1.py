class UserAccount:
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        
    def set_password(self, new_password):
        self.__password = new_password
        
    def check_password(self, password):
        return password == self.__password
    
Artem = UserAccount('SanyGame', 'priupolin5443@yandex.ru', '2281337')
print(Artem.check_password('2281337'))
Artem.set_password('123456789')
print(Artem.check_password('2281337'))
print(Artem.check_password('123456789'))