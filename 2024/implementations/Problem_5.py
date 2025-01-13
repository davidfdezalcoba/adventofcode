class Problem_5:
    _orders = {}
    _instructions = False
    _sum = 0

    def parseInput(self, input):
        for line in input:
            if line == '\n':
                self._instructions = True
            elif not self._instructions:
                page_before, page_after = map(lambda n: int(n), line.split('|'))
                if page_before in self._orders.keys():
                    self._orders.get(page_before).append(page_after)
                else:
                    self._orders[page_before] = [page_after]
            else:
                update = [int(e) for e in line.split(',')]
                if self._solve(update):
                    self._sum = self._sum + update[len(update) // 2]

    def _solve(self, update):
        for index, elem in enumerate(update):
            before = update[:index]
            for b in before:
                if b in self._orders.get(elem, []):
                    return False
        return True

    def solve(self):
        print(self._sum)


class Problem_5_2:
    _orders = {}
    _instructions = False
    _sum = 0

    def parseInput(self, input):
        for line in input:
            if line == '\n':
                self._instructions = True
            elif not self._instructions:
                page_before, page_after = map(lambda n: int(n), line.split('|'))
                if page_before in self._orders.keys():
                    self._orders.get(page_before).append(page_after)
                else:
                    self._orders[page_before] = [page_after]
            else:
                update = [int(e) for e in line.split(',')]
                if not self._solve(update):
                    self._sum = self._sum + update[len(update) // 2]

    def _solve(self, update):
        is_ok = True
        index = 0
        while index < len(update):
            before = update[:index]
            for i, b in enumerate(before):
                if b in self._orders.get(update[index], []):
                    update.insert(index + 1, update.pop(i))
                    index = index - 1
                    is_ok = False
            index = index + 1
        return is_ok

    def solve(self):
        print(self._sum)
