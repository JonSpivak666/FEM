def get_rhs_function(pde_type):
    """
    Retorna la función f(x, y, z) del lado derecho de la ecuación para el tipo de PDE.
    """
    if pde_type == "Poisson":
        # -Δu = 1 → f = 1
        return lambda x, y, z: 1.0
    elif pde_type == "Elasticidad":
        return lambda x, y, z: 0.0  # Placeholder
    elif pde_type == "Calor estacionario":
        return lambda x, y, z: 100.0  # Fuente constante
    elif pde_type == "Calor transitorio":
        return lambda x, y, z: 0.0  # Se aplicará en función del tiempo
    else:
        return lambda x, y, z: 0.0  # Por defecto

def get_boundary_condition(pde_type):
    """
    Retorna una función booleana para la condición Dirichlet.
    """
    if pde_type == "Poisson":
        return lambda x, y, z: x == 0 or x == 1 or y == 0 or y == 1
    else:
        return lambda x, y, z: False  # sin condiciones por defecto
