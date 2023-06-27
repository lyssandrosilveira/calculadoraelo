import streamlit as st

def calculate_probability(ELO_mandante, ELO_visitante):
    if ELO_mandante == 0 and ELO_visitante == 0:
        return 0.5
    elif ELO_mandante == 0:
        return 0.0
    elif ELO_visitante == 0:
        return 1.0
    else:
        p = (ELO_mandante / 400) / ((ELO_mandante / 400) + (ELO_visitante / 400))
        return p

def main():
    st.title("Cálculo da Probabilidade de Vitória")
    st.write("Este aplicativo calcula a probabilidade de vitória de um time com base em seus ratings ELO.")

    # Input ELO_mandante and ELO_visitante values
    ELO_mandante = st.number_input("Informe o rating ELO do time da casa: ", min_value=0)
    ELO_visitante = st.number_input("Informe o rating ELO do time visitante: ", min_value=0)

    # Calculate the probability of victory
    probability = calculate_probability(ELO_mandante, ELO_visitante)

    st.write(f"A probabilidade do time da casa vencer é: {probability:.2%}")

if __name__ == '__main__':
    main()


    # Exibe o crédito do desenvolvedor
    st.write("Desenvolvido por Lyssandro Silveira")

if __name__ == '__main__':
    main()
