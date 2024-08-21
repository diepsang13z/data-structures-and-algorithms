from collections import defaultdict


class Graph:

    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def visualize(self):
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                edges.append((node, neighbor))
        return edges


def main():
    graph = Graph()
    graph.add_edge('a', 'c')
    graph.add_edge('b', 'c')
    graph.add_edge('b', 'e')
    graph.add_edge('c', 'd')
    graph.add_edge('c', 'e')
    graph.add_edge('c', 'a')
    graph.add_edge('c', 'b')
    graph.add_edge('e', 'b')
    graph.add_edge('d', 'c')
    graph.add_edge('e', 'c')
    print(graph.visualize())
    print(graph.graph)


if __name__ == '__main__':
    main()
