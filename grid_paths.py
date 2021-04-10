def calculate_total_no_of_paths_in_grid(m, n):
    if m == 1 or n == 1:
        return 1
    return calculate_total_no_of_paths_in_grid(m - 1, n) + calculate_total_no_of_paths_in_grid(m, n - 1)

print(calculate_total_no_of_paths_in_grid(10, 10))
