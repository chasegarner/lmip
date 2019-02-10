import pytest


@pytest.fixture(scope='session')
def test_utils():
    return _TestUtils()


class _TestUtils:
    @staticmethod
    def assert_values_in_order(iterable):
        data = list(iterable)
        assert all([data[i] <= data[i + 1] for i in range(len(data) - 1)])
