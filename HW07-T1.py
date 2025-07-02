#!/usr/bin/env python3
import argparse

# -------- Task 1: Find max in a BST --------
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = BSTNode(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = BSTNode(key)
            else:
                self.right.insert(key)


def find_max_in_bst(root):
    """
    Returns the maximum key in a binary search tree.
    """
    current = root
    while current and current.right:
        current = current.right
    return current.key if current else None


def generate_readme(max_value, readme_path='README.md'):
    lines = [
        '# Завдання 1: Знаходження максимального значення у BST',
        '',
        '## Результат',
        f'- Найбільше значення у бінарному дереві пошуку: **{max_value}**',
        '',
        '## Опис алгоритму',
        'Для пошуку найбільшого значення у BST проходимо по правим нащадкам, ' \
        'доки не дістанемось вершини без правого нащадка.',
        '',
        '## Складність',
        '- Часова: O(h), де h — висота дерева (у середньому O(log n)).',
        '- Просторова: O(h) для стеку викликів рекурсії.',
        '',
        '## Висновок',
        'Алгоритм ефективний для пошуку максимального елемента у BST, ' \
        'оскільки у збалансованому дереві h набагато менше, ніж n.'
    ]
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"README generated: {readme_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Task 1: Find max in BST'
    )
    parser.add_argument(
        '--values',
        default='15,6,3,7,20,17,25',
        help='Comma-separated list of integer values to insert into the BST'
    )
    parser.add_argument(
        '--readme',
        default='README.md',
        help='Output path for the generated README'
    )
    args = parser.parse_args()

    # Build BST from provided values
    values = list(map(int, args.values.split(',')))
    root = BSTNode(values[0])
    for v in values[1:]:
        root.insert(v)

    # Find maximum value
    max_val = find_max_in_bst(root)
    print(f"Max value in BST: {max_val}")

    # Generate README
    generate_readme(max_val, args.readme)

if __name__ == '__main__':
    main()
