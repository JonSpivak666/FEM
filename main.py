import streamlit as st
from fem.structure_selector import get_structure_options
from fem.mesh_configurator import get_mesh_options
from fem.mesh_generator import generate_mesh
from fem.assembler import assemble_poisson_system
from fem.boundary_conditions import apply_dirichlet_bc
from fem.solver import solve_system
from fem.visualizer import visualize_mesh, visualize_solution

st.set_page_config(page_title="FEM", layout="wide")
st.title("FEM")
st.subheader("Finite Element Method")

# Sidebar: Configuración general
st.sidebar.header("Configuración de Simulación")

# Selección del tipo de estructura geométrica
structure_type = st.sidebar.selectbox(
    "Tipo de estructura",
    get_structure_options()
)

# Selección del tipo de PDE
pde_type = st.sidebar.selectbox(
    "Ecuación (PDE)",
    ["Poisson", "Elasticidad", "Calor estacionario", "Calor transitorio", "Electromagnetismo (en desarrollo)"]
)

# Selección del tipo de elemento
element_type = st.sidebar.selectbox(
    "Tipo de elemento",
    ["Lineales (Lagrange)", "Cuadráticos", "Alta orden (en desarrollo)"]
)

# Selección del método de discretización
discretization_method = st.sidebar.selectbox(
    "Discretización",
    ["Galerkin estándar", "Galerkin descontinuo", "Mixto (en desarrollo)"]
)

# Selección del solucionador
solver_type = st.sidebar.selectbox(
    "Método de solución",
    ["Directo", "Gradiente conjugado", "Multigrid (en desarrollo)"]
)

# Parámetros de malla
mesh_params = get_mesh_options()

# Botón para correr simulación completa
if st.sidebar.button("Ejecutar Simulación"):

    st.subheader("1. Malla generada")
    mesh = generate_mesh(structure_type, mesh_params)
    visualize_mesh(mesh)

    st.subheader("2. Ensamblaje del sistema")
    K, F = assemble_poisson_system(mesh, pde_type)

    st.subheader("3. Aplicación de condiciones de frontera")
    K_bc, F_bc = apply_dirichlet_bc(K.copy(), F.copy(), mesh, pde_type)

    st.subheader("4. Solución del sistema")
    U = solve_system(K_bc, F_bc, solver_type=solver_type)

    st.subheader("5. Visualización de la solución")
    visualize_solution(mesh, U, title=f"Solución de {pde_type}")

else:
    st.info("Selecciona las opciones y presiona 'Ejecutar Simulación'.")
