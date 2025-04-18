import streamlit as st

def get_mesh_options():
    st.sidebar.markdown("### Parámetros de Mallado")

    nx = st.sidebar.slider("Divisiones en X", min_value=1, max_value=100, value=10)
    ny = st.sidebar.slider("Divisiones en Y", min_value=1, max_value=100, value=10)
    nz = st.sidebar.slider("Divisiones en Z", min_value=1, max_value=100, value=10)

    mesh_type = st.sidebar.selectbox("Tipo de malla", ["Hexaedros", "Tetraedros (en desarrollo)"])

    return {
        "nx": nx,
        "ny": ny,
        "nz": nz,
        "type": mesh_type
    }
