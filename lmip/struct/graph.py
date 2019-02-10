import collections
import queue


SearchResult = collections.namedtuple('SearchResult', ['target', 'path'])


class Vertex:

    def __init__(self, value):
        self._value = value
        self.branches = []  # = set() ; You could use a set here, but
                            # a deterministic order is useful for testing

    def __repr__(self):
        return str(self.value)

    @property
    def value(self):
        return self._value

    def make_edge(self, other_node):
        self.branches.append(other_node)
        other_node.branches.append(self)

    def search_breadth_first(self, target_value):
        return _BreadthFirstSearch().run(self, target_value)

    def search_depth_first(self, target_value):
        return _DepthFirstSearch().run(self, target_value)


class _BreadthFirstSearch:

    def __init__(self):
        self._seen = set()

    def run(self, starting_node, search_value):
        path = []

        next_nodes = queue.SimpleQueue()
        next_nodes.put(starting_node)

        while not next_nodes.empty():
            current_node = next_nodes.get()
            if current_node not in self._seen:
                if current_node.value == search_value:
                    return SearchResult(current_node, path)
                else:
                    path.append(current_node)
                    for branch in current_node.branches:
                        next_nodes.put(branch)
                    self._seen.add(current_node)

        return None


class _DepthFirstSearch:

    def __init__(self):
        self._seen = set()

    def run(self, current_node, search_value):
        results = self._run(current_node, search_value)
        return None if results is None else SearchResult(
            results[-1],
            results[0:-1]
        )

    def _run(self, current_node, search_value):
        self._seen.add(current_node)

        if current_node.value == search_value:
            return [current_node]

        for branch in current_node.branches:
            if branch not in self._seen:
                return [current_node] + self._run(branch, search_value)
