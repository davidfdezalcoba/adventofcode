from abc import ABC, abstractmethod
import sys
import importlib

NUM_PROBLEM = sys.argv[1]


def main():
    implementations = importlib.import_module(f'implementations.Problem_{NUM_PROBLEM}')
    Problem = getattr(implementations, f'Problem_{NUM_PROBLEM}')
    problem = Problem()

    with open(f'./inputs/{NUM_PROBLEM}.txt', 'r') as input:
        problem.parseInput(input)

    problem.solve()


if __name__ == '__main__':
    main()
