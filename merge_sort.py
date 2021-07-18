import sys


def merge_sort(int_arr):
    if len(int_arr) == 1:
        return int_arr
    if len(int_arr) > 1:
        mid = len(int_arr) // 2
        LH = merge_sort(int_arr[:mid])
        RH = merge_sort(int_arr[mid:])
        return merge(LH, RH)


def merge(LH, RH):
    output = [0]*(len(LH)+len(RH))
    i = j = 0
    LH.append(sys.maxsize)
    RH.append(sys.maxsize)
    for k in range(len(output)):
        if LH[i] < RH[j]:
            output[k]=LH[i]
            i+=1
        else:
            output[k]=RH[j]
            j += 1
    return output


int_arr = [9, 3, 1, 0, 6, 2, 5]
print(merge_sort(int_arr))

