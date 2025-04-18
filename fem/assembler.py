import numpy as np
from fem.problem_definitions import get_rhs_function
from fem.materials import get_material_properties

def assemble_poisson_system(grid, pde_type):
    """
    Ensambla el sistema KU = F para la ecuación de Poisson sobre una malla 2D estructurada.
    """
    rhs_function = get_rhs_function(pde_type)
    props = get_material_properties(pde_type)
    k = props.get("k", 1.0)

    # Obtener puntos de la malla
    points = grid.points
    cells = grid.cells_dict.get(9)  # 9 = QUAD, 5 = TRIANGLE (ver VTK)
    if cells is None:
        raise ValueError("Solo se soportan celdas cuadriláteras por ahora.")

    n_points = points.shape[0]
    K = np.zeros((n_points, n_points))
    F = np.zeros(n_points)

    # Ensamblaje elemental simple (forma simbólica, no integrada por cuadratura)
    for quad in cells:
        node_ids = quad
        coords = points[node_ids]

        centroid = np.mean(coords, axis=0)
        area = compute_area(coords)

        # Matriz elemental (simplificada)
        Ke = (k * area / 4.0) * np.ones((4, 4))
        np.fill_diagonal(Ke, k * area)

        # Vector de carga elemental
        f_val = rhs_function(*centroid)
        Fe = np.full(4, f_val * area / 4.0)

        for i in range(4):
            F[node_ids[i]] += Fe[i]
            for j in range(4):
                K[node_ids[i], node_ids[j]] += Ke[i, j]

    return K, F

def compute_area(coords):
    """
    Calcula el área de un cuadrilátero plano en 2D.
    """
    x0, y0 = coords[0][:2]
    x1, y1 = coords[1][:2]
    x2, y2 = coords[2][:2]
    x3, y3 = coords[3][:2]
    return 0.5 * abs((x0*y1 + x1*y2 + x2*y3 + x3*y0) - (y0*x1 + y1*x2 + y2*x3 + y3*x0))
