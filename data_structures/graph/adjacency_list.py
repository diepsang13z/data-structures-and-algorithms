class Node:

    def __init__(self, data: any) -> None:
        self.vertex: any = data
        self.next: Node = None


class Graph:

    def __init__(self, V: int) -> None:
        self.V: int = V
        self.graph: list[Node] = [None] * V

    def add_edge(self, src: int, dest: int) -> None:
        node: Node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node: Node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def visualize(self) -> None:
        for i in range(self.V):
            content = f'{i}'
            neighbor = self.graph[i]
            while neighbor:
                content += f' -> {neighbor.vertex}'
                neighbor = neighbor.next
            print(content)


def main():
    V = 5
    graph = Graph(V)

    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.visualize()


if __name__ == '__main__':
    main()
