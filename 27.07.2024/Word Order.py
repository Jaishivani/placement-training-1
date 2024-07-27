n = int(input())
word_count = {}
order = []

for _ in range(n):
    word = input().strip()  
    if word in word_count:
        word_count[word] += 1 
    else:
        word_count[word] = 1 
        order.append(word)  
print(len(order))

print(" ".join(str(word_count[word]) for word in order))
