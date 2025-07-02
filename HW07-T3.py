#!/usr/bin/env python3
import argparse

# -------- Task 3: Sum of all values in a BST --------
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


def sum_bst(root):
    """
    Returns the sum of all keys in a binary search tree.
    """
    if root is None:
        return 0
    return root.key + sum_bst(root.left) + sum_bst(root.right)


def generate_readme(total_sum, readme_path='README_Task3.md'):
    lines = [
        '# Завдання 3: Сума всіх значень у BST',
        '',
        '## Результат',
        f'- Сума всіх значень у бінарному дереві пошуку: **{total_sum}**',
        '',
        '## Опис алгоритму',
        'Рекурсивно обходимо дерево (DFS), сумуючи ключ у кожній вершині та ' +
        'суми піддерев.',
        '',
        '## Складність',
        '- Часова: O(n), де n — кількість вузлів (відвідуємо кожен вузол один раз).',
        '- Просторова: O(h) для стеку рекурсії, де h — висота дерева.',
        '',
        '## Висновок',
        'Простий рекурсивний обхід є ефективним для підрахунку суми значень у дереві.'
    ]
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"README for Task3 generated: {readme_path}")


def main():
    parser = argparse.ArgumentParser(description='Task 3: Sum values in BST')
    parser.add_argument(
        '--values', default='15,6,3,7,20,17,25',
        help='Comma-separated integer values to insert into the BST'
    )
    parser.add_argument(
        '--readme', default='README_Task3.md',
        help='File path for the generated README'
    )
    args = parser.parse_args()

    # Build BST from provided values
    values = list(map(int, args.values.split(',')))
    root = BSTNode(values[0])
    for v in values[1:]:
        root.insert(v)

    # Compute sum of all values
    total = sum_bst(root)
    print(f"Sum of all values in BST: {total}")

    # Generate README
    generate_readme(total, args.readme)

if __name__ == '__main__':
    main()
