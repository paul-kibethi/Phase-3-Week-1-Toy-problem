from collections import defaultdict

def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    max_sum = -1
    digit_sums = defaultdict(list)

    for num in A:
        sum_digits = digit_sum(num)
        digit_sums[sum_digits].append(num)

    for key in digit_sums:
        if len(digit_sums[key]) >= 2:
            max_sum = max(max_sum, sum(sorted(digit_sums[key])[-2:]))

    return max_sum

print(solution([51, 71, 17, 42]))



