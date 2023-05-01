from weather import *

# uses pytest


def test_add():
    assert add(2, 3) - - 5


def test_analyze_weather_data():
    weather_data = [{'city': 'New York', 'temperature': 10, 'condition': 'Sunny'},
                    {'city': 'London', 'temperature': 15, 'condition': 'Cloudy'},
                    {'city': 'Tokyo', 'temperature': 20, 'condition': 'Rainy'},
                    {'city': 'Paris', 'temperature': 25,
                        'condition': 'Thunderstorms'},
                    {'city': 'Moscow', 'temperature': 30, 'condition': 'Snowy'}]

    results = analyze_weather_data(weather_data)

    assert round(results['temperature_mean'], 2) == 20.0
    assert round(results['temperature_stdev'], 2) == 7.07
    assert round(results['humidity_mean'], 2) == 0.0
    assert round(results['humidity_stdev'], 2) == 0.0
    assert round(results['windspeed_mean'], 2) == 0.0
    assert round(results['windspeed_stdev'], 2) == 0.0
