# Сумма отрицательных элементов между максимумом и минимумом

## Суть задачи
Найти сумму отрицательных элементов массива, которые находятся **строго между** максимальным и минимальным элементами.

## Решение

### Алгоритм
1. Найти индексы максимума и минимума.
2. Определить левую и правую границы: `left = min(max_idx, min_idx)`, `right = max(max_idx, min_idx)`.
3. Пройти по элементам между ними и сложить только отрицательные.
4. Вывести сумму.

### Код (основная функция)

```python
def find_sum_between_extremes(arr):
    if not arr:
        return 0, None, None, []

    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))

    left = min(max_index, min_index)
    right = max(max_index, min_index)

    negative_elements = []
    for i in range(left + 1, right):
        if arr[i] < 0:
            negative_elements.append(arr[i])

    total = sum(negative_elements)
    return total, max_index, min_index, negative_elements
```


