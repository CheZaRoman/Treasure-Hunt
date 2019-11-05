import random
EXAMPLE_MAP = [
    [55, 14, 25, 52, 21],
    [44, 31, 11, 53, 43],
    [24, 13, 45, 12, 34],
    [42, 22, 43, 32, 41],
    [51, 23, 33, 54, 15]]

TEST_MAP = [
    [34, 21, 32, 41, 25],
    [14, 42, 43, 14, 31],
    [54, 45, 52, 42, 23],
    [33, 15, 51, 31, 35],
    [21, 52, 33, 13, 23]]


class TreasureHunterError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class TreasureMap:

    def __init__(self, treasure_map=list(), size=5):
        if treasure_map:
            self.treasure_map = treasure_map
            self.size = len(treasure_map)
        else:
            self.size = size
            self.treasure_map = []
            for r in range(self.size):
                self.treasure_map.append([])
                for c in range(self.size):
                    self.treasure_map[r].append(random.randrange(11, 55))

    def __getitem__(self, row: int):
        return self.treasure_map[int(row)]

    def show(self):
        for i in self.treasure_map:
            print(i)


class TreasureHunter:
    DEFAULT_CLUES = [11, 55, 15]

    def __init__(self, clues=DEFAULT_CLUES, treasure_map=None):
        self.clues = clues.copy()
        self.treasure_map = treasure_map
        self.treasure = None
        self.count_down = 0
        self.entry_point = clues[-1]
        if not self.treasure_map:
            raise TreasureHunterError(message='You need a map of treasure!')

    @property
    def row(self):
        return int(self.get_last_clue / 10) - 1

    @property
    def column(self):
        return int(self.get_last_clue % 10) - 1

    @property
    def get_last_clue(self):
        return self.clues[-1]

    @property
    def get_next_clue(self):
        posible_next_clue = self.treasure_map[self.row][self.column]
        if self.entry_point == posible_next_clue or posible_next_clue in self.clues:
            raise TreasureHunterError('It\'s looping...')
        else:
            return posible_next_clue

    def __check_treasure(self):
        return True if self.treasure_map[self.row][
                           self.column] == self.get_last_clue else False

    def __check_treasure_without_checking(self):
        try:
            row = self.get_last_clue / 10 - 1
            column = self.get_last_clue % 10 - 1
            if self.treasure_map[row][column] == self.get_last_clue:
                self.treasure = self.get_last_clue
                return True
            else:
                return False
        except IndexError:
            raise TreasureHunterError(
                message="Invalid treasure map! Try another.")

    def find_treasure_loop(self):
        while not self.__check_treasure_without_checking() and not self.treasure:
            self.clues.append(self.get_next_clue)
            self.count_down += 1
        return self.clues

    def find_treasure_recursion(self):
        try:
            if not self.__check_treasure_without_checking():
                self.clues.append(self.get_next_clue)
                return self.find_treasure_recursion()
            else:
                return self.clues
        except Exception as e:
            raise e

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type:
            return type


def main():
    print('First treasure map:')
    trsr_map_example = TreasureMap(treasure_map=EXAMPLE_MAP)
    with TreasureHunter(treasure_map=trsr_map_example) as trsr_hunter_example:
        trsr_map_example.show()
        print("Loop: {}".format(trsr_hunter_example.find_treasure_loop()))
        print("Recursion: {}".format(trsr_hunter_example.find_treasure_recursion()))

    print('Second treasure map:')
    trsr_map_test = TreasureMap(treasure_map=TEST_MAP)
    with TreasureHunter(treasure_map=trsr_map_test) as trsr_hunter_test:
        trsr_map_test.show()
        print("Loop: {}".format(trsr_hunter_test.find_treasure_loop()))
        print("Recursion: {}".format(trsr_hunter_test.find_treasure_recursion()))

    print('Random treasure map:')
    trsr_map_test = TreasureMap()
    with TreasureHunter(treasure_map=trsr_map_test) as trsr_hunter_test:
        trsr_map_test.show()
        print("Loop: {}".format(trsr_hunter_test.find_treasure_loop()))
        print("Recursion: {}".format(trsr_hunter_test.find_treasure_recursion()))

if __name__ == "__main__":
    main()
