import queue


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

    def get_edge(self, vertex):
        """
        Generator for returning the next vertex adjacent to the given vertex
        :param vertex:
        :return:
        """
        if vertex in self.adjacency_list:
            for u in self.adjacency_list[vertex]:
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

                for neighbor in self.get_edge(v):
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

                for neighbor in self.get_edge(v):
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
                    to_visit.append(v)  # add to stack to signal vertex has finished DFS

                for u in self.get_edge(v):
                    if u in statuses:
                        if statuses[u] == STATUS_STARTED:
                            contains_cycle = True
                            break
                    else:
                        to_visit.append(u)

                if contains_cycle:
                    break

        return contains_cycle


def main():
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
    # dg.add_edge(8, 0) # uncomment to create a cycle

    components, dfs_parents = dg.dfs()

    print("Components: ", components)
    print("Parents (dfs): ", dfs_parents)

    bfs_parents = dg.bfs()
    print("Parents (bfs): ", bfs_parents)

    print("Contains a cycle: ", dg.contains_cycle())


if __name__ == "__main__":
    main()
