from collections import deque
n = int(input())
d = deque()

for _ in range(n):
    operation = input().strip().split()
    command = operation[0]
    
    if command == 'append':
        d.append(int(operation[1]))
    elif command == 'appendleft':
        d.appendleft(int(operation[1]))
    elif command == 'pop':
        d.pop()
    elif command == 'popleft':
        d.popleft()
print(" ".join(map(str, d)))
