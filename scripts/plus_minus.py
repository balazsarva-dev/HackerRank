def plusMinus(arr: list) -> list:
    positives, negatives, zeros = [n for n in arr if n > 0], [n for n in arr if n < 0], [n for n in arr if n == 0]
    f = lambda x: len(x) / len(arr)
    return [f(positives), f(negatives), f(zeros)]

if __name__ == '__main__':
    while True:
        n = int(input())
        if n in range(1, 101):
            break
    while True:
        arr = list(map(int, input().split()))
        if len(arr) == n and all(x in range(-100, 101) for x in arr):
            break
    res = plusMinus(arr)
    for num in res: print(f'{num:.6f}')