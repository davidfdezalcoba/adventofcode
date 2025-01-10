class Problem_4_2:
    _sum = 0
    _matrix = []

    def parseInput(self, input):
        self._matrix = [row[:-1] for row in input]
        for i, ei in enumerate(self._matrix):
            for j, ej in enumerate(ei):
                if ej == 'A':
                    if i - 1 < 0 or i + 1 >= len(self._matrix) or j - 1 < 0 or j + 1 >= len(self._matrix):
                        continue
                    plus_45 = self._matrix[i + 1][j + 1] == 'M' and self._matrix[i - 1][j - 1] == 'S'
                    plus_45 = plus_45 or self._matrix[i + 1][j + 1] == 'S' and self._matrix[i - 1][j - 1] == 'M'
                    minus_45 = self._matrix[i + 1][j - 1] == 'M' and self._matrix[i - 1][j + 1] == 'S'
                    minus_45 = minus_45 or self._matrix[i + 1][j - 1] == 'S' and self._matrix[i - 1][j + 1] == 'M'
                    if plus_45 and minus_45:
                        self._sum = self._sum + 1

    def solve(self):
        print(self._sum)
