import math
import numpy as np
import matplotlib.pyplot as plt


# =========== Задача 1

# def F(A, a):
#     if not (0 < a < 1):
#         raise ValueError("Параметр a должен быть в интервале (0, 1)")
#
#     return {label for label, mu in A.items() if mu >= a}
#
# temperature = {
#     "Ледяная": 0.2,
#     "Морозная": 0.4,
#     "Холодная": 0.6,
#     "Прохладная": 0.8,
#     "Комфортная": 1,
#     "Теплая": 0.8,
#     "Жаркая": 0.6,
#     "Знойная": 0.4,
#     "Палящая": 0.2
# }
#
# for a in [0.2, 0.4, 0.6, 0.8]:
#     print(f"альфа срез(mu = {a}): {F(temperature, a)}")
