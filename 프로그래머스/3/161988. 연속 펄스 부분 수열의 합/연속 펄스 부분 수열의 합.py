def solution(sequence):
    cur1 = cur2 = 0
    ans1 = ans2 = 0

    for i, v in enumerate(sequence):
        a = v if i%2 else -v
        b = -a

        cur1 = max(a, cur1 + a)
        cur2 = max(b, cur2 + b)

        ans1 = max(ans1, cur1)
        ans2 = max(ans2, cur2)

    return max(ans1, ans2)

# def solution(sequence):
#     A = []
#     B = []
#     n = len(sequence)
#     for i, v in enumerate(sequence):
#         if i % 2:
#             A.append(-v)
#             B.append(v)
#         else:
#             A.append(v)
#             B.append(-v)

#     for i in range(1, n):
#         A[i] = max(A[i], A[i-1]+A[i])
#         B[i] = max(B[i], B[i-1]+B[i])

#     return max(max(A), max(B))
    