# Multi-level inheritance
# შექმენით კლასი Gadgets, რომელსაც ეყოლება შვილი კლასი Phone-ი. 
# აიღეთ Phone კლასი, დაუმატეთ რამდენიმე თვისება და ერთი მეთოდი, რომელიც გამოიტანს: 'Calling'-ს. და მშობელ კლასად გადაეცით Ios და Android კლასებს




# Multiple Level Inheritence
# შექმენით კლასი VacuumCleaner, რომელსაც ექნება Vacuum მეთოდი.
# ასევე, შექმენით Robot კლასი, რომელსაც ექნება DetectObstacle მეთოდი.
# საბოლოოდ, შექმენით RobotVacuum კლასი, რომელიც მიიღებს VacuumCleaner და Robot -ის მეთოდებს მემკვიდრეობით.








class Gadgets:
    pass

class Phone(Gadgets):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self):
        print('tr tr')

class Ios(Phone):
    pass

class Android(Phone):
    pass



phone1 = Ios('apple', '2600')
phone2 = Android('samsung', '2500')


print(phone1.brand, phone1.price)
print(phone2.brand, phone2.price)













class VacuumCleaner:
    def Vacuum(self):
        print('vacuuming')

class Robot:
    def DetectObstacle(self):
        print('rame')

class RobotVacuum(VacuumCleaner, Robot):
    pass




robotvacuum1 = RobotVacuum()

robotvacuum1.Vacuum()
robotvacuum1.DetectObstacle()