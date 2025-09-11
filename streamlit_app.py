import streamlit as st
import random as rd
from lists import randomChapter

st.set_page_config(page_title="L48LdP", layout="centered")

# Título centrado con parte en azul
st.markdown(
    "<h1 style='text-align: center;'>Las <span style='color: royalblue;'>48</span> Leyes del Poder</h1>",
    unsafe_allow_html=True
)

# Subtítulo centrado
st.markdown(
    "<p style='text-align: center;'>Oprime el botón para seleccionar aleatoriamente una de las leyes para repasar el día de hoy.</p>",
    unsafe_allow_html=True
)
with st.container(horizontal_alignment="center"):

    # Botón y resultado
    if st.button("Generar", type="primary"):
        num, titulo = randomChapter(rd.randint(0, 47))

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