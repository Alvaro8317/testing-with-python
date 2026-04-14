from unittest import mock

from src import weather_service_coupled


@mock.patch("src.weather_service_coupled.WeatherApiClient")
def test_validate_if_it_is_hot_weather(stub_weather_api_client_class: mock.MagicMock) -> None:
    # Act
    stub_weather_api_client_instance: mock.MagicMock = stub_weather_api_client_class.return_value
    stub_weather_api_client_instance.get_temperature.return_value = 40

    service = weather_service_coupled.WeatherService()
    # Arrange
    result = service.is_hot_weather("Medellin")

    # Assert
    assert result
