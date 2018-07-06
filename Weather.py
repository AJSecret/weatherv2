import pyowm
owm = pyowm.OWM('be56619fa3e0af1183509ed8251e895c')

exit = False
while not exit:
    user_choice = int(raw_input("1 to exit 2 to continue \n"))
    if user_choice == 1:
        exit = True
    else:
        loc = raw_input("Tell me a location \n")
        observation = owm.weather_at_place(loc)
        w = observation.get_weather()

        w.get_wind()
        w.get_humidity()
        w.get_temperature()

        wind = w.get_wind()
        humidity = w.get_humidity()
        temperature_info = w.get_temperature()
        temp_kel = temperature_info['temp']
        temp_cel = temp_kel -273.15
        print "the wind speed in Accra is at: " + str(wind['speed'])
        print " the humidity in Accra is at: " + str(humidity)
        print "the temperature in Accra  is at: " + str(temp_cel)

