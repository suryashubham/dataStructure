from math import ceil
def calculate_days():
    D1, V1, D2, V2, P = map(int, input().split())
    if D1 == D2:
        extra = D1 - 1
        total = extra + ceil(P / (V1 + V2))
        print(total)
    else:
        extra = D1 - 1 if D1 < D2 else D2 - 1
        d_s_p = (D2 - D1) * V1 if D1 < D2 else (D1 - D2) * V2
        days_for_single_prod = abs(D1 - D2)
        total = ceil((P - d_s_p) / (V1 + V2)) + extra + days_for_single_prod
        print(total)
