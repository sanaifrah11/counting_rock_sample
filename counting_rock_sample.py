
S, R = map(int, input().split())

samples = list(map(int, input().split()))

for i in range(R):
    low, high = map(int, input().split())

    count = 0
    for size in samples:
        if low <= size <= high:
            count += 1

    print(count)
