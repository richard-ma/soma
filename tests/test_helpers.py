import pytest, random
import soma.helpers as helpers


def package_total_limitation(total: float, limitation: int) -> dict:
    return {'total': total, 'limitation': limitation}

def package_curnum_limitation(curnum: int, limitation: int) -> dict:
    return {'curnum': curnum, 'limitation': limitation}

def package_total_limitation_curmoney(total: float, limitation: int, curmoney: float) -> dict:
    return {'total': total, 'limitation': limitation, 'curmoeny': curmoney}

@pytest.fixture
def greater_than():
    first = random.randint(1, 100)
    second = first + 1
    return (first, second)

@pytest.fixture
def less_than():
    first = random.randint(1, 100)
    second = first - 1
    return (first, second)

@pytest.fixture
def equal_to():
    first = random.randint(1, 100)
    second = first
    return (first, second)

@pytest.fixture
def limitation_greater_than_total(greater_than):
    return package_total_limitation(*greater_than)

@pytest.fixture
def limitation_less_than_total(less_than):
    return package_total_limitation(*less_than)

@pytest.fixture
def limitation_equal_to_total(equal_to):
    return package_total_limitation(*equal_to)

@pytest.fixture
def limitation_and_total_is_zero():
    return package_total_limitation(0, 0)

@pytest.fixture
def only_limitation_of_total_is_zero():
    return package_total_limitation(100, 0)

@pytest.fixture
def limitation_greater_than_curnum(greater_than):
    return package_curnum_limitation(*greater_than)

@pytest.fixture
def limitation_less_than_curnum(less_than):
    return package_curnum_limitation(*less_than)

@pytest.fixture
def limitation_equal_to_curnum(equal_to):
    return package_curnum_limitation(*equal_to)

@pytest.fixture
def limitation_and_curnum_is_zero():
    return package_curnum_limitation(0, 0)

@pytest.fixture
def only_limitation_of_curnum_is_zero():
    return package_curnum_limitation(100, 0)

class TestLimitOnemin():
    def test_limitation_is_zero(self, limitation_and_total_is_zero, only_limitation_of_total_is_zero):
        assert helpers.limit_onemin(**limitation_and_total_is_zero) is True
        assert helpers.limit_onemin(**only_limitation_of_total_is_zero) is True

    def test_limitation_greater_than_total(self, limitation_greater_than_total):
        assert helpers.limit_onemin(**limitation_greater_than_total) is False

    def test_limitation_less_than_total(self, limitation_less_than_total):
        assert helpers.limit_onemin(**limitation_less_than_total) is True

    def test_limitation_equal_to_total(self, limitation_equal_to_total):
        assert helpers.limit_onemin(**limitation_equal_to_total) is True

class TestLimitOnemax():
    def test_limitation_is_zero(self, limitation_and_total_is_zero, only_limitation_of_total_is_zero):
        assert helpers.limit_onemax(**limitation_and_total_is_zero) is True
        assert helpers.limit_onemax(**only_limitation_of_total_is_zero) is True

    def test_limitation_greater_than_total(self, limitation_greater_than_total):
        assert helpers.limit_onemax(**limitation_greater_than_total) is True

    def test_limitation_less_than_total(self, limitation_less_than_total):
        assert helpers.limit_onemax(**limitation_less_than_total) is False

    def test_limitation_equal_to_total(self, limitation_equal_to_total):
        assert helpers.limit_onemax(**limitation_equal_to_total) is True

class TestLimitNum():
    def test_limitation_is_zero(self, limitation_and_curnum_is_zero, only_limitation_of_curnum_is_zero):
        assert helpers.limit_num(**limitation_and_curnum_is_zero) is True
        assert helpers.limit_num(**only_limitation_of_curnum_is_zero) is True

    def test_limitation_greater_than_curnum(self, limitation_greater_than_curnum):
        assert helpers.limit_num(**limitation_greater_than_curnum) is True

    def test_limitation_less_than_curnum(self, limitation_less_than_curnum):
        assert helpers.limit_num(**limitation_less_than_curnum) is False

    def test_limitation_equal_to_curnum(self, limitation_equal_to_curnum):
        assert helpers.limit_num(**limitation_equal_to_curnum) is False

class TestLimitMoney():
    def test_limitation_is_zero(self):
        assert helpers.limit_money(total=0, limitation=0, curmoney=0) is True
        assert helpers.limit_money(total=100, limitation=0, curmoney=100) is True

    def test_limitation_sub_curmoney_greater_than_total(self):
        assert helpers.limit_money(total=1, limitation=100, curmoney=1) is True

    def test_limitation_sub_curmoney_less_than_total(self):
        assert helpers.limit_money(total=100, limitation=100, curmoney=1) is False

    def test_limitation_sub_curmoney_equal_to_total(self):
        assert helpers.limit_money(total=99, limitation=100, curmoney=1) is True