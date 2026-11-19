import math
import numpy as np
import matplotlib.pyplot as plt

# =========== Задача 3
#
# """
# Режим 1: F(A=..., U=...) — дискретное дополнение.
#     A — словарь {элемент: mu}
#     U — список/множество всех элементов
#     Возвращает словарь {элемент: 1 - mu} для всех элементов U.
#
# Режим 2: F(R=True, m=...) — непрерывное дополнение.
#     m — функция принадлежности m(x)
#     Возвращает новую функцию m_bar(x) = 1 - m(x).
# """
#
# def F(A = None, U = None, R = None, m = None):
#     # непрерывный
#     if R is not None and m is not None:
#         def m_bar(x):
#             return 1 - m(x)
#         return m_bar
#
#     # дискретный
#     if A is not None and U is not None:
#         # элементы, которых нет в A, считаем с mu = 0
#         result = {}
#         for x in U:
#             mu = A.get(x, 0.0)
#             result[x] = 1 - mu
#         return result
#
#     raise ValueError("Нужно передать либо (A, U), либо (R, m)")
#
# # # Дискретное дополнение:
# # U = ["Аня", "Антон", "Анастасия", "Аркадий", "Александр"]
# # A = {
# #     "Аня":   0.95,
# #     "Антон": 0.60,
# #     "Анастасия":  0.40,
# #     "Аркадий":  0.80,
# #     "Александр":  0.20,
# # }
# #
# # A_bar = F(A, U)
# # print("Дискретное дополнение:")
# # for x in U:
# #     print(f"{x}: muA: {A.get(x, 0):.2f} ; {A_bar[x]:.2f}")
#
#
# # # непрерывное дополнение:
# # Стандартная треугольная функция принадлежности
# def m_triangle(x):
#     """Треугольная ФП с вершиной в 0.5, носителем (0, 1)."""
#     x = np.asarray(x, dtype=float)
#     y = np.zeros_like(x)
#     left  = (x > 0.0) & (x <= 0.5)
#     right = (x > 0.5) & (x < 1.0)
#     y[left]  = 2 * x[left]
#     y[right] = 2 * (1 - x[right])
#     return y
#
# m_bar = F(R = True, m=m_triangle)   # дополнение: 1 - m(x)
# x = np.linspace(-0.2, 1.2, 500)
# y  = m_triangle(x)
# yb = m_bar(x)
#
# plt.figure(figsize=(8, 4.5))
# plt.plot(x, y,  label="A:  m(x)  (треугольная ФП)", linewidth=2)
# plt.plot(x, yb, label="Ā:  1 − m(x)  (дополнение)", linewidth=2, linestyle="--")
# plt.axhline(0, color="gray", linewidth=0.6)
# plt.axhline(1, color="gray", linewidth=0.6)
# plt.title("Нечёткое множество и его классическое дополнение")
# plt.xlabel("x")
# plt.ylabel("степень принадлежности μ")
# plt.legend()
# plt.grid(alpha=0.3)
# plt.tight_layout()
# plt.show()

