"""
Кейс-задача: Найти сумму отрицательных элементов,
расположенных между максимальным и минимальным элементами массива.
"""

def find_sum_between_extremes(arr):
    """
    Находит сумму отрицательных элементов между максимумом и минимумом.
    
    Аргументы:
        arr: список чисел
    
    Возвращает:
        кортеж (сумма, индекс_макс, индекс_мин, список_отрицательных)
    """
    if not arr:
        return 0, None, None, []
    
    # Находим индексы максимального и минимального элементов
    # (берём первое вхождение)
    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))
    
    # Определяем левую и правую границы диапазона
    left = min(max_index, min_index)
    right = max(max_index, min_index)
    
    # Собираем отрицательные элементы между границами
    negative_elements = []
    for i in range(left + 1, right):
        if arr[i] < 0:
            negative_elements.append(arr[i])
    
    # Вычисляем сумму
    total = sum(negative_elements)
    
    return total, max_index, min_index, negative_elements


def main():
    """Основная функция для взаимодействия с пользователем."""
    print("=" * 60)
    print("ПРОГРАММА ДЛЯ ПОИСКА СУММЫ ОТРИЦАТЕЛЬНЫХ ЭЛЕМЕНТОВ")
    print("между максимальным и минимальным элементами массива")
    print("=" * 60)
    
    # Выбор способа ввода данных
    print("\nВыберите способ ввода данных:")
    print("1 - Ввод с клавиатуры")
    print("2 - Автоматическая генерация случайных чисел")
    
    choice = input("Ваш выбор (1 или 2): ").strip()
    
    arr = []
    
    if choice == "1":
        # Ручной ввод
        try:
            n = int(input("Введите размер массива N: "))
            if n <= 0:
                print("Размер массива должен быть положительным!")
                return
            
            print("Введите элементы массива (через пробел):")
            elements = list(map(int, input().split()))
            
            if len(elements) != n:
                print(f"Ошибка: ожидалось {n} элементов, получено {len(elements)}")
                return
            
            arr = elements
            
        except ValueError:
            print("Ошибка: введите корректные целые числа!")
            return
    
    elif choice == "2":
        # Генерация случайных чисел
        import random
        n = int(input("Введите размер массива N: "))
        if n <= 0:
            print("Размер массива должен быть положительным!")
            return
        
        # Генерируем числа от -20 до 20
        arr = [random.randint(-20, 20) for _ in range(n)]
        print(f"\nСгенерированный массив: {arr}")
    
    else:
        print("Неверный выбор!")
        return
    
    # Выполнение основной логики
    total, max_idx, min_idx, negatives = find_sum_between_extremes(arr)
    
    # Вывод результатов
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 60)
    print(f"Исходный массив: {arr}")
    print(f"Максимальный элемент: {arr[max_idx]} (индекс {max_idx})")
    print(f"Минимальный элемент: {arr[min_idx]} (индекс {min_idx})")
    
    left = min(max_idx, min_idx)
    right = max(max_idx, min_idx)
    
    if right - left <= 1:
        print("Между максимумом и минимумом нет элементов!")
    else:
        between = arr[left + 1:right]
        print(f"Элементы между ними: {between}")
        
        if negatives:
            print(f"Отрицательные элементы между ними: {negatives}")
            print(f"Их сумма: {total}")
        else:
            print("Отрицательных элементов между ними нет!")
            print(f"Сумма = {total}")
    
    print("=" * 60)


if __name__ == "__main__":
    main()