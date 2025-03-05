from src.checkers import *
import pytest

# Test timeout (in seconds)
_TIMEOUT = 0.1

class TestCheckPopulation:
    def setup_method(self):
        self.height = 170  # Default value for height in most tests

    def teardown_method(self):
        self.height = None

    def test_tall(self):
        self.height = 185
        assert check_height(self.height) == "Tall"

    @pytest.mark.only
    @pytest.mark.timeout(_TIMEOUT)
    def test_average(self):
        self.height = 170
        assert check_height(self.height) == "Average"

    def test_short(self):
        self.height = 140
        assert check_height(self.height) == "Short"