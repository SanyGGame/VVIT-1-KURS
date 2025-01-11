class Employee:
    def __init__(self, name, ident):
        self.name = name
        self.ident = ident
        
    def get_info(self):
        return f'Имя: {self.name}, ID: {self.ident}'

class Manager(Employee):
    def __init__(self, name, ident, department):
        super().__init__(name, ident)
        self.department = department

    def get_info(self):
        return f'Имя: {self.name}, ID: {self.ident}, Отдел: {self.department}'

    def manage_project(self):
        return f'{self.name} руководит проектом в отделе {self.department}'

class Technician(Employee):
    def __init__(self, name, ident, specialization):
        super().__init__(name, ident)
        self.specialization = specialization

    def get_info(self):
        return f'Имя: {self.name}, ID: {self.ident}, Специализация: {self.specialization}'

    def perform_maintenance(self):
        return f'{self.name} ({self.specialization}) выполнил(а) техническое обслуживание'

class TechManager(Manager, Technician):
    def __init__(self, name, ident, department, specialization):
        Employee.__init__(self, name, ident)
        self.department = department
        self.specialization = specialization
        self.team = []

    def get_info(self):
        return f'Имя: {self.name}, ID: {self.ident}, Отдел: {self.department}, Специализация: {self.specialization}'

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if len(self.team) == 0:
            return 'Нет подчинённых сотрудников'
        else:
            info = 'Подчинённые сотрудники:\n'
            for emp in self.team:
                info += f'{emp.get_info()}\n'
            return info
        
emp1 = Employee("Артём Приуполин", 100)
manager = Manager("Андрей Сахаровский", 101, "IT")
technician = Technician("Дмитрий Орешкин", 102, "Java-разработчик")
tech_manager = TechManager("Никита Морозов", 103, "Маркетинг", "Продакт-менеджер")

print(emp1.get_info())
print(manager.get_info())
print(technician.get_info())
print(tech_manager.get_info())

print(manager.manage_project())
print(technician.perform_maintenance())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())

tech_manager.add_employee(emp1)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

print(tech_manager.get_team_info())
                
