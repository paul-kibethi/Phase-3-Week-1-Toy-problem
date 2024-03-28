def solution(N):
    if N <= 26:
        return ''.join(chr(ord('a') + i) for i in range(N))
    else:
        repeat = N // 26
        remainder = N % 26
        return ''.join(chr(ord('a') + i) * repeat for i in range(26)) + ''.join(chr(ord('a') + i) for i in range(remainder))

print(solution(3))
