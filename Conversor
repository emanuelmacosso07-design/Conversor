import streamlit as st

# Configuração da página do site
st.set_page_config(page_title="Conversor Pro", page_icon="🌡️")

st.title("🌡️ Conversor de Temperatura")
st.write("Transforme Celsius em Fahrenheit instantaneamente!")

# Caixa de entrada numérica estilizada
celsius = st.number_input("Digite o valor em Celsius (°C):", format="%.2f")

# Botão com cor e ação
if st.button("Converter para Fahrenheit"):
    fahrenheit = (celsius * 1.8) + 32
    # Exibe o resultado num balão verde bonito
    st.success(f"O resultado é: {fahrenheit:.2f} °F")
    st.balloons() # Efeito visual de festa ao converter!

st.divider()
st.caption("Criado por um desenvolvedor Python no S21 🚀")
