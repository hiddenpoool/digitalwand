# -----------------
# Реализуйте функцию count_inversion, которая принимает на вход последовательность.
# Все единицы должны быть пронумерованы, и порядок очень важен
# Предоставляется последовательность (1, 2, 5, 3, 4, 7, 6), и мы видим здесь 
# три инверсии 5 и 3; 5 и 4; 7 и 6. => count_inversion ((1, 2, 5, 3, 4, 7, 6)) == 3
# Задача состоит в том, чтобы посчитать количество инверсий 
# -----------------



def count_inversion(sequence):
    sequence = list(sequence)
    last_item = len(sequence) - 1
    g = 0
    for i in range(0, last_item):
        for x in range(0, last_item):

            if sequence[x] > sequence[x+1]:
                g += 1
                sequence[x], sequence[x+1] = sequence[x+1], sequence[x]


    return g


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Code's finished")