import streamlit as st
import math

st.title("Menghitung :blue[volume tabung] :rocket:")

r = st.number_input("Masukan Jari-Jari (cm): ",0)
r = st.number_input("Masukan Tinggi (cm): ",0)

if st.button("Menghitung Volume", typr="primary"):
  v = math.pi*(r**2)*t
  st.success(f'Volume tabung adalah {v:.2f}')
