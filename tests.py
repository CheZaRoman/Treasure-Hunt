from first_imp import find_treasure_loop, find_treasure_recursion
from second_imp import TreasureMap, TreasureHunter

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

EXAMPLE_MAP_WITH_ERROR = [[55, 14, 25, 52, 21],
                          [49, 31, 11, 53, 43],
                          [24, 13, 45, 12, 34],
                          [42, 22, 43, 32, 41],
                          [51, 23, 33, 54, 15]]

RESULT_TEST = [11, 55, 15, 25, 31, 54, 13, 32, 45, 35, 23, 43, 51, 21, 14, 41,
               33, 52]

RESULT_EXEMPLE = [11, 55, 15, 21, 44, 32, 13, 25, 43]

RND_treasure_map = [
    [15, 44, 31, 31, 34],
    [21, 14, 13, 53, 30],
    [49, 26, 20, 21, 20],
    [38, 17, 50, 28, 51],
    [33, 42, 52, 32, 24]]

RND_treasure_map_result = [11, 55, 15, 34, 21]

def test_function_loop_1():
    result = find_treasure_loop(clues=[11, 55, 15], treasure_map=TEST_MAP)
    assert RESULT_TEST == result


def test_function_recursion_1():
    result = find_treasure_recursion(clues=[11, 55, 15], treasure_map=TEST_MAP)
    assert RESULT_TEST == result


def test_function_loop_2():
    result = find_treasure_loop(clues=[11, 55, 15], treasure_map=EXAMPLE_MAP)
    assert RESULT_EXEMPLE == result


def test_function_recursion_2():
    result = find_treasure_recursion(clues=[11, 55, 15],
                                     treasure_map=EXAMPLE_MAP)
    assert RESULT_EXEMPLE == result


def test_loop_1():
    trsr_map_example = TreasureMap(treasure_map=EXAMPLE_MAP)
    trsr_hunter_example = TreasureHunter(treasure_map=trsr_map_example)
    assert RESULT_EXEMPLE == trsr_hunter_example.find_treasure_loop()


def test_loop_2():
    trsr_map_example = TreasureMap(treasure_map=TEST_MAP)
    trsr_hunter_example = TreasureHunter(treasure_map=trsr_map_example)
    assert RESULT_TEST == trsr_hunter_example.find_treasure_loop()


def test_recursion_1():
    trsr_map_example = TreasureMap(treasure_map=EXAMPLE_MAP)
    trsr_hunter_example = TreasureHunter(treasure_map=trsr_map_example)
    assert RESULT_EXEMPLE == trsr_hunter_example.find_treasure_recursion()


def test_recursion_2():
    trsr_map_example = TreasureMap(treasure_map=TEST_MAP)
    trsr_hunter_example = TreasureHunter(treasure_map=trsr_map_example)
    assert RESULT_TEST == trsr_hunter_example.find_treasure_recursion()


def test_rnd():
    trsr_rnd_example = TreasureMap(treasure_map=RND_treasure_map)
    trsr_hunter_example = TreasureHunter(treasure_map=trsr_rnd_example)
    assert RND_treasure_map_result == \
           trsr_hunter_example.find_treasure_recursion()


def test_empty_result():
    empty = [[32, 29, 41, 37, 24],
             [53, 24, 40, 26, 52],
             [13, 44, 29, 11, 17],
             [20, 48, 18, 11, 39],
             [42, 12, 43, 14, 21]]
    trsr_rnd_example = TreasureMap(treasure_map=empty)
    with TreasureHunter(treasure_map=trsr_rnd_example) as trsr_hunter_example:
        assert None == trsr_hunter_example.find_treasure_recursion()
