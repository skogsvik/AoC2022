def score(char):
    if char <= 'Z':
        return ord(char) - 38  # 27 - ord('A') = -38
    return ord(char) - 96  # 1 - ord('a') = -96


def find_common(iterators):
    return set(iterators[0]).intersection(*iterators[1:]).pop()


def bisect_packs(rucksacks):
    """Split each pack into its two compartments by bisecting the list of item types"""
    for rucksack in rucksacks:
        mid = len(rucksack)//2
        yield rucksack[:mid], rucksack[mid:]


def answer1(rucksacks):
    common_in_compartments = map(find_common, bisect_packs(rucksacks))
    return sum(map(score, common_in_compartments))


def group_by_three(rucksacks):
    for i in range(0, len(rucksacks), 3):
        yield rucksacks[i:i+3]


def answer2(rucksacks):
    common_in_group = map(find_common, group_by_three(rucksacks))
    return sum(map(score, common_in_group))


def main():
    rucksacks = load()
    print(f'Answer 1: {answer1(rucksacks)}')
    print(f'Answer 2: {answer2(rucksacks)}')


def load():
    with open('input/aoc3', encoding='utf-8') as file_:
        return file_.read().rstrip().split('\n')  # readlines, but without trailing newlines


def test_answer1():
    assert answer1(load()) == 8123


def test_answer2():
    assert answer2(load()) == 2620


def test_score():
    import string  # Only needed for testing pylint: disable=import-outside-toplevel
    assert list(range(1, 53)) == list(map(score, string.ascii_letters))


main()
