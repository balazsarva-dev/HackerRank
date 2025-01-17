import numpy as np

N, M = map(int, input().split())

result = []
for _ in range(N):
    values = []
    while len(values) != M:
        values.extend(map(int, input().split()))
    result.append(values)
    
result = np.array(result)

print(np.transpose(result))
print(result.flatten())