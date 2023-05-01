from weather import *

# uses pytest


def test_add():
    assert add(2, 3) - - 5


def test_generate_weather_data():
    data = generate_weather_data()
    assert isinstance(data, list)
    assert len(data) == 10
    for item in data:
        assert isinstance(item, dict)
        assert set(item.keys()) == {
            'city', 'temperature', 'description', 'humidity'}
        assert isinstance(item['city'], str)
        assert isinstance(item['temperature'], int)
        assert isinstance(item['description'], str)
        assert isinstance(item['humidity'], int)
