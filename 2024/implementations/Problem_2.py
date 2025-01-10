class Problem_2:
    _sum = 0

    def _isOk(self, levels):
        isIncreasing = levels[1] > levels[0]
        i = 0
        while i < len(levels) - 1:
            sum = levels[i + 1] - levels[i]
            if sum == 0:
                return False
            if isIncreasing and sum < 0:
                return False
            if not isIncreasing and sum > 0:
                return False
            if abs(sum) > 3:
                return False
            i = i + 1
        return True

    def parseInput(self, input):
        for line in input:
            levels = [int(item) for item in line.split(' ')]
            if self._isOk(levels):
                self._sum = self._sum + 1

    def solve(self):
        print(self._sum)
