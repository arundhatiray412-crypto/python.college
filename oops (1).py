class Transport: 
    def __init__(self,type):
        self.type=type
class Bus(Transport):
    def __init__(self,t,n,s,d):
        super().__init__(t)
        self.seatNO=n
        self.source=s
        self.destination=d
    def show(self):
        print(self.type)
        print(self.seatNO)
        print(self.source)
        print(self.destination)
ob1=Bus("road transport",25,"agartala","kolkata") 
ob1.show()           




class Transport:
    def __init__(self, t):
        self.type = t


class Bus(Transport):
    def __init__(self, t, seatno, source, destination):
        super().__init__(t)
        self.seatno = seatno
        self.source = source
        self.destination = destination

    def show(self):
        print("Transport Type:", self.type)
        print("Seat Number:", self.seatno)
        print("Source:", self.source)
        print("Destination:", self.destination)


obj = Bus("Bus", 12, "Kolkata", "Barasat")
obj.show()






class Transport:
    def __init__(self, t):
        self.type = t

    def show(self):
        print("Transport Type:", self.type)


class Boat(Transport):
    def __init__(self, t, c, s, d):
        super().__init__(t)
        self.capacity = c
        self.source = s
        self.destination = d

    def show(self):
        print("Transport Type:", self.type)
        print("Capacity:", self.capacity)
        print("Source:", self.source)
        print("Destination:", self.destination)


class Bus(Transport):
    def __init__(self, t, seatno, s, d):
        super().__init__(t)
        self.seatno = seatno
        self.source = s
        self.destination = d

    def show(self):
        print("Transport Type:", self.type)
        print("Seat Number:", self.seatno)
        print("Source:", self.source)
        print("Destination:", self.destination)


# Two Boat objects
boat1 = Boat("Boat", 50, "Kolkata", "Sundarban")
boat2 = Boat("Boat", 80, "Haldia", "Digha")

# Two Bus objects
bus1 = Bus("Bus", 12, "Kolkata", "Barasat")
bus2 = Bus("Bus", 25, "Agartala", "Udaipur")

print("Boat 1")
boat1.show()

print("\nBoat 2")
boat2.show()

print("\nBus 1")
bus1.show()

print("\nBus 2")
bus2.show()






import math

class Shape:
    def __init__(self, r):
        self.radius = r


class Circle(Shape):
    def calarea(self):
        area = math.pi * self.radius ** 2
        print("Area of Circle =", round(area))


class Sphere(Shape):
    def calvolume(self):
        volume = (4/3) * math.pi * self.radius ** 3
        print("Volume of Sphere =", round(volume))


c = Circle(7)
s = Sphere(7)

c.calarea()
s.calvolume()





import math

class Triangle:
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


class EquilateralTriangle(Triangle):
    def calarea(self):
        area = (math.sqrt(3) / 4) * self.side1 ** 2
        print("Area =", round(area))

    def findangle(self):
        print("tan(angle1) =", round(math.tan(math.radians(self.angle1))))
        print("tan(angle2) =", round(math.tan(math.radians(self.angle2))))
        print("tan(angle3) =", round(math.tan(math.radians(self.angle3))))


class ScaleneTriangle(Triangle):
    def calperimeter(self):
        p = self.side1 + self.side2 + self.side3
        print("Perimeter =", p)

    def calarea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s-self.side1) * (s-self.side2) * (s-self.side3))
        print("Area =", round(area))


e = EquilateralTriangle(6, 6, 6, 60, 60, 60)
e.calarea()
e.findangle()

sc = ScaleneTriangle(5, 6, 7, 40, 60, 80)
sc.calperimeter()
sc.calarea()
