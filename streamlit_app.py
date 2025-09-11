import streamlit as st
import random as rd
from lists import randomChapter

st.title("Las 48 Leyes del Poder")
st.write(
    "Oprime el botón para seleccionar aleatoriamiente una de las leyes para repasar el día de hoy.")

if st.button("Generar", type="primary"):
    num = rd.randint(0, 9)  # de 0 a 47 (48 leyes)
    st.write(randomChapter(num))