import math

class Shape:
    def __init__(self):
        pass

class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

class Cylinder(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

class Cone(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return math.pi * self.radius * (self.radius + math.sqrt((self.height ** 2) + (self.radius ** 2)))

    def volume(self):
        return (1/3) * math.pi * (self.radius ** 2) * self.height

class RectangularPrism(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def volume(self):
        return self.length * self.width * self.height

def main():
    print("1. Sphere")
    print("2. Cylinder")
    print("3. Cone")
    print("4. Rectangular Prism")
    choice = int(input("Choose a shape: "))

    if choice == 1:
        radius = float(input("Enter the radius: "))
        shape = Sphere(radius)
    elif choice == 2:
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        shape = Cylinder(radius, height)
    elif choice == 3:
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        shape = Cone(radius, height)
    elif choice == 4:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        shape = RectangularPrism(length, width, height)
    else:
        print("Invalid choice")
        return

    print("Surface area: ", shape.surface_area())
    print("Volume: ", shape.volume())

if __name__ == "__main__":
    main()