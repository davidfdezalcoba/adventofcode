import sys
import importlib

NUM_PROBLEM = sys.argv[1]


def main():
    if '_' in NUM_PROBLEM:
        file = f'Problem_{NUM_PROBLEM[:-2]}'
        input = f'{NUM_PROBLEM[:-2]}'
        cl = f'Problem_{NUM_PROBLEM}'
    else:
        file = f'Problem_{NUM_PROBLEM}'
        input = f'{NUM_PROBLEM}'
        cl = f'Problem_{NUM_PROBLEM}'
    implementations = importlib.import_module(f'implementations.{file}')
    Problem = getattr(implementations, cl)
    problem = Problem()

    with open(f'./inputs/{input}.txt', 'r') as input:
        problem.parseInput(input)

    problem.solve()


if __name__ == '__main__':
    main()
