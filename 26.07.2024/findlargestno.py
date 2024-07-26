def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

numbers = [10, 20, 4, 45, 99]
print(second_largest(numbers))
