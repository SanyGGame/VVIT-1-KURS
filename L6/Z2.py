class Vehicle:
    
    def __init__(self,make,model):
        self.make = make
        self.model = model
        
    def get_info(self):
        print(f'Марка: {self.make}, Модель: {self.model}')

class Car(Vehicle):

    def __init__(self, make, model, fuel_type):
        super().__init__(make,model)
        self.fuel_type = fuel_type
        
    def get_info(self):
        print(f'Марка: {self.make}, Модель: {self.model}, Тип топлива: {self.fuel_type}')

Carr = Vehicle('BMW','X7')
Carr.get_info()
Toyota = Car('Toyota', 'Corolla', 'АИ-95')
Toyota.get_info()
