def rfind_duplicate_offset(message, length):
    """
    Find the index right after the leftmost part of the rightmost duplicate pair
    """
    for i, char in enumerate(message[:0:-1], 1):
        if (pos := message.rfind(char, 0, length - i)) >= 0:
            # NOTE: There are cases where there might be a later duplicate (e.g. wzzw), but the
            # increase in big-O complexity kills any potential time save as it is likely rare
            return pos + 1
    return False


def find_pos_after_unique_seq(message, length):
    # return length + next(i for i in range(len(message)) if all_unique(message[i:i+length]))
    i = 0
    while offset := rfind_duplicate_offset(message[i:i+length], length):
        i += offset
    return i + length


def answer1(message):
    return find_pos_after_unique_seq(message, 4)


def answer2(message):
    return find_pos_after_unique_seq(message, 14)


def main():
    message = load()
    print(f'Answer 1: {answer1(message)}')
    print(f'Answer 2: {answer2(message)}')


def load():
    with open('input/aoc6', encoding='utf-8') as file_:
        return file_.read().rstrip()


def test_answer1():
    assert answer1(load()) == 1658


def test_answer2():
    assert answer2(load()) == 2260


main()
