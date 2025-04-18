import streamlit as st
import pyvista as pv

def visualize_mesh(mesh):
    """
    Visualiza solo la malla sin solución.
    """
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh, show_edges=True, color='white')
    plotter.set_background("black")
    plotter.camera_position = "xy"
    plotter.show(screenshot="temp_mesh.png")
    st.image("temp_mesh.png", caption="Vista de la malla generada")

def visualize_solution(mesh, U, title="Solución FEM"):
    """
    Visualiza la solución u sobre la malla como un campo escalar.
    """
    if len(U) != mesh.n_points:
        st.error("El tamaño de la solución no coincide con la malla.")
        return

    mesh.point_data["u"] = U  # Asignar la solución a cada nodo

    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh, scalars="u", cmap="viridis", show_edges=True)
    plotter.set_background("white")
    plotter.camera_position = "xy"
    plotter.show(screenshot="temp_solution.png")

    st.image("temp_solution.png", caption=title)
