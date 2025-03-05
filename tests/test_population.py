from dataclasses import dataclass
from unittest.mock import patch
from src.checkers import *
import pytest

_TIMEOUT = 1

@dataclass
class ResponseObject:
    status_code: int
    message: str

class TestCheckPopulation:
    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @pytest.mark.only
    @pytest.mark.timeout(_TIMEOUT)
    @patch('src.checkers.requests.get')
    @pytest.mark.parametrize(
        "country, expected_response",
        [
            ('Spain', ResponseObject(status_code=200, message='Success')),
            ('Finland', ResponseObject(status_code=500, message='Error'))
        ]
    )
    def test_population(self, mock_get, country, expected_response):
        mock_get.return_value = expected_response
        response = check_population(country)
        assert response.status_code == expected_response.status_code
        mock_get.assert_called_once_with(
        url=f"https://api.population.io/1.0/population/{country}/today-and-tomorrow/"
        )
