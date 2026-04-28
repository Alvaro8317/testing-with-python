# Un Stub reemplaza una dependencia y devuelve respuestas predefinidas (hardcodeadas).
# Se usa cuando necesitamos controlar los datos que recibe nuestro código,
# sin depender de sistemas externos (APIs, bases de datos, etc.).


class WeatherApiClient:
    """Cliente real que consulta una API externa (lenta, costosa, impredecible)."""

    def get_temperature(self, city: str) -> float:
        # En producción haría una llamada HTTP real
        raise NotImplementedError("Llama a una API real")


class WeatherService:
    def __init__(self, api_client: WeatherApiClient) -> None:
        self._client = api_client

    def is_hot_weather(self, city: str) -> bool:
        temperature = self._client.get_temperature(city)
        return temperature > 30.0

    def get_weather_advice(self, city: str) -> str:
        temperature = self._client.get_temperature(city)
        if temperature > 30.0:
            return "Lleva agua y protector solar"
        elif temperature > 15.0:
            return "El clima es agradable"
        else:
            return "Abrígate bien"
