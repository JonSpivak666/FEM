import numpy as np
from fem.problem_definitions import get_boundary_condition

def apply_dirichlet_bc(K, F, grid, pde_type):
    """
    Aplica condiciones de frontera tipo Dirichlet (u = 0) al sistema KU = F.
    """
    bc_func = get_boundary_condition(pde_type)
    points = grid.points
    n_points = points.shape[0]

    for i in range(n_points):
        x, y, z = points[i]
        if bc_func(x, y, z):
            K[i, :] = 0.0
            K[:, i] = 0.0
            K[i, i] = 1.0
            F[i] = 0.0

    return K, F
