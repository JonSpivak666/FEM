import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve, cg

def solve_system(K, F, solver_type="Directo"):
    """
    Resuelve el sistema KU = F utilizando el método seleccionado.
    """
    if solver_type == "Directo":
        U = np.linalg.solve(K, F)

    elif solver_type == "Gradiente conjugado":
        K_sparse = csr_matrix(K)
        U, info = cg(K_sparse, F)
        if info != 0:
            raise RuntimeError("Gradiente conjugado no convergió.")

    else:
        raise NotImplementedError(f"Método de solución no soportado: {solver_type}")

    return U
