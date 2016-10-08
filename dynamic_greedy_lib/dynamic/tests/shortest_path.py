from utils.tests import TestRunner
from dynamic import shortest_path

runner = TestRunner(shortest_path.solve)

# Empty graph
runner.expect_equal([],[])

runner.expect_equal(
    [[None]]
    ,
    [[float("inf")]]
)

# Very simple graph
runner.expect_equal(
    [[0, 1],
     [2, 0]]
    ,
    [[0, 1],
     [2, 0]]
)

# Example from video: https://www.youtube.com/watch?v=KQ9zlKZ5Rzc
runner.expect_equal(
    [[0, None, 3, 0],
     [-2, 0, None, 1],
     [None, None, 0, 5],
     [None, 4, None, 0]]
    ,
    [[0, 4, 3, 0],
     [-2, 0, 1, -2],
     [7, 9, 0, 5],
     [2, 4, 5, 0]]
)