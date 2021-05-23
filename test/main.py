  
import eel
import pyowm

owm = pyowm.OWM("5db2544bed2c9d235b2dc4b05a3f30eb")

@eel.expose



def get_weather(place):

    city = place
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)

    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "В городе " + city + " сейчас " + str(temp) + " градусов!"



eel.init("web")

eel.start("main.html", size=(700, 700))
