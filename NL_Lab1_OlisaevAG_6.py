
# =========== Задача 6

def f_composition(A, B):
    """
    Композиция двух нечётких бинарных отношений A (N×M) и B (M×K).
    Возвращает матрицу C (N×K).
    """
    N = len(A)
    M = len(A[0]) if N else 0
    M2 = len(B)
    K = len(B[0]) if M2 else 0

    if M != M2:
        raise ValueError(f"Размерности не согласованы: A — {N}×{M}, B — {M2}×{K}")

    C = [[0.0] * K for _ in range(N)]

    for i in range(N):
        for k in range(K):
            C[i][k] = max(min(A[i][j], B[j][k]) for j in range(M))

    return C


A = [[0.2, 0.6, 0.0], [1.0, 0.7, 0.3]]
B = [[0.3, 0.8], [0.7, 0.1], [0.5, 0.5]]

print("Нечеткое бинарное отношение А:" + str(A))
print("Нечеткое бинарное отношение B:" + str(B))

print('\nКомпозицию 𝐴°𝐵 (𝑁𝑥𝐾):')
print(f_composition(A, B))
