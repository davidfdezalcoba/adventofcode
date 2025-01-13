class Problem_4:
    _sum = 0
    _matrix = []
    # 0 -> N
    # 1 -> NE
    # 2 -> E
    # 3 -> SE
    # 4 -> S
    # 5 -> SW
    # 6 -> W
    # 7 -> NW

    def palabra(self, i, j, dir):
        ll = len(self._matrix)
        match dir:
            case 0:
                if i - 3 < 0:
                    return None
                aux = [s[j] for s in self._matrix[i - 3:i]]
                aux.reverse()
                return aux
            case 1:
                if i + 3 >= ll or j - 3 < 0:
                    return None
                aux = []
                for ii in range(3):
                    aux.append(self._matrix[i + 1 + ii][j - 1 - ii])
                return aux
            case 2:
                if j + 3 >= ll:
                    return None
                return list(self._matrix[i][j + 1:j + 4])
            case 3:
                if i + 3 >= ll or j + 3 >= ll:
                    return None
                aux = []
                for ii in range(3):
                    aux.append(self._matrix[i + 1 + ii][j + 1 + ii])
                return aux
            case 4:
                if i + 3 > ll:
                    return None
                return [s[j] for s in self._matrix[i + 1:i + 4]]
            case 5:
                if j + 3 >= ll or i - 3 < 0:
                    return None
                aux = []
                for ii in range(3):
                    aux.append(self._matrix[i - 1 - ii][j + 1 + ii])
                return aux
            case 6:
                if j - 3 < 0:
                    return None
                aux = list(self._matrix[i][j - 3:j])
                aux.reverse()
                return aux
            case 7:
                if i - 3 < 0 or j - 3 < 0:
                    return None
                aux = []
                for ii in range(3):
                    aux.append(self._matrix[i - 1 - ii][j - 1 - ii])
                return aux

    def parseInput(self, input):
        self._matrix = [row[:-1] for row in input]
        for i, ei in enumerate(self._matrix):
            for j, ej in enumerate(ei):
                if ej == 'X':
                    for dir in range(8):
                        p = self.palabra(i, j, dir)
                        if p and 'X' + ''.join(p) == 'XMAS':
                            self._sum = self._sum + 1

    def solve(self):
        print(self._sum)


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
