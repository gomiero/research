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

# -----------------------------------------------------------------------------
# Experimental Probabilistic Operators - A.G.O. Research Project
# Boot and iteration functions for matrix expansion and probabilistic dynamics.
# -----------------------------------------------------------------------------


def o_boot(a: np.ndarray, res: np.ndarray):
    """
    Bootstraps a 2x2 probability matrix into a 4x4 space.

    This operator embeds matrix `a` into the center of matrix `res` (4x4),
    and computes surrounding values based on multiplicative interactions
    between `a`'s elements. The result is a nonlinear expansion with potential
    fractal-like properties.

    Args:
        a   : Input 2x2 matrix of probabilities.
        res : Output 4x4 matrix to be filled (must be preallocated).
    """
    # Place the 2x2 matrix into the center of the 4x4 result matrix
    res[1:3, 1:3] = a

    # Fill the four corners using cross products
    res[0][0] = a[1][1] * a[0][0]
    res[0][3] = a[0][1] * a[1][0]
    res[3][0] = a[0][1] * a[1][0]
    res[3][3] = a[1][1] * a[0][0]

    # Fill top row (excluding corners)
    res[0][1] = a[0][0] * a[1][0]
    res[0][2] = a[0][1] * a[1][1]

    # Fill left column (excluding corners)
    res[1][0] = a[0][0] * a[0][1]
    res[2][0] = a[1][0] * a[1][1]

    # Fill right column (excluding corners)
    res[1][3] = a[0][0] * a[0][1]
    res[2][3] = a[1][0] * a[1][1]

    # Fill bottom row (excluding corners)
    res[3][1] = a[0][0] * a[1][0]
    res[3][2] = a[0][1] * a[1][1]


def o_reboot_dynamic(mat: np.ndarray, a: np.ndarray):
    print("reboot")
    mat[1:3, 1:3] = a
    print(mat)
    print("_"*9)
    return mat

def o_iter(aop: np.ndarray, op=1) -> np.ndarray:
    """
    Iterative operator for dynamic probabilistic expansion.

    Performs a cross-block matrix multiplication over a 4x4 matrix,
    creating a new 4x4 matrix composed of block interactions.
    The result is normalized so the sum is 1 (stochastic matrix).

    Returns:
        A normalized 4x4 matrix after transformation.
    """

    def r1234(a1: np.ndarray,a2: np.ndarray,a3: np.ndarray,a4: np.ndarray) -> np.ndarray:
        return np.concatenate((
            np.concatenate((
                a1[:],
                a2[:]
            ), axis=1),
            np.concatenate((
                a3[:],
                a4[:]
            ), axis=1)
        ), axis=0)


    def r2341(a1: np.ndarray,a2: np.ndarray,a3: np.ndarray,a4: np.ndarray) -> np.ndarray:
        return np.concatenate((
            np.concatenate((
                a2[:],
                a3[:]
            ), axis=1),
            np.concatenate((
                a4[:],
                a1[:]
            ), axis=1)
        ), axis=0)

    def r3412(a1: np.ndarray,a2: np.ndarray,a3: np.ndarray,a4: np.ndarray) -> np.ndarray:
        return np.concatenate((
            np.concatenate((
                a3[:],
                a4[:]
            ), axis=1),
            np.concatenate((
                a1[:],
                a2[:]
            ), axis=1)
        ), axis=0)


    def r4123(a1: np.ndarray,a2: np.ndarray,a3: np.ndarray,a4: np.ndarray) -> np.ndarray:
        return np.concatenate((
            np.concatenate((
                a4[:],
                a1[:]
            ), axis=1),
            np.concatenate((
                a2[:],
                a3[:]
            ), axis=1)
        ), axis=0)

    a1 = np.matmul(aop[2:4, 2:4], aop[0:2, 0:2])
    a2 = np.matmul(aop[2:4, 0:2], aop[0:2, 2:4])
    a3 = np.matmul(aop[0:2, 2:4], aop[2:4, 0:2])
    a4 = np.matmul(aop[0:2, 0:2], aop[2:4, 2:4])
    # Block multiplication and reconstruction
    match op:
        case 1:
            res = r1234(a1, a2, a3, a4)
        case 2:
            res = r2341(a1, a2, a3, a4)
        case 3:
            res = r3412(a1, a2, a3, a4)
        case 4:
            res = r4123(a1, a2, a3, a4)

    # Normalize to ensure it forms a probability space
    res /= np.sum(res)
    return res

if __name__=="__main__":
    # local tests
    N = 2
#   a = np.random.rand(N, N)
    a = np.array([
        [0.1, 0.2],
        [0.3, 0.4]
    ])
    ax = np.array([
        [0.4, 0.1],
        [0.3, 0.2]
    ])
    ax = np.array([
        [0.3, 0.4],
        [0.2, 0.1]
    ])
    ax = np.array([
        [0.2, 0.3],
        [0.1, 0.4]
    ])
    res = np.zeros((4,4))
    o_boot(a, res)

    print(f"N = {N}")
    print("Matrix A:\n", a)
    print("Matrix res:\n", res)
    
    IT = 20
    cnt = 0
    for _ in range(IT):
        res = o_iter(res, 2)
        print(res)
        if cnt % 5 == 0:
            o_reboot_dynamic(res, a)
        print()
        cnt += 1
