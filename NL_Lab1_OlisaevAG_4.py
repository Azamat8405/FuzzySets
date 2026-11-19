import math
import numpy as np
import matplotlib.pyplot as plt

# =========== Задача 4

# ДИСКРЕТНЫЙ СЛУЧАЙ
def F_disc(A, B, operation):
    """
    A, B — словари {элемент: μ}, μ ∈ [0, 1]
    operation — 'union', 'intersection', 'difference', 'symdiff'
    Отсутствующий элемент считаем с μ = 0.
    """
    keys = set(A) | set(B) #
    result = {}

    for x in keys:
        a = A.get(x, 0.0)
        b = B.get(x, 0.0)

        if operation == 'union':            # A ∪ B («ИЛИ». насколько элемент принадлежит хотя бы одному из множеств)
            result[x] = max(a, b)           # для объединения берем максимальное из двух принадлежностей
        elif operation == 'intersection':   # A ∩ B («И». одновременно принадлежит и множеству A, и множеству B)
            result[x] = min(a, b)           # для объединения берем минимальное из двух принадлежностей
        elif operation == 'difference':     # A \ B (Насколько каждый элемент всё ещё остаётся в A, если мы “вычтем” из него B)
            result[x] = min(a, 1 - b)
        elif operation == 'symdiff':        # A ∆ B  (либо в A, либо в B, но не в обоих сразу)
            result[x] = max(min(a, 1 - b), min(1 - a, b))
        else:
            raise ValueError(f"Неизвестная операция: {operation}")

    return result


# =====================================================
# НЕПРЕРЫВНЫЙ СЛУЧАЙ
# =====================================================
def F_cont(mA, mB, op):
    """
    mA, mB — функции принадлежности m(x)
    Возвращает новую функцию, реализующую операцию.
    """
    if op == 'union':
        return lambda x: np.maximum(mA(x), mB(x))
    if op == 'intersection':
        return lambda x: np.minimum(mA(x), mB(x))
    if op == 'difference':                # A \ B
        return lambda x: np.minimum(mA(x), 1 - mB(x))
    if op == 'symdiff':                   # A ∆ B
        return lambda x: np.maximum(
            np.minimum(mA(x), 1 - mB(x)),
            np.minimum(1 - mA(x), mB(x))
        )
    raise ValueError(f"Неизвестная операция: {op}")


# # дискретный случай
# # =====================================================
# A = {"Аня": 0.9, "Борис": 0.6, "Вера": 0.3, "Глеб": 0.8}
# B = {"Аня": 0.4, "Борис": 0.7, "Вера": 0.9, "Дина": 0.5}
#
# print("Дискретные операции:")
# for op, name in [('union', 'A ∪ B'), ('intersection', 'A ∩ B'),
#                  ('difference', 'A \\ B'), ('symdiff', 'A ∆ B')]:
#     print(f"\n{name}:")
#     for x, mu in sorted(F_disc(A, B, op).items()):
#         print(f"  {x}: {mu:.2f}")



# непрерывный случай
# =====================================================

# Две треугольные функции принадлежности
def tri(x, a, b, c):
    """Треугольная ФП: 0 при x<=a, 1 в b, 0 при x>=c."""
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    left  = (x > a) & (x <= b)
    right = (x > b) & (x < c)
    y[left]  = (x[left] - a) / (b - a)
    y[right] = (c - x[right]) / (c - b)
    return y

mA = lambda x: tri(x, 0.0, 0.4, 0.8)   # треугольник с вершиной в 0.4
mB = lambda x: tri(x, 0.3, 0.7, 1.0)   # треугольник с вершиной в 0.7

x = np.linspace(-0.2, 1.2, 800)

fig, axes = plt.subplots(2, 2, figsize=(11, 8))
ops = [('union', 'A ∪ B  (max)'),
       ('intersection', 'A ∩ B  (min)'),
       ('difference', 'A \\ B  (min(μA, 1−μB))'),
       ('symdiff', 'A ∆ B  (симметрическая разность)')]

for ax, (op, title) in zip(axes.flat, ops):
    f = F_cont(mA, mB, op)
    ax.plot(x, mA(x), '--', color='tab:blue',  label='A:  μA(x)')
    ax.plot(x, mB(x), '--', color='tab:orange', label='B:  μB(x)')
    ax.plot(x, f(x),  '-',  color='tab:green', linewidth=2.5, label=title)
    ax.set_title(title)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

plt.tight_layout()
plt.show()