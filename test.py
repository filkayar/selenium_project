def sort(A):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                A[j], A[i] = A[i], A[j]
    return A
