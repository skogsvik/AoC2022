def answer1(sorted_total_calories_per_elf):
    return sorted_total_calories_per_elf[-1]


def answer2(sorted_total_calories_per_elf):
    return sum(sorted_total_calories_per_elf[-3:])


def get_sorted_total_calories_per_elf():
    return sorted([sum(e) for e in load()])


def main():
    sorted_total_calories_per_elf = get_sorted_total_calories_per_elf()
    print(f'Answer 1: {answer1(sorted_total_calories_per_elf)}')
    print(f'Answer 2: {answer2(sorted_total_calories_per_elf)}')


def load():
    with open('input/aoc1', encoding='utf-8') as file_:
        return [
            [int(calories) for calories in elf.split()]
            for elf in file_.read().split('\n\n')
        ]


def test_answer1():
    assert answer1(get_sorted_total_calories_per_elf()) == 68442


def test_answer2():
    assert answer2(get_sorted_total_calories_per_elf()) == 204837


main()
