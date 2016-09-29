import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])


class GraphUndirectedWeighted(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))

    def get_neighbor(self, vertex):
        """
        Returns the next neighbor to vertex
        :param vertex:
        :rtype: Edge
        """
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v

    def dijkstra(self, source, dest):
        q = queue.PriorityQueue()
        parents = []
        distances = []
        start_weight = float("inf")

        for i in self.get_vertex():
            weight = start_weight
            if source == i:
                weight = 0
            distances.append(weight)
            parents.append(None)

        q.put(([0, source]))

        while not q.empty():
            v_tuple = q.get()
            v = v_tuple[1]

            for e in self.get_neighbor(v):
                candidate_distance = distances[v] + e.weight
                if distances[e.vertex] > candidate_distance:
                    distances[e.vertex] = candidate_distance
                    parents[e.vertex] = v
                    # primitive but effective negative cycle detection
                    if candidate_distance < -1000:
                        raise Exception("Negative cycle detected")
                    q.put(([distances[e.vertex], e.vertex]))

        shortest_path = []
        end = dest
        while end is not None:
            shortest_path.append(end)
            end = parents[end]

        shortest_path.reverse()

        return shortest_path, distances[dest]

    def prim(self):
        """
        Returns a dictionary of parents of vertices in a minimum spanning tree
        :rtype: dict
        """
        s = set()
        q = queue.PriorityQueue()
        parents = {}
        start_weight = float("inf")
        weights = {}  # since we can't peek into queue

        for i in self.get_vertex():
            weight = start_weight
            if i == 0:
                q.put(([0, i]))
            weights[i] = weight
            parents[i] = None

        while not q.empty():
            v_tuple = q.get()
            vertex = v_tuple[1]

            s.add(vertex)

            for u in self.get_neighbor(vertex):
                if u.vertex not in s:
                    if u.weight < weights[u.vertex]:
                        parents[u.vertex] = vertex
                        weights[u.vertex] = u.weight
                        q.put(([u.weight, u.vertex]))

        return parents


def main():
    g = GraphUndirectedWeighted(9)
    g.add_edge(0, 1, 4)
    g.add_edge(1, 7, 6)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 7, 1)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 5, 1)
    g.add_edge(5, 6, 1)
    g.add_edge(6, 7, 2)
    g.add_edge(6, 8, 2)
    g.add_edge(7, 8, 2)
    # for testing negative cycles
    # g.add_edge(1, 9, -5)
    # g.add_edge(9, 7, -4)

    shortest_path, distance = g.dijkstra(0, 1)
    assert shortest_path == [0, 1] and distance == 4

    shortest_path, distance = g.dijkstra(0, 8)
    assert shortest_path == [0, 1, 2, 3, 7, 8] and distance == 11

    shortest_path, distance = g.dijkstra(5, 0)
    assert shortest_path == [5, 3, 2, 1, 0] and distance == 9

    shortest_path, distance = g.dijkstra(1, 1)
    assert shortest_path == [1] and distance == 0

    msp = g.prim()
    print(msp)
    assert(msp == {0: None, 1: 0, 2: 1, 3: 2, 4: 5, 5: 3, 6: 5, 7: 3, 8: 6})


if __name__ == "__main__":
    main()
