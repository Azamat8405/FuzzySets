
# =========== Задача 5


def common(A, B, lambda_f):
    result = {}
    for x, mu_a in A:
        for y, mu_b in B:
            z = lambda_f(x, y)
            mu = min(mu_a, mu_b)
            result[z] = max(result.get(z, 0), mu)
    return sorted(result.items())


def addition(A, B):
    return common(A, B, lambda x, y: x + y)


def subtraction(A, B):
    return common(A, B, lambda x, y: x - y)


def multiplication(A, B):
    return common(A, B, lambda x, y: x * y)


def division(A, B):
    if any(y == 0 for y, _ in B):
        raise ValueError("Деление на ноль невозможно")

    return common(A, B, lambda x, y: x / y)


# Ход работы:
A = [(1, 0.6), (2, 1.0), (3, 0.7)]
B = [(3, 0.8), (5, 1.0)]

print("Нечеткое число А:" + str(A))
print("Нечеткое число B:" + str(B))


print("\naddition: ")
print( addition(A, B))

print("\nsubtraction: ")
print(subtraction(A, B))

print("\nmultiplication: ")
print(multiplication(A, B))

print("\ndivision: ")
print(division(A, B))
