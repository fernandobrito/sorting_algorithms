from pprint import pprint

from metaheuristics.problems.knapsack import Knapsack
from metaheuristics.techniques.simulated_annealing import SimulatedAnnealing

def runTest():
    file = open('mknap1_1.txt', 'r')
    knapsack = Knapsack.from_file(file)

    pprint(vars(knapsack))

    heuristic = SimulatedAnnealing()

    # Fill the knapsack randomly
    knapsack = knapsack.randomize()


    for index in range(5):
        print("\n\n=== Running ", index)
        print("Current")
        pprint(vars(knapsack))
        knapsack = heuristic.execute_once(knapsack)

if __name__ == "__main__":
    runTest()