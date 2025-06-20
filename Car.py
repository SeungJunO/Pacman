class Car:
    def __init__(self, speed=0,gear=1,color="white"):
        self.__spedd = speed
        self.__gear = gear
        self.__color = color

    def setSpeed(self, speed):
        self.__speed = speed

    def setGear(self,gear):
        self.__gear = gear

    def setColor(self,color):
        self.__color = color

    def getSpeed(self):
        return self.__speed

    def getGear(self):
        return self.__gear

    def getcolor(self):
        return self.__color

    def view(self):
        return print('speed=%d, gear=%d, color=%s' %(self.__speed, self.__gear,self.__color))

    def __str__(self):
        return '(%d %d %s)' %(self.__speed, self.__gear, self.__color)

myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
myCar.view()
print(myCar)
