m = int(input())  
a = set(map(int, input().split()))

n = int(input())  
b = set(map(int, input().split()))  

sym_diff = a.symmetric_difference(b)
sorted_sym_diff = sorted(sym_diff)

for elem in sorted_sym_diff:
    print(elem)
