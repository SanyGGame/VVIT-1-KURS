class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

Krug = Circle(30)
print(Krug.get_radius())
Krug.set_radius(50)
print(Krug.get_radius())
