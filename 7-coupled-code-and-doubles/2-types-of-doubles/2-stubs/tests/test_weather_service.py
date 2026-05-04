from unittest import mock

import pytest
from src import weather_service


class HotWeatherApiStub(weather_service.WeatherApiClient):
    """Simula una API que reporta clima caluroso (35°C)."""

    def get_temperature(self, city: str) -> float:
        return 35.0


class MildWeatherApiStub(weather_service.WeatherApiClient):
    """Simula una API que reporta clima templado (22°C)."""

    def get_temperature(self, city: str) -> float:
        return 22.0


class ColdWeatherApiStub(weather_service.WeatherApiClient):
    """Simula una API que reporta clima frío (5°C)."""

    def get_temperature(self, city: str) -> float:
        return 5.0


class TestWeatherService:
    def test_is_hot_weather_returns_true_when_above_30(self) -> None:
        service = weather_service.WeatherService(api_client=HotWeatherApiStub())

        result = service.is_hot_weather("Bogotá")

        assert result

    def test_is_hot_weather_returns_false_when_below_30(self) -> None:
        service = weather_service.WeatherService(api_client=ColdWeatherApiStub())

        result = service.is_hot_weather("Bogotá")

        assert not result

    def test_advice_for_hot_weather(self) -> None:
        service = weather_service.WeatherService(api_client=HotWeatherApiStub())

        advice = service.get_weather_advice("Medellín")

        assert advice == "Lleva agua y protector solar"

    def test_advice_for_mild_weather(self) -> None:
        service = weather_service.WeatherService(api_client=MildWeatherApiStub())

        advice = service.get_weather_advice("Medellín")

        assert advice == "El clima es agradable"

    def test_advice_for_cold_weather(self) -> None:
        service = weather_service.WeatherService(api_client=ColdWeatherApiStub())

        advice = service.get_weather_advice("Medellín")

        assert advice == "Abrígate bien"


def test_should_validate_advice_for_mild_weather() -> None:
    # Act
    stub_cold_weather = mock.MagicMock()
    stub_cold_weather.get_temperature.return_value = 28
    service = weather_service.WeatherService(api_client=stub_cold_weather)

    # Arrange
    result = service.get_weather_advice(city="Mosquera")

    # Assert
    assert result == "El clima es agradable"


def test_should_validate_advice_for_hot_weather() -> None:
    # Act
    stub_cold_weather = mock.MagicMock()
    stub_cold_weather.get_temperature.return_value = 35
    service = weather_service.WeatherService(api_client=stub_cold_weather)

    # Arrange
    result = service.get_weather_advice(city="Mosquera")

    # Assert
    assert result == "Lleva agua y protector solar"


@pytest.fixture(scope="function")
def fxt_stub_weather(request: pytest.FixtureRequest) -> mock.MagicMock:
    value_temperature = request.param
    stub_cold_weather = mock.MagicMock()
    stub_cold_weather.get_temperature.return_value = value_temperature
    return stub_cold_weather


@pytest.mark.parametrize(
    "fxt_stub_weather, expected_advice",
    [
        (pytest.param(8, "Abrígate bien", id="A cold weather")),
        (pytest.param(28, "El clima es agradable", id="Mild weather")),
        (pytest.param(35, "Lleva agua y protector solar", id="Hot weather")),
    ],
    indirect=["fxt_stub_weather"],
)
def test_should_validate_advice(fxt_stub_weather: mock.MagicMock, expected_advice: str) -> None:
    service = weather_service.WeatherService(api_client=fxt_stub_weather)

    # Arrange
    result = service.get_weather_advice(city="Mosquera")

    # Assert
    assert result == expected_advice
