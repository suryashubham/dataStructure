#!/usr/bin/env python3

import sys


def get_length_of_longest_substring(s):
    w = list()
    c = list()
    if len(s) == 0:
        print("enter a valid string")
        sys.exit(0)
    else:
        i = 0
        j = 0
        while j <= len(s) - 1:
            if s[j] not in w:
                w.append(s[j])
                if j + 1 <= len(s) - 1 and s[j + 1] not in w:
                    j = j + 1
            else:
                c.append(len(w))
                i = i + 1
                j = j + 1
                print(w)
                w = w[i:]
        print(c)
        print(max(c))


s = input("enter a string to get the maximum length of substring :")
get_length_of_longest_substring(s)
