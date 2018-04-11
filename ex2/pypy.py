# -----------------
# Реализуйте функцию even_last, которая принимает на вход список
# задан массив целых чисел. Вы должны найти сумму элементов с четными индексами
# (0-й, 2-й, 4-й ...), а затем умножить это суммированное число на конечный элемент массива.
# Не забывайте, что первый элемент имеет индекс 0.
# Для пустого массива результат всегда будет 0 (ноль).
# -----------------


def even_last(array):
    sum = 0
    if len(array) > 0:
        numbers = array[::2]
        for obj in numbers:
            sum = sum + obj
        sum = sum * array[-1]
        print(sum)

    return sum


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert even_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_last([6]) == 36, "(6)*6=36"
    assert even_last([]) == 0, "An empty array = 0"

    print("YES!!!")