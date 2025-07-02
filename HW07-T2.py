#!/usr/bin/env python3
import argparse

# -------- Task 2: Find min in a BST (separate script) --------
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


def find_min_in_bst(root):
    """
    Returns the minimum key in a binary search tree.
    """
    current = root
    while current and current.left:
        current = current.left
    return current.key if current else None


def generate_readme(min_value, path='README_Task2.md'):
    lines = [
        '# Завдання 2: Знаходження мінімального значення у BST',
        '',
        '## Результат',
        f'- Найменше значення у бінарному дереві пошуку: **{min_value}**',
        '',
        '## Опис алгоритму',
        'Для пошуку найменшого значення у BST проходимо по лівим нащадкам, ' \
        'доки не досягнемо вершини без лівого нащадка.',
        '',
        '## Складність',
        '- Часова: O(h), де h — висота дерева (у середньому O(log n)).',
        '- Просторова: O(h) для стеку рекурсії.',
        '',
        '## Висновок',
        'Алгоритм ефективно знаходить мінімальний елемент у BST та працює за час пропорційний висоті дерева.'
    ]
    with open(path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"README for Task2 generated: {path}")


def main():
    parser = argparse.ArgumentParser(description='Task 2: Find min in BST')
    parser.add_argument(
        '--values', default='15,6,3,7,20,17,25',
        help='Comma-separated integer values to insert into the BST'
    )
    parser.add_argument(
        '--readme', default='README_Task2.md',
        help='File path for the generated README'
    )
    args = parser.parse_args()

    # Build BST from provided values
    values = list(map(int, args.values.split(',')))
    root = BSTNode(values[0])
    for v in values[1:]:
        root.insert(v)

    # Find minimum value
    min_val = find_min_in_bst(root)
    print(f"Min value in BST: {min_val}")

    # Generate README
    generate_readme(min_val, args.readme)

if __name__ == '__main__':
    main()
