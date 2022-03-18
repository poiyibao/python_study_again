"""
import folium

#print(folium.__version__)

#world_map = folium.Map()
#world_map.save('test_01.html')
national_map = folium.Map(location=[35.6, 100.6], zoom_start=4)
national_map.save('test_01.html')

"""
from demo_3 import ElectCar

my_new_car = ElectCar("audi", "elctron","2022")

print(my_new_car.get_descriptive_name())
my_new_car.battery.describe_bettery()
my_new_car.battery.get_range()
