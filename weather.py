import random
import statistics


def analyze_weather_data(weather_data):
    """
    Analyze the weather data and return a dictionary with the results.
    """
    results = {}
    temperatures = [data['temperature'] for data in weather_data]
    humidity = [data['humidity'] for data in weather_data]
    windspeed = [data['windspeed'] for data in weather_data]

    results['temperature_mean'] = statistics.mean(temperatures)
    results['temperature_stdev'] = statistics.stdev(temperatures)

    results['humidity_mean'] = statistics.mean(humidity)
    results['humidity_stdev'] = statistics.stdev(humidity)

    results['windspeed_mean'] = statistics.mean(windspeed)
    results['windspeed_stdev'] = statistics.stdev(windspeed)

    return results


def generate_weather_data(num_entries):
    weather_data = []
    cities = ['New York', 'London', 'Tokyo', 'Paris', 'Moscow']
    weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Thunderstorms', 'Snowy']

    for i in range(num_entries):
        city = random.choice(cities)
        temperature = round(random.uniform(-10, 40), 2)
        humidity = round(random.uniform(0, 100), 2)
        windspeed = round(random.uniform(0, 50), 2)
        condition = random.choice(weather_conditions)

        data = {'city': city, 'temperature': temperature,
                'humidity': humidity, 'windspeed': windspeed, 'condition': condition}
        weather_data.append(data)

    return weather_data


def add(x, y):
    return x + y


data = generate_weather_data(5)
print(analyze_weather_data(data))
