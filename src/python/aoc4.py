def answer1(ranges):
    return sum(r[0] <= r[2] and r[1] >= r[3]
               or r[2] <= r[0] and r[3] >= r[1]
               for r in ranges)


def answer2(ranges):
    return sum(r[0] <= r[2] <= r[1]
               or r[2] <= r[0] <= r[3]
               for r in ranges)


def main():
    ranges = load()
    print(f'Answer 1: {answer1(ranges)}')
    print(f'Answer 2: {answer2(ranges)}')


def load():
    with open('input/aoc4', encoding='utf-8') as file_:
        return [
            [int(n)
             for range_ in pair.rstrip().split(',')
             for n in range_.split('-')]
            for pair in file_.readlines()]


def test_answer1():
    assert answer1(load()) == 569


def test_answer2():
    assert answer2(load()) == 936


main()
