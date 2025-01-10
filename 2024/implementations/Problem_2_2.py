class Problem_2_2:
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
            # Since input reports are not long, we can check every sublist in a reasonable
            # time. So we remove one element at a time and check
            else:
                for index, elem in enumerate(levels):
                    if index == 0 and self._isOk(levels[1:]):
                        self._sum = self._sum + 1
                        break
                    elif index == len(levels) - 1 and self._isOk(levels[:len(levels) - 1]):
                        self._sum = self._sum + 1
                        break
                    elif self._isOk(levels[0:index] + levels[index + 1:len(levels)]):
                        self._sum = self._sum + 1
                        break

    def solve(self):
        print(self._sum)
