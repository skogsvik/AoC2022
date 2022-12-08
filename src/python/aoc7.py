
def answer1(directory_sizes):
    return sum(size for size in directory_sizes if size <= 100_000)


def answer2(directory_sizes):
    needed_space = directory_sizes[-1] - 40_000_000  # Space required to get 30_000_000 free space
    return min(size for size in directory_sizes if size >= needed_space)


def main():
    directory_sizes = load()
    print(f'Answer 1: {answer1(directory_sizes)}')
    print(f'Answer 2: {answer2(directory_sizes)}')


def load():
    with open('input/aoc7', encoding='utf-8') as file_:
        lines = file_.readlines()

    # Assume that we only visit each directory once and can therefore parse struture in a stack
    completed_dirs = []  # Directory sizes for directories which have been fully traversed
    current_dirs = []  # Stack with current directory tree which is not completely traversed yet

    for line in lines:
        # Ignore lines which don't add new info
        if line.startswith('$ ls') or line.startswith('dir'):
            continue

        # Go up one level and add directory size to parent
        if line.startswith('$ cd ..'):
            # NOTE: this could cause problems if we ever exited the root directory again
            current_dirs[-2] += current_dirs[-1]
            completed_dirs.append(current_dirs.pop())
            continue

        # Go down one level, add one more directory to stack
        if line.startswith('$ cd'):
            current_dirs.append(0)
            continue

        # File, add size to current directory
        file_size = int(line.split(' ', 1)[0])
        current_dirs[-1] += file_size

    # Exit the current directory tree
    while len(current_dirs) >= 2:
        current_dirs[-2] += current_dirs[-1]
        completed_dirs.append(current_dirs.pop())
    completed_dirs.append(current_dirs.pop())  # Pop off the root

    assert not current_dirs
    return completed_dirs


def test_answer1():
    assert answer1(load()) == 1297683


def test_answer2():
    assert answer2(load()) == 5756764


main()
