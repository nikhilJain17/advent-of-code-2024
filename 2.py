"""
Part 1:

Given a list of rows, check if each row is:
1. monotonically increasing or decreasing
2. delta of 1 to 3 between each element per row


Part 2:
A row is safe if 
3. you can remove one element and satisfy 1 and 2

So when you spot a problem element, try fetching the next elem
if you can, otherwise if its at the end, remove it and return True.
"""
def is_monotonically_increasing_with_delta(row):
    for i in range(len(row) - 1):
        num, next = row[i], row[i+1]
        if (next - num > 3) or (next - num < 1):
            return False
    return True

def is_monotonically_decreasing_with_delta(row):
    # since we have no negative numbers (?)
    return is_monotonically_increasing_with_delta([-1 * num for num in row])

def is_monotonically_increasing_with_delta_and_removal(row):
    for i in range(len(row) - 2):
        num, next, skip = row[i], row[i+1], row[i+2]
        if (next - num > 3) or (next - num < 1):
            # since (num, next) is causing a problem, try either
            # (num, skip) or (next, skip)
            if not is_monotonically_increasing_with_delta(row[:i+1] + row[i+2:]) and not is_monotonically_increasing_with_delta(row[:i] + row[i+1:]):
                return False
    return True 

def is_monotonically_decreasing_with_delta_and_removal(row):
       # since we have no negative numbers (?)
    return is_monotonically_increasing_with_delta_and_removal([-1 * num for num in row])
 

def main():
    num_safe_rows = 0
    num_safe_rows_with_removal = 0
    with open("./2_input.txt") as f:
        for line in f:
            nums = list(map(int, line.split()))
            if is_monotonically_increasing_with_delta(nums):
                num_safe_rows += 1
                num_safe_rows_with_removal += 1
            elif is_monotonically_decreasing_with_delta(nums):
                num_safe_rows += 1
                num_safe_rows_with_removal += 1
            elif is_monotonically_increasing_with_delta_and_removal(nums):
                num_safe_rows_with_removal += 1
            elif is_monotonically_decreasing_with_delta_and_removal(nums):
                num_safe_rows_with_removal += 1
    print("num safe rows:", num_safe_rows)
    print("num safe rows with up to 1 removal per row:", num_safe_rows_with_removal)

if __name__ == '__main__':
    main()