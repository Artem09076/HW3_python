n=float(input())
def mor_tu(n):
    def helper(n):
        # базовый случай
        if n == 0:
            return []

        # рекурсивный случай
        prev_row = helper(n-1)
        curr_row = [1] * (len(prev_row) + 1)
        for j in range(1, len(prev_row)):
            curr_row[j] = prev_row[j-1] + prev_row[j]
        return curr_row

    # получаем последовательность Морса-Туэ
    sequence = helper(n)

    # преобразуем последовательность в строку и возвращаем результат
    return " ".join(str(x) for x in [0] + sequence)

print(mor_tu(n))