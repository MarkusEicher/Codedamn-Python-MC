current_weather = input("What is the weather like today? ")
match current_weather:
    case "sunny":
        print("It's sunny today!")
    case "rainy":
        print("It's raining today!")
    case "snowy":
        print("It's snowing today!")
    case "cloudy":
        print("It's cloudy today!")
    case current_weather:
        print("I don't know what to say!")