from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('0da99b52a0c62d2c7e58ff65e8748bc1')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('Hong Kong,HK')
w = observation.weather


w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

print(w.wind())
reg = owm.city_id_registry()
list_of_tuples = london = reg.ids_for('Hong kong', matching='like')
#print(list_of_tuples)

# Will it be clear tomorrow at this time in Milan (Italy) ?



