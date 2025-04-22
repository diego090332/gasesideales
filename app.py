import streamlit as st
st.imagen ("imagen.jpeg")

# Constante del gas ideal
R = 0.0821  # L·atm/(mol·K)

st.title("Calculadora de la Ecuación de los Gases Ideales")

st.markdown("### Ecuación: PV = nRT")

opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

# Variables de entrada
if opcion == "Presión (P)":
    volumen = st.number_input("Volumen (L)", min_value=0.01)
    temperatura = st.number_input("Temperatura (K)", min_value=0.01)
    moles = st.number_input("Número de moles (mol)", min_value=0.0)

    if st.button("Calcular Presión"):
        presion = (moles * R * temperatura) / volumen
        st.success(f"Presión: {presion:.4f} atm")

elif opcion == "Volumen (V)":
    presion = st.number_input("Presión (atm)", min_value=0.01)
    temperatura = st.number_input("Temperatura (K)", min_value=0.01)
    moles = st.number_input("Número de moles (mol)", min_value=0.0)

    if st.button("Calcular Volumen"):
        volumen = (moles * R * temperatura) / presion
        st.success(f"Volumen: {volumen:.4f} L")

elif opcion == "Temperatura (T)":
    presion = st.number_input("Presión (atm)", min_value=0.01)
    volumen = st.number_input("Volumen (L)", min_value=0.01)
    moles = st.number_input("Número de moles (mol)", min_value=0.0)

    if st.button("Calcular Temperatura"):
        temperatura = (presion * volumen) / (moles * R)
        st.success(f"Temperatura: {temperatura:.4f} K")

elif opcion == "Número de moles (n)":
    presion = st.number_input("Presión (atm)", min_value=0.01)
    volumen = st.number_input("Volumen (L)", min_value=0.01)
    temperatura = st.number_input("Temperatura (K)", min_value=0.01)

    if st.button("Calcular número de moles"):
        moles = (presion * volumen) / (R * temperatura)
        st.success(f"Número de moles: {moles:.4f} mol")
