
n = int(input())

english_subscribers = set(map(int, input().split()))

m = int(input())
french_subscribers = set(map(int, input().split()))
all_subscribers = english_subscribers.union(french_subscribers)
print(len(all_subscribers))
