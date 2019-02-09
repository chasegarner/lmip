from hypothesis import given, strategies
import pytest

from lmip.sort import quick


@pytest.mark.parametrize('sort_to_test', [
    quick.quick_sort
])
@given(strategies.lists(strategies.integers()))
def test_quicksort(sort_to_test, test_data):
    assert_values_in_order(
        sort_to_test(test_data)
    )


def assert_values_in_order(iterable):
    data = list(iterable)
    assert all([data[i] <= data[i + 1] for i in range(len(data) - 1)])
