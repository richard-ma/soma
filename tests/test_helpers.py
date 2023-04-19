import unittest, pytest, random
import soma.helpers as helpers


class TestLimitOnemin(unittest.TestCase):
    def test_limit_is_zero(self):
        params = {
            'total': 0,
            'onemin': 0,
        }
        self.assertTrue(helpers.helper_limit_onemin(**params))
        params = {
            'total': random.randint(1, 100),
            'onemin': 0,
        }
        self.assertTrue(helpers.helper_limit_onemin(**params))

    def test_limit_greater_than_total(self):
        params = {
            'total': 99.99,
            'onemin': 100,
        }
        self.assertFalse(helpers.helper_limit_onemin(**params))
        params = {
            'total': random.randint(0, 99),
            'onemin': 100,
        }
        self.assertFalse(helpers.helper_limit_onemin(**params))

    def test_limit_less_than_total(self):
        params = {
            'total': 100.01,
            'onemin': 100,
        }
        self.assertTrue(helpers.helper_limit_onemin(**params))
        params = {
            'total': random.randint(101, 1000),
            'onemin': 100,
        }
        self.assertTrue(helpers.helper_limit_onemin(**params))

    def test_limit_equal_total(self):
        params = {
            'total': 100,
            'onemin': 100,
        }
        self.assertTrue(helpers.helper_limit_onemin(**params))