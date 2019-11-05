import random


def create_map(size: int = 5):
    """
    Method for creating treasure map for player
    :param size: size of map [int]
    :return: treasure_map [list]
    """
    treasure_map = []
    for r in range(size):
        treasure_map.append([])
        for c in range(size):
            treasure_map[r].append(random.randrange(11, 55))
    return treasure_map


def show_map(treasure_map: list):
    """
    Method for showing map
    :param treasure_map: treasure_map for player [list]
    :return: None
    """
    for i in treasure_map:
        print(i)


def get_next_clue(last_clue: int, treasure_map: list):
    """
    Method for getting next clue on map
    :param last_clue: last_clue [int]
    :param treasure_map: treasure_map [list]
    :return: next treasure clue [int]
    """
    row = last_clue / 10 - 1
    column = last_clue % 10 - 1
    return treasure_map[int(row)][int(column)]


def check_treasure(clue: int, treasure_map: list):
    """
    Method for checking if clue is treasure
    :param clue: clue [int]
    :param treasure_map: treasure_map [list]
    :return: True if it is, False if not
    """
    row = clue / 10 - 1
    column = clue % 10 - 1
    return True if treasure_map[int(row)][int(column)] == clue else False


def find_treasure_loop(clues: list, treasure_map: list):
    """
    General function for searching treasure
    :param clues: list of clues [list]
    :param treasure_map: treasure_map [list]
    :return: list of clues
    """
    while not check_treasure(clues[-1], treasure_map):
        clues.append(get_next_clue(clues[-1], treasure_map))
    return clues


def find_treasure_recursion(clues: list, treasure_map: list):
    """
    Method for recursion searching of treasure
    :param clues: list of clues [list]
    :param treasure_map: treasure_map [list]
    :return: list of clues
    """
    if not check_treasure(clues[-1], treasure_map):
        clues.append(get_next_clue(clues[-1], treasure_map))
        return find_treasure_recursion(clues, treasure_map)
    else:
        return clues


def main():
    my_clues_example = [11, 55, 15]
    my_clues_test = [11, 55, 15]
    example_map = [
        [55, 14, 25, 52, 21],
        [44, 31, 11, 53, 43],
        [24, 13, 45, 12, 34],
        [42, 22, 43, 32, 41],
        [51, 23, 33, 54, 15]]
    test_map = [
        [34, 21, 32, 41, 25],
        [14, 42, 43, 14, 31],
        [54, 45, 52, 42, 23],
        [33, 15, 51, 31, 35],
        [21, 52, 33, 13, 23]]
    print('First treasure map:')
    show_map(treasure_map=example_map)
    print("Loop: {}".format(find_treasure_loop(clues=my_clues_example,
                                               treasure_map=example_map)))
    print("Recursion: {}".format(find_treasure_recursion(
        clues=my_clues_example, treasure_map=example_map)))

    print('Second treasure map:')
    show_map(treasure_map=test_map)
    print("Loop: {}".format(find_treasure_loop(
        clues=my_clues_test, treasure_map=test_map)))
    print("Recursion: {}".format(find_treasure_recursion(
        clues=my_clues_test, treasure_map=test_map)))

if __name__ == "__main__":
    main()
