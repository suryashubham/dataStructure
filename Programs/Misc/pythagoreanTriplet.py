
# TC = O(n^2)

def is_triplet(arr, n):
    arr = [i * i for i in arr]
    arr.sort()

    for i in range(n - 1, 1, -1):
        j = 0
        k = i - 1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                return [arr[i], arr[j], arr[k]]
            else:
                if arr[j] + arr[k] < arr[i]:
                    j = j + 1
                else:
                    k = k - 1
    return []


def print_result(result):
    if len(result) > 0:
        print(result)
    else:
        print("no triplets")


array = [13, 1, 41, 6, 5, 12]
arr_size = len(array)
res = is_triplet(array, arr_size)
print_result(res)
pythagoreanTriplet.py
Displaying pythagoreanTriplet.py.
