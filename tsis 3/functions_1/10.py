def unique_list(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

list = [int(x) for x in input().split()]
print(unique_list(list))
