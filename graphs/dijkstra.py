import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])


class GraphWeighted(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v


def dijkstra(graph, source, dest):
    q = queue.PriorityQueue()
    parents = []
    distances = []
    start_weight = float("inf")

    for i in graph.get_vertex():
        weight = start_weight
        if source == i:
            weight = 0
        q.put(([weight, i]))
        distances.append(weight)
        parents.append(None)

    while not q.empty():
        v_tuple = q.get()
        v = v_tuple[1]

        for e in graph.get_edge(v):
            candidate_distance = distances[v] + e.weight
            if distances[e.vertex] > candidate_distance:
                distances[e.vertex] = candidate_distance
                parents[e.vertex] = v
                q.put(([distances[e.vertex], e.vertex]))

    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        end = parents[end]

    shortest_path.reverse()

    return shortest_path, distances[dest]


def main():
    g = GraphWeighted(9)
    g.add_edge(0, 1, 4)
    g.add_edge(1, 7, 6)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 0, 4)
    g.add_edge(2, 1, 1)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 2, 3)
    g.add_edge(3, 7, 1)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 3, 2)
    g.add_edge(4, 5, 1)
    g.add_edge(5, 4, 1)
    g.add_edge(5, 3, 1)
    g.add_edge(5, 6, 1)
    g.add_edge(6, 5, 1)
    g.add_edge(6, 7, 2)
    g.add_edge(6, 8, 2)
    g.add_edge(7, 1, 6)
    g.add_edge(7, 3, 1)
    g.add_edge(7, 6, 2)
    g.add_edge(7, 8, 2)
    g.add_edge(8, 7, 2)
    g.add_edge(8, 6, 2)

    shortest_path, distance = dijkstra(g, 0, 8)
    assert shortest_path == [0, 1, 2, 3, 7, 8] and distance == 11

    shortest_path, distance = dijkstra(g, 5, 0)
    assert shortest_path == [5, 3, 2, 1, 0] and distance == 9

    shortest_path, distance = dijkstra(g, 1, 1)
    assert shortest_path == [1] and distance == 0


if __name__ == "__main__":
    main()
