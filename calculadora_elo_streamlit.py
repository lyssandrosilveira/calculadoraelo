import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

$ streamlit run calculadora_elo_streamlit.py

import streamlit as st

def calculate_probability(ELO_mandante, ELO_visitante):
    p = (ELO_mandante / 400) / ((ELO_mandante / 400) + (ELO_visitante / 400))
    return p

def run_app():
    st.title("Cálculo da Probabilidade de Vitória")
    ELO_mandante = st.number_input("ELO do time mandante:")
    ELO_visitante = st.number_input("ELO do time visitante:")

    if st.button("Calcular"):
        probability = calculate_probability(ELO_mandante, ELO_visitante)
        st.write(f"A probabilidade do time mandante vencer é: {probability:.2%}")

    # Adicionar link de atalho
    st.markdown("Clique [aqui](http://clubelo.com/) para acessar o Club Elo.")

    # Adicionar texto de desenvolvimento
    st.write("Desenvolvido por Lyssandro Silveira")

def main():
    run_app()

if __name__ == '__main__':
    main()
