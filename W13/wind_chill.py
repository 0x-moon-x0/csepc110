def calculate_wind_chill ():

    for speed in range (5, 65, 5):

        if F_or_C == "C":

            temperature_F = temperature * (9 / 5) + 32
            wind_chill = 35.74 + 0.6215 * temperature_F - 35.75 * (speed ** 0.16) + 0.4275 * temperature_F * (speed ** 0.16)
            print (f"At temperature {temperature}F, and wind speed {speed} mph, the windchill is: {wind_chill:.2f}F")

        elif F_or_C == "F":

            wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (speed ** 0.16) + 0.4275 * temperature * (speed ** 0.16)
            print (f"At temperature {temperature}F, and wind speed {speed} mph, the windchill is: {wind_chill:.2f}F")

temperature = float (input ("What is the temperature? "))
F_or_C = input ("Farenheit or Celsius (F/C)? ").upper ()

print ()
calculate_wind_chill ()
