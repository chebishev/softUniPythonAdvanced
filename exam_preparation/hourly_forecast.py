def forecast(*weather):
    weather_translate = {
        "Sunny": 1,
        "Rainy": 3,
        "Cloudy": 2
    }
    weather_cities = {}
    weather_dictionary = {}
    for item in weather:
        weather_dictionary[item[0]] = weather_translate[item[1]]
        weather_cities[item[0]] = item[1]
    sorted_weather = dict(sorted(weather_dictionary.items(), key=lambda x: (x[1], x[0])))
    output_list = []
    for k in sorted_weather:
        output_list.append(f"{k} - {weather_cities[k]}")

    return "\n".join(output_list)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
