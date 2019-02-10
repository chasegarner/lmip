from hypothesis import given, strategies
import pytest

from lmip.sort import merge, quick


@pytest.mark.parametrize('sort_to_test', [
    merge.merge_sort,
    quick.quick_sort
])
@given(strategies.lists(strategies.integers()))
def test_sorts(sort_to_test, test_utils, test_data):
    test_utils.assert_values_in_order(
        sort_to_test(test_data)
    )
