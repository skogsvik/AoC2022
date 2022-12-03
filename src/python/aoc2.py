import re


def answer1(all_rounds):
    # A|X: Rock
    # B|Y: Paper
    # C|Z: Scissors
    return (
        6 * len(re.findall(r'A Y|B Z|C X', all_rounds))  # Win
        + 3 * len(re.findall(r'A X|B Y|C Z', all_rounds))  # Draw
        + 1 * all_rounds.count('X')  # Rock
        + 2 * all_rounds.count('Y')  # Paper
        + 3 * all_rounds.count('Z')  # Scissors
    )


def answer2(all_rounds):
    # A: Rock
    # B: Paper
    # C: Scissors
    # X: Lose
    # Y: Draw
    # Z: Win
    return (
        6 * all_rounds.count('Z')  # Win
        + 3 * all_rounds.count('Y')  # Draw
        + 1 * len(re.findall(r'A Y|B X|C Z', all_rounds))  # Rock
        + 2 * len(re.findall(r'A Z|B Y|C X', all_rounds))  # Paper
        + 3 * len(re.findall(r'A X|B Z|C Y', all_rounds))  # Scissors
    )


def main():
    all_rounds = load()
    print(f'Answer 1: {answer1(all_rounds)}')
    print(f'Answer 2: {answer2(all_rounds)}')


def load():
    with open('input/aoc2', encoding='utf-8') as file_:
        return file_.read()


def test_answer1():
    assert answer1(load()) == 11841


def test_answer2():
    assert answer2(load()) == 13022


main()
