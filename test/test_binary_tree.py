from hypothesis import given, strategies

from lmip.struct import binary_tree


@given(strategies.lists(strategies.integers()))
def test_search(test_utils, test_data):
    tree = binary_tree.BinaryTree()

    for data in test_data:
        tree.insert(data)

    for data in test_data:
        assert tree.search(data)


@given(strategies.lists(strategies.integers()))
def test_delete(test_utils, test_data):
    tree = binary_tree.BinaryTree()

    for data in test_data:
        tree.insert(data)

    for data in test_data:
        tree.delete(data)

    assert tree.is_empty()


@given(strategies.lists(strategies.integers()))
def test_to_list(test_utils, test_data):
    tree = binary_tree.BinaryTree()

    for data in test_data:
        tree.insert(data)

    test_utils.assert_values_in_order(tree.to_list())
