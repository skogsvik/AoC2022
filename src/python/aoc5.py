def find_final_stack_tops(instructions, getter):
    stacks, movements = instructions
    for quantity, src, destination in movements:
        stacks[destination] += getter(stacks[src], quantity)
        del stacks[src][-quantity:]
    return ''.join(s[-1] for s in stacks)


def answer1(instructions):
    return find_final_stack_tops(instructions, lambda stack, quantity: stack[:-quantity-1:-1])


def answer2(instructions):
    return find_final_stack_tops(instructions, lambda stack, quantity: stack[-quantity:])


def main():
    print(f'Answer 1: {answer1(load())}')
    print(f'Answer 2: {answer2(load())}')


def load():
    with open('input/aoc5', encoding='utf-8') as file_:
        stack_data, movement_data = map(str.splitlines, file_.read().rstrip().split('\n\n'))

    stack_centers = range(1, len(stack_data[-1]), 4)
    stacks = [
        [line[col] for line in stack_data[-2::-1] if line[col] != ' ']
        for col in stack_centers
    ]

    movements = [list(map(int, line.split(' ')[1::2])) for line in movement_data]
    for line in movements:
        # 0-indexing
        line[1] -= 1
        line[2] -= 1
    return stacks, movements


def test_answer1():
    assert answer1(load()) == 'RLFNRTNFB'


def test_answer2():
    assert answer2(load()) == 'MHQTLJRLB'


main()
