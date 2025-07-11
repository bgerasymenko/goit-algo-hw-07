# Завдання 2: Знаходження мінімального значення у BST

## Результат
- Найменше значення у бінарному дереві пошуку: **3**

## Опис алгоритму
Для пошуку найменшого значення у BST проходимо по лівим нащадкам, доки не досягнемо вершини без лівого нащадка.

## Складність
- Часова: O(h), де h — висота дерева (у середньому O(log n)).
- Просторова: O(h) для стеку рекурсії.

## Висновок
Алгоритм ефективно знаходить мінімальний елемент у BST та працює за час пропорційний висоті дерева.