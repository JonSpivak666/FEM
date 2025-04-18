def get_material_properties(pde_type):
    """
    Devuelve un diccionario con las propiedades del material dependiendo del PDE.
    """
    if pde_type == "Poisson":
        return {
            "k": 1.0  # coeficiente de difusión isotrópica
        }

    elif pde_type == "Elasticidad":
        return {
            "E": 200e9,     # Módulo de Young [Pa]
            "nu": 0.3       # Coeficiente de Poisson
        }

    elif pde_type == "Calor estacionario":
        return {
            "k": 10.0       # Conductividad térmica [W/mK]
        }

    elif pde_type == "Calor transitorio":
        return {
            "k": 10.0,
            "rho": 7800.0,  # Densidad [kg/m³]
            "cp": 500.0     # Calor específico [J/kg·K]
        }

    else:
        return {}
