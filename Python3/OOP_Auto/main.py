#bude se jednat o závody aut - každé auto bude mít svůj název, barvu, rychlost, rychlost pro daný převod
#metody budou odstartuj,

class Car:
    def __init__(self, name="Delorian", color="BLACK", numberOfSpeeds=5):
        self.__name = name
        self.__color = color
        self.__currentSpeed = 0
        self.__numberOfSpeeds = numberOfSpeeds
        self.__shiftSpeed = 35

    def __str__(self):
        return f"Barva: {self.__color} || Název: {self.__name} || Rychlost: {self.__currentSpeed}"

    def shift(self):
        speed = "X"
        while speed not in range(self.shifts() + 1):
            try:
                speed = int(input(f"Jakou rychlost chcete zařadit? Maximální počet převodů je {self.shifts()}: "))
            except:
                print("Chybné zadání")
        self.__currentSpeed = speed * self.__shiftSpeed

    def shifts(self):
        return self.__numberOfSpeeds

    def changeColor(self):
        self.__color = input("Napište novou barvu: ")

    def changeName(self):
        self.__name = input("Napište nový název: ")

class Driver:
    def __init__(self, car):
        self.__car = car

    def prerad(self):
        self.__car.shift()

class Menu:
    def __init__(self, car):
        self.__menuChoice = "X"
        self.__car = car

    def __str__(self):
        return f"0. Spusti hru\n1. Změň barvu\n2. Změň název auta\n3. Přesedni do jiného auta"

    def menuChoice(self):
        print(self)
        self.__menuChoice = int(input("Zvolte co chcete dělat: "))
        if self.__menuChoice == 0:
            print("Tohle je 0")
            print(type(self.__menuChoice))
        elif self.__menuChoice == 1:
            self.__car.changeColor()
        elif self.__menuChoice == 2:
            self.__car.changeName()


class Game:
    def __init__(self, driver, car, menu):
        self.__gameon = 1
        self.__driver = driver
        self.__car = car
        self.__menu = menu

    def play(self):
        while self.__menu.menuChoice != 0:
            self.__menu.menuChoice()
        while self.__gameon == 1:
            print(self.__car)
            self.__driver.prerad()

if __name__ == '__main__':
    car = Car()
    driver = Driver(car)
    menu = Menu(car)
    game = Game(driver, car, menu)
    game.play()














