# largest difference between two number in a given list such that the larger number should occur after the smaller no.

arr = [12, 1, 3, 4, 1, 2, 111, -5, 0]


def find_max_sum_sub_array():
    diff_list = create_difference_list()
    max_sum = arr[0]
    for index in range(1, len(diff_list)):
        if diff_list[index - 1] > 0:
            diff_list[index] = diff_list[index] + diff_list[index - 1]
            if diff_list[index] > max_sum:
                max_sum = diff_list[index]
        elif diff_list[index] > max_sum:
            max_sum = diff_list[index]
    print("maximum difference between the no. in list such that larger no. occurs after samller no is:", max_sum)


def create_difference_list():
    temp_list = list()
    for index in range(1, len(arr)):
        temp_list.append(arr[index] - arr[index - 1])
    return temp_list


find_max_sum_sub_array()
