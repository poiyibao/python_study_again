"""
favorite_languages = {
    'jen': 'python',
    'sada' : 'dart',
    'awda' : 'ruby',
}
for lan in favorite_languages.values():
   print(f"list is { lan.title()}")
# sorted() set()转换为集合

aliens =[]
for create_alien in range(30):
    #print(create_alien)
    if(create_alien<3):
        new = {'clor':'blue','points':'10','speed':'fast'}
        aliens.append(new)
    else:
        new = {'clor':'green','points':'5','speed':'slow'}
        aliens.append(new)
for alien in aliens[:5]:
    print(alien)

message_list = ['test 1', 'test 2', 'test 3', 'test 4']

def show_messages(list):
    for mess in list:
        print(f"the message is {mess} ")
show_messages(message_list)

 """

class Car:
    #moudle
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odmeter(self):
        print(f"the car has {self.odometer_reading} miles on it.")
    def upadte_odmeter(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Roll back confused")
    def add_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    def describe_bettery(self):
        print(f"the car has {self.battery_size}kWh battery")
    def get_range(self):
        if self.battery_size >= 300:
            range = "full power"
        elif self.battery_size >100 & self.battery_size <300:
            range = "sufficient power"
        else:
            range = "low power"
        print(f"the car has {range}." )

class ElectCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
