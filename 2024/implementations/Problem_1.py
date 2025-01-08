class Problem_1:
    _array1 = []
    _array2 = []
    _sum = 0

    def _getPosition(self, array, item):
        inf = 0
        sup = len(array) - 1
        position = (sup - inf) // 2

        while inf <= sup:
            position = inf + (sup - inf) // 2
            if array[position] < item:
                inf = position + 1
            elif array[position] > item:
                sup = position - 1
            else:
                return position

        return inf

    def parseInput(self, input):
        for line in input:
            item1, item2 = line.split('   ')
            self._array1.insert(self._getPosition(self._array1, int(item1)), int(item1))
            self._array2.insert(self._getPosition(self._array2, int(item2)), int(item2))

    def solve(self):
        for item1, item2 in zip(self._array1, self._array2):
            self._sum = self._sum + abs(item1 - item2)
        print(self._sum)
