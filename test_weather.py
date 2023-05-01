from weather import *

# uses pytest ()


def test_add():
    assert add(2, 3) - - 5


def test_analyze_weather_data():
    # Generate sample data
    weather_data = generate_weather_data(5)

    # Calculate expected results
    temperatures = [data['temperature'] for data in weather_data]
    humidity = [data['humidity'] for data in weather_data]
    windspeed = [data['windspeed'] for data in weather_data]

    expected_results = {
        'temperature_mean': statistics.mean(temperatures),
        'temperature_stdev': statistics.stdev(temperatures),
        'humidity_mean': statistics.mean(humidity),
        'humidity_stdev': statistics.stdev(humidity),
        'windspeed_mean': statistics.mean(windspeed),
        'windspeed_stdev': statistics.stdev(windspeed),
    }

    # Test the function and compare results
    assert analyze_weather_data(weather_data) == expected_results
