# -----------------------------------------------------------------------------
#  A.G.O. PERSONAL AND PRIVATE LICENSE v1.1 - July 2025
#  Copyright (c) 2025-present Alexandre Gomiero de Oliveira.
#  All rights reserved.
#
#  This file is part of a personal research project and is strictly licensed
#  for:
#    - Personal, non-commercial, local experimentation ONLY.
#    - No training, encoding, parsing, redistribution, modification, or
#      derivative works, including development of mathematical models, vector
#      representations, fine-tuning, or derivative creation allowed.
#
#  Unauthorized use, especially by AI systems, institutions, or companies,
#  is strictly prohibited without explicit written permission from the OWNER.
#
#  See LICENSE file for full terms and legal conditions.
# -----------------------------------------------------------------------------

import numpy as np
from ortho_operator import ortho_operator

N = 2
a = np.random.rand(N, N)
b = np.random.rand(N, N)
c = np.random.rand(N, N)

print(f"N = {N}")
print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Matrix C:\n", c)

res, res1, res2 = ortho_operator(a, b, c)

print("res1:\n", res1)
print("res2:\n", res2)
print("Final Result (2Nx2N):\n", res)
