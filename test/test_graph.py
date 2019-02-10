from lmip.struct import graph


def test_graph_searches():
    #          1
    #        / | \
    #       2--3  4
    #          \ / \
    #           5   6

    n1 = graph.GraphNode(1)
    n2 = graph.GraphNode(2)
    n3 = graph.GraphNode(3)
    n4 = graph.GraphNode(4)
    n5 = graph.GraphNode(5)
    n6 = graph.GraphNode(6)

    n1.make_branch(n2)
    n1.make_branch(n3)
    n1.make_branch(n4)
    n2.make_branch(n3)
    n3.make_branch(n5)
    n4.make_branch(n5)
    n4.make_branch(n6)

    assert n1.search_depth_first(5) == graph.SearchResult(
        n5, [n1, n2, n3]
    )
    assert n1.search_breadth_first(5) == graph.SearchResult(
        n5, [n1, n2, n3, n4]
    )

    assert n1.search_depth_first(6) == graph.SearchResult(
        n6, [n1, n2, n3, n5, n4]
    )
    assert n1.search_breadth_first(6) == graph.SearchResult(
        n6, [n1, n2, n3, n4, n5]
    )

    assert n4.search_depth_first(2) == graph.SearchResult(
        n2, [n4, n1]
    )
    assert n4.search_breadth_first(2) == graph.SearchResult(
        n2, [n4, n1, n5, n6]
    )

    # You could test every combination of edge to edge for better coverage.


def test_return_none_on_no_path():
    n1 = graph.GraphNode(1)
    n2 = graph.GraphNode(2)

    assert n1.search_depth_first(2) is None
    assert n1.search_breadth_first(2) is None
