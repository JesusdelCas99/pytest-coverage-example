from src.checkers import *

class TestCheckHeight:
    def setup_method(self):
        self.height = 170  # Default value for height in most tests

    def teardown_method(self):
        self.height = None

    def test_tall(self):
        self.height = 185
        assert check_height(self.height) == "Tall"

    def test_average(self):
        self.height = 170
        assert check_height(self.height) == "Average"

    def test_short(self):
        self.height = 140
        assert check_height(self.height) == "Short"