import pytest, random
import soma.helpers as helpers


def package_total_limitaion(total: float, limitation: int) -> dict:
    return {'total': total, 'limitation': limitation}

@pytest.fixture
def limitation_greater_than_total():
    total = random.randint(1, 100)
    limitation = total + 1
    return package_total_limitaion(total, limitation)

@pytest.fixture
def limitation_less_than_total():
    total = random.randint(1, 100)
    limitation = total - 1
    return package_total_limitaion(total, limitation)

@pytest.fixture
def limitation_equal_to_total():
    total = limitation = random.randint(1, 100)
    return package_total_limitaion(total, limitation)

@pytest.fixture
def limitation_and_total_is_zero():
    return package_total_limitaion(0, 0)

@pytest.fixture
def only_limitation_is_zero():
    return package_total_limitaion(100, 0)

class TestLimitOnemin():
    def test_limitation_is_zero(self, limitation_and_total_is_zero, only_limitation_is_zero):
        assert helpers.limit_onemin(**limitation_and_total_is_zero) is True
        assert helpers.limit_onemin(**only_limitation_is_zero) is True

    def test_limitation_greater_than_total(self, limitation_greater_than_total):
        assert helpers.limit_onemin(**limitation_greater_than_total) is False

    def test_limitation_less_than_total(self, limitation_less_than_total):
        assert helpers.limit_onemin(**limitation_less_than_total) is True

    def test_limitation_equal_to_total(self, limitation_equal_to_total):
        assert helpers.limit_onemin(**limitation_equal_to_total) is True

class TestLimitOnemax():
    def test_limitation_is_zero(self, limitation_and_total_is_zero, only_limitation_is_zero):
        assert helpers.limit_onemax(**limitation_and_total_is_zero) is True
        assert helpers.limit_onemax(**only_limitation_is_zero) is True

    def test_limitation_greater_than_total(self, limitation_greater_than_total):
        assert helpers.limit_onemax(**limitation_greater_than_total) is True

    def test_limitation_less_than_total(self, limitation_less_than_total):
        assert helpers.limit_onemax(**limitation_less_than_total) is False

    def test_limitation_equal_to_total(self, limitation_equal_to_total):
        assert helpers.limit_onemax(**limitation_equal_to_total) is True