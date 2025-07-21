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

def ortho_operator(a: np.ndarray, b: np.ndarray, c: np.ndarray):
    """
    Generalized NxN version of the custom matrix operator.

    Given three NxN matrices:
    - a and b are multiplied using standard matrix multiplication
    - c is used to apply orthogonal weighting
        - res1: c acts row-wise (element [i,j] affected by c[i,j])
        - res2: c acts column-wise (element [i,j] affected by c[j,i])

    Returns:
        res: 2Nx2N matrix composed from res1 and res2 in an orthogonal layout
        res1: row-weighted result
        res2: column-weighted result
    """
    matmul_result = np.matmul(a, b)
    res1 = matmul_result * c
    res2 = matmul_result * c.T
    res1_t = np.concatenate((res1, res2.T), axis=1)
    res2_t = np.concatenate((res1.T, res2), axis=1)
    res = np.concatenate((res1_t, res2_t))
    return res, res1, res2
