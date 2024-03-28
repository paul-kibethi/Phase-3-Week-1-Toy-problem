def solution(A):
    total_moves = 0
    for i in range(len(A)):
        diff = A[i] - 10
        if diff > 0:
            A[i] -= diff
            if i + 1 < len(A):
                A[i + 1] += diff
            total_moves += diff
    if all(box == 10 for box in A):
        return total_moves
    else:
        return -1

    print(solution([7, 15, 10, 8]))

