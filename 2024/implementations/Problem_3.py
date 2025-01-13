from re import finditer, sub
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


class Problem_3_2:
    _pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    _do_pattern = r'(don\'t\(\)(.|\n)*?do\(\))'
    _dont_pattern = r'(don\'t\(\).*$)'
    _sum = 0

    def parseInput(self, input):
        line = input.read()
        line = sub(self._do_pattern, 'disabled', line)
        line = sub(self._dont_pattern, 'disabled', line)
        matches = finditer(self._pattern, line)
        muls = list(map(lambda n: int(n.group(1)) * int(n.group(2)), matches))
        partial_sum = reduce(lambda n, m: n + m, muls)
        self._sum = self._sum + partial_sum

    def solve(self):
        print(self._sum)
