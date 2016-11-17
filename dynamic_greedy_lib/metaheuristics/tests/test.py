from pprint import pprint

from metaheuristics.problems.knapsack import Knapsack
from metaheuristics.techniques.simulated_annealing import SimulatedAnnealing

def runTest():
    file = open('input_1.txt', 'r')
    knapsack = Knapsack.from_file(file)

    pprint(vars(knapsack))

    heuristic = SimulatedAnnealing()

    for index in range(10):
        print("=== Running ", index)
        knapsack = heuristic.execute_once(knapsack)
        pprint(knapsack)

if __name__ == "__main__":
    runTest()