from src.checkers import check_age
import pytest
import time

# Test timeout (in seconds)
_TIMEOUT = 1

class TestCheckAge:
    def setup_method(self):
        self.citizenship = "Local"

    def teardown_method(self):
        self.citizenship = None

    @pytest.mark.only
    @pytest.mark.timeout(_TIMEOUT)
    @pytest.mark.parametrize(
        "age, citizenship, expected",
        [
            (70, "Local", "Senior Local"),
            (30, "Local", "Adult Local"),
            (16, "Local", "Minor"),
            (70, "Foreigner", "Senior Foreigner"),
            (30, "Foreigner", "Adult Foreigner"),
        ]
    )
    def test_check_age(self, age, citizenship, expected):
        self.citizenship = citizenship  # Asignar el valor de la prueba
        assert check_age(age, self.citizenship) == expected
