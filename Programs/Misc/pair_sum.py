# program to find a pair from a given list such that sum is equal to the given value

arr = [90, 2, -3, 9, 115, -6, 7]
target = -9


def find_pair():
    hash_table = dict()
    for x in range(len(arr)):
        hash_table[arr[x]] = 0
    for y in range(len(arr)):
        hash_table[arr[y]] = 1
        if target - arr[y] in hash_table.keys() and hash_table[target - arr[y]] == 1:
            print(arr[y], target - arr[y])
            break
        elif target - arr[y] in hash_table.keys():
            hash_table[target - arr[y]] = 1


find_pair()
