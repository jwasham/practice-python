import queue
import copy


class DirectedGraph(object):
    """
    Directed Graph, with graph represented as an adjacency list
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        """
        Adds an edge defined by vertices source and destination
        :param source:
        :param destination:
        :return:
        """
        if source not in self.adjacency_list:
            self.adjacency_list[source] = set()
        self.adjacency_list[source].add(destination)

    def get_vertex(self):
        """
        Generator for returning the next vertex from the adjacency list
        :return:
        """
        for v in self.adjacency_list:
            yield v

    def get_neighbor(self, vertex):
        """
        Generator for returning the next vertex adjacent to the given vertex
        :param vertex:
        :return:
        """
        if vertex in self.adjacency_list:
            for u in self.adjacency_list[vertex]:
                yield u

    def get_reverse_neighbor(self, vertex):
        """
        Generator for returning the reversed edge neighbor to the given vertex (parent)
        :param vertex:
        :return:
        """
        reversed_list = {}
        for v, u in self.adjacency_list.items():
            for w in u:
                if w not in reversed_list:
                    reversed_list[w] = set()
                reversed_list[w].add(v)

        if vertex in reversed_list:
            for u in reversed_list[vertex]:
                yield u

    def dfs(self):
        """
        Computes the initial source vertices for each connected component
        and the parents for each vertex as determined through depth-first-search
        :return: initial source vertices for each connected component, parents for each vertex
        :rtype: set, dict
        """
        parents = {}
        components = set()
        to_visit = []

        for vertex in self.get_vertex():
            if vertex not in parents:
                components.add(vertex)
            else:
                continue

            to_visit.append(vertex)

            while to_visit:
                v = to_visit.pop()

                for neighbor in self.get_neighbor(v):
                    if neighbor not in parents:
                        parents[neighbor] = v
                        to_visit.append(neighbor)

        return components, parents

    def bfs(self):
        """
        Computes the the parents for each vertex as determined through breadth-first search
        :return: parents for each vertex
        :rtype: dict
        """
        parents = {}
        to_visit = queue.Queue()

        for vertex in self.get_vertex():
            to_visit.put(vertex)

            while not to_visit.empty():
                v = to_visit.get()

                for neighbor in self.get_neighbor(v):
                    if neighbor not in parents:
                        parents[neighbor] = v
                        to_visit.put(neighbor)

        return parents

    def contains_cycle(self):
        """
        Determines if one of the connected components contains a cycle
        :return: true if one of the connected components contains a cycle
        :rtype: bool
        """
        contains_cycle = False
        STATUS_STARTED = 1
        STATUS_FINISHED = 2

        for vertex in self.get_vertex():
            statuses = {}
            to_visit = [vertex]

            while to_visit and not contains_cycle:
                v = to_visit.pop()

                if v in statuses:
                    if statuses[v] == STATUS_STARTED:
                        statuses[v] = STATUS_FINISHED
                else:
                    statuses[v] = STATUS_STARTED
                    to_visit.append(v)  # add to stack again to signal vertex has finished DFS

                for u in self.get_neighbor(v):
                    if u in statuses:
                        if statuses[u] == STATUS_STARTED:
                            contains_cycle = True
                            break
                    else:
                        to_visit.append(u)

                if contains_cycle:
                    break

        return contains_cycle

    def topological_sort(self):
        """
        Determines the priority of vertices to be visited.
        :return:
        """
        STATUS_STARTED = 1
        STATUS_FINISHED = 2
        order = []
        statuses = {}

        assert (not self.contains_cycle())

        for vertex in self.get_vertex():
            to_visit = [vertex]

            while to_visit:
                v = to_visit.pop()

                if v in statuses:
                    if statuses[v] == STATUS_STARTED:
                        statuses[v] = STATUS_FINISHED
                        order.append(v)
                else:
                    statuses[v] = STATUS_STARTED
                    to_visit.append(v)  # add to stack again to signal vertex has finished DFS

                for u in self.get_neighbor(v):
                    if u not in statuses:
                        to_visit.append(u)

        order.reverse()

        return order

    def strongly_connected_components(self):
        """
        Compute the vertices in the strongly connected components
        :return list of lists, one for each component's vertices:
        """
        stack = self.scc_dfs_forward_pass()
        components = self.scc_dfs_reverse_pass(stack)

        return components

    def scc_dfs_forward_pass(self):
        stack = []
        visited = set()

        for v in self.get_vertex():
            self.dfs_forward(v, stack, visited)

        return stack

    def dfs_forward(self, vertex, stack, visited):
        if vertex not in visited:
            visited.add(vertex)
            for u in self.get_neighbor(vertex):
                self.dfs_forward(u, stack, visited)
            stack.append(vertex)

    def scc_dfs_reverse_pass(self, stack):
        components = []
        visited = set()

        while stack:
            v = stack.pop()
            if v not in visited:
                component = []
                self.dfs_reverse(v, component, visited)
                component.reverse()
                components.append(component)

        return components

    def dfs_reverse(self, vertex, component, visited):
        if vertex not in visited:
            visited.add(vertex)
            component.append(vertex)
            for u in self.get_reverse_neighbor(vertex):
                self.dfs_reverse(u, component, visited)


def get_test_graph_1():
    dg = DirectedGraph()
    dg.add_edge(0, 1)
    dg.add_edge(0, 5)
    dg.add_edge(1, 2)
    dg.add_edge(2, 4)
    dg.add_edge(2, 6)
    dg.add_edge(3, 2)
    dg.add_edge(5, 8)
    dg.add_edge(6, 5)
    dg.add_edge(7, 5)
    dg.add_edge(7, 5)

    return dg


def get_test_graph_2():
    dg_small = DirectedGraph()
    dg_small.add_edge(2, 1)
    dg_small.add_edge(4, 5)
    dg_small.add_edge(0, 1)
    dg_small.add_edge(1, 4)
    dg_small.add_edge(1, 3)

    return dg_small


def get_test_graph_3():
    dg_other = DirectedGraph()
    dg_other.add_edge(3, 11)
    dg_other.add_edge(5, 2)
    dg_other.add_edge(2, 4)
    dg_other.add_edge(2, 7)
    dg_other.add_edge(8, 11)
    dg_other.add_edge(4, 7)
    dg_other.add_edge(7, 8)

    return dg_other


def get_test_graph_4():
    """
    Returns graph containing a cycle
    :return:
    """
    dg = copy.copy(get_test_graph_1())
    dg.add_edge(8, 0)  # creates cycle

    return dg


def get_test_graph_5():
    """
    Returns a graph with 3 cycles and 5 strongly connected components
    :return:
    """
    dg = DirectedGraph()
    dg.add_edge(0, 2)
    dg.add_edge(1, 3)
    dg.add_edge(3, 2)
    dg.add_edge(2, 1)
    dg.add_edge(4, 5)
    dg.add_edge(5, 6)
    dg.add_edge(6, 4)
    dg.add_edge(3, 5)
    dg.add_edge(7, 5)
    dg.add_edge(8, 10)
    dg.add_edge(10, 11)
    dg.add_edge(11, 9)
    dg.add_edge(9, 8)

    return dg


def test_dfs():
    dg1 = get_test_graph_1()
    c1, p1 = dg1.dfs()
    assert (c1 == {0, 3, 7})
    assert (p1 == {1: 0, 2: 1, 4: 2, 5: 0, 6: 2, 8: 5})


def test_bfs():
    dg1 = get_test_graph_1()
    p1 = dg1.bfs()
    assert (p1 == {1: 0, 2: 1, 4: 2, 5: 0, 6: 2, 8: 5})


def test_contains_cycle():
    assert (get_test_graph_1().contains_cycle() == False)
    assert (get_test_graph_2().contains_cycle() == False)
    assert (get_test_graph_3().contains_cycle() == False)
    assert (get_test_graph_4().contains_cycle() == True)


def test_topological_sort():
    assert (get_test_graph_1().topological_sort() == [7, 3, 0, 1, 2, 4, 6, 5, 8])
    assert (get_test_graph_2().topological_sort() == [2, 0, 1, 3, 4, 5])
    assert (get_test_graph_3().topological_sort() == [5, 3, 2, 4, 7, 8, 11])


def test_strongly_connected_components():
    dg = get_test_graph_5()

    assert (dg.contains_cycle())

    components = dg.strongly_connected_components()
    assert (components == [[10, 11, 9, 8], [7], [0], [1, 3, 2], [6, 4, 5]])


def main():
    test_dfs()
    test_bfs()
    test_contains_cycle()
    test_topological_sort()
    test_strongly_connected_components()

    print("Tests complete.")


if __name__ == "__main__":
    main()
