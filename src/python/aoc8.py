import numpy as np

# Don't check sides since they are always visible/have at least one direction with 0 score
INNER = slice(1, -1)


def check_visibility_from_left(forest, visibility_mask):
    for tree_row, mask in zip(forest[INNER], visibility_mask[INNER]):
        mask[INNER] = [visible or (tree > tree_row[:i]).all()
                       for i, (tree, visible) in enumerate(zip(tree_row[INNER], mask[INNER]), 1)]


def view_distance(height, other_trees):
    for i, other_height in enumerate(other_trees, 1):
        if height <= other_height:
            return i
    return len(other_trees)


def score_view_to_the_right(forest):
    return [
        [
            view_distance(tree, tree_row[i+1:])
            for i, tree in enumerate(tree_row[INNER], 1)
        ]
        for tree_row in forest[INNER]
    ]


def answer1(forest):
    visible = np.full(forest.shape, False)
    visible[:, [0, -1]] = True  # Sides are always visible
    visible[[0, -1], :] = True  # Top and bottom are always visible

    for rot in range(4):
        check_visibility_from_left(np.rot90(forest, rot), np.rot90(visible, rot))
    return np.count_nonzero(visible)


def answer2(forest):
    scenic_scores = np.ones_like(forest[INNER, INNER])
    for rot in range(4):
        scenic_scores *= np.rot90(score_view_to_the_right(np.rot90(forest, rot)), -rot)
    return scenic_scores.max()


def main():
    forest = load()
    print(f'Answer 1: {answer1(forest)}')
    print(f'Answer 2: {answer2(forest)}')


def load():
    with open('input/aoc8', encoding='utf-8') as file_:
        return np.array([list(map(int, line.rstrip())) for line in file_.readlines()])


def test_answer1():
    assert answer1(load()) == 1825


def test_answer2():
    assert answer2(load()) == 235200


main()
