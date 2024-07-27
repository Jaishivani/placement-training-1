t = int(input())

for _ in range(t):
    a_size = int(input())
    A = set(map(int, input().split()))
    
    b_size = int(input())
    B = set(map(int, input().split()))
    
    print(A.issubset(B))
