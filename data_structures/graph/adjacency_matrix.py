def create_adjacency_matrix(V, edges):
    matrix = [[0] * V for _ in range(V)]

    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1

    return matrix


def main():
    V_1 = 3
    edges_1 = [(0, 1), (1, 2), (2, 0)]
    matrix_1 = create_adjacency_matrix(V_1, edges_1)
    for row in matrix_1:
        print(row)

    print()

    V_2 = 4
    edges_2 = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 0)]
    matrix_2 = create_adjacency_matrix(V_2, edges_2)
    for row in matrix_2:
        print(row)


if __name__ == '__main__':
    main()
