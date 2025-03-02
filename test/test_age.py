from src.checkers import *

class TestCheckAge:

    def setup_method(self):
        self.citizenship = "Local"

    def teardown_method(self):
        self.citizenship = None

    def test_senior_local(self):
        assert check_age(70, self.citizenship) == "Senior Local"

    def test_adult_local(self):
        assert check_age(30, self.citizenship) == "Adult Local"

    def test_minor_local(self):
        assert check_age(16, self.citizenship) == "Minor"

    def test_senior_foreigner(self):
        self.citizenship = "Foreigner"
        assert check_age(70, self.citizenship) == "Senior Foreigner"

    def test_adult_foreigner(self):
        self.citizenship = "Foreigner"
        assert check_age(30, self.citizenship) == "Adult Foreigner"
