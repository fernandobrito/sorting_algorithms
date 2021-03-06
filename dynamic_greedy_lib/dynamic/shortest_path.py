import copy

"""
Find shortest distance between all pairs of vertices in a directed graph
using Floyd Warshall algorithm.

Applications:
    "The Floyd–Warshall algorithm can be used to solve the following problems,
    among others: Transitive closure of directed graphs, Finding a regular
    expression denoting the regular language, Inversion of real matrices,
    Optimal routing, Computing canonical form of difference bound matrices (DBMs)"
    [Wikipedia]

Complexity: O(n^3)
    Iterate n times over all cells (n^2). n * n^2 = n^3

Author: Fernando Brito (11111309)

Resources:
    - http://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/
    - https://www.youtube.com/watch?v=KQ9zlKZ5Rzc
"""

def solve(input):
    """
    :param input: adjacency matrix. Use None to mark absence of edges
    :return: matrix with shortest path between all vertices
    """

    # Create a copy of input
    solution = copy.deepcopy(input)

    # Replace None with infinity
    _replace_none_with_inf(solution)

    # Get number of vertices (square matrix)
    number_vertices = len(solution)

    # Add all vertices one by one to the set of intermediate vertices
    for vertex_index in range(number_vertices):

        # Pick all vertices as source one by one
        for source in range(number_vertices):

            # Pick all vertices as destination
            for destination in range(number_vertices):

                # If going from source to destination, considering
                # the new vertex_index, is better than what we
                # already have, update it
                best_path_so_far = solution[source][destination]
                new_path = solution[source][vertex_index] + \
                            solution[vertex_index][destination]

                solution[source][destination] = min(best_path_so_far, new_path)

    # Return solution
    return solution


def _replace_none_with_inf(table):
    """
    Replace, in-place, all None's with infinity
    """
    inf = float("inf")

    for row in range(len(table)):
        for column in range(len(table[row])):
            table[row][column] = inf if table[row][column] is None else table[row][column]