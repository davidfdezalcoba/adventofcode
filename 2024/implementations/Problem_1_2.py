class Problem_1_2:
    _dict1 = {}
    _dict2 = {}
    _sum = 0

    def parseInput(self, input):
        for line in input:
            item1, item2 = line.split('   ')
            self._dict1.setdefault(int(item1), 0)
            self._dict2.setdefault(int(item2), 0)
            self._dict1.setdefault(int(item2), 0)
            self._dict2.setdefault(int(item1), 0)
            self._dict1[int(item1)] = self._dict1[int(item1)] + 1
            self._dict2[int(item2)] = self._dict2[int(item2)] + 1

    def solve(self):
        for key in self._dict1.keys():
            self._sum = self._sum + key * self._dict1[key] * self._dict2[key]
        print(self._sum)
