import pyvista as pv

def generate_mesh(structure_type, mesh_params):
    nx, ny, nz = mesh_params["nx"], mesh_params["ny"], mesh_params["nz"]

    if structure_type == "Dominio cúbico 3D":
        grid = pv.UniformGrid()

        grid.dimensions = (nx + 1, ny + 1, nz + 1)
        grid.spacing = (1 / nx, 1 / ny, 1 / nz)
        grid.origin = (0, 0, 0)

        return grid

    elif structure_type == "Placa cuadrada 2D":
        plane = pv.Plane(i_size=1.0, j_size=1.0, i_resolution=nx, j_resolution=ny)
        return plane

    elif structure_type == "Barra 1D":
        line = pv.Line(pointa=(0, 0, 0), pointb=(1, 0, 0), resolution=nx)
        return line

    else:
        return None
