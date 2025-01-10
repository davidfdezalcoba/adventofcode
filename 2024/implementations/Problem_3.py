from re import finditer
from functools import reduce


class Problem_3:
    _pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    _sum = 0

    def parseInput(self, input):
        for line in input:
            matches = finditer(self._pattern, line)
            muls = list(map(lambda n: int(n.group(1)) * int(n.group(2)), matches))
            self._sum = self._sum + reduce(lambda n, m: n + m, muls)

    def solve(self):
        print(self._sum)
