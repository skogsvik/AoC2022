import numpy as np


def move_head(head, direction):
    if direction == 'U':
        head[1] += 1
    elif direction == 'D':
        head[1] -= 1
    elif direction == 'R':
        head[0] += 1
    elif direction == 'L':
        head[0] -= 1
    else:
        raise ValueError(f"{direction} is not a valid movement")


def update_segments(segments):
    for first, second in zip(segments, segments[1:]):
        move_segment(first, second)


def move_segment(first, second):
    # NOTE: Checking each pair individually is oddly enough faster than an array based solution here
    if abs(first[0] - second[0]) >= 2 or abs(first[1] - second[1]) >= 2:
        second += np.sign(first - second)


def move_rope(movements, n_segments):
    rope = [np.zeros(2, dtype=np.int32) for _ in range(n_segments+1)]
    tail_visited = {tuple(rope[-1])}
    for direction, count in movements:
        for _ in range(count):
            move_head(rope[0], direction)
            update_segments(rope)
            tail_visited.add(tuple(rope[-1]))
    return len(tail_visited)


def answer1(movements):
    return move_rope(movements, 1)


def answer2(movements):
    return move_rope(movements, 9)


def main():
    movements = load()
    print(f'Answer 1: {answer1(movements)}')
    print(f'Answer 2: {answer2(movements)}')


def load():
    with open('input/aoc9', encoding='utf-8') as file_:
        lines = (line.split(' ', 1) for line in file_.readlines())
    return [(d, int(n)) for d, n in lines]


def test_answer1():
    assert answer1(load()) == 5513


def test_answer2():
    assert answer2(load()) == 2427


main()
