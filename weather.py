import random
import statistics
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/weather')
def display_weather():
    headers = [
        'City', 'Temperature (C)', 'Humidity (%)', 'Wind Speed (km/h)', 'Condition']
    rows = []
    for data in weather_data:
        city = data['city']
        temp = str(data['temperature'])
        humid = str(data['humidity'])
        wind = str(data['windspeed'])
        condition = data['condition']
        rows.append([city, temp, humid, wind, condition])
    return render_template('weather.html', headers=headers, rows=rows)


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


def display_weather_data(weather_data):
    print("| City          | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Condition     |")
    print("+---------------+----------------+--------------+-------------------+---------------+")

    for data in weather_data:
        city = data['city'].ljust(15)
        temp = str(data['temperature']).ljust(16)
        humid = str(data['humidity']).ljust(14)
        wind = str(data['windspeed']).ljust(19)
        condition = data['condition'].ljust(15)
        print(f"| {city}| {temp}| {humid}| {wind}| {condition}|")


def add(x, y):
    return x + y


weather_data = generate_weather_data(5)
display_weather_data(weather_data)

# Run the Flask app by adding the following code at the end of your Python file:
if __name__ == '__main__':
    app.run()
