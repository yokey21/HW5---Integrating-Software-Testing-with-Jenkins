import random


def generate_weather_data(num_entries):
    weather_data = []
    cities = ['New York', 'London', 'Tokyo', 'Paris', 'Moscow']
    weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Thunderstorms', 'Snowy']

    for i in range(num_entries):
        city = random.choice(cities)
        temperature = round(random.uniform(-10, 40), 2)
        condition = random.choice(weather_conditions)

        data = {'city': city, 'temperature': temperature, 'condition': condition}
        weather_data.append(data)

    return weather_data


def add(x, y):
    return x + y


data = generate_weather_data(5)
print(data)
