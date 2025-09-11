import streamlit as st
import random as rd
from lists import randomChapter

st.set_page_config(page_title="L48LdP")
st.title("Las 48 Leyes del Poder")
st.write(
    "Oprime el botón para seleccionar aleatoriamiente una de las leyes para repasar el día de hoy.")

if st.button("Generar", type="primary"):
    num, titulo = randomChapter(rd.randint(0, 9))
    
    # Número de la ley (azul y grande)
    st.markdown(
        f"<h2 style='text-align: center; color: royalblue;'>Ley {num}</h2>",
        unsafe_allow_html=True
    )
    
    # Título de la ley (debajo, centrado)
    st.markdown(
        f"<p style='text-align: center; font-size:18px;'>{titulo}</p>",
        unsafe_allow_html=True
    )