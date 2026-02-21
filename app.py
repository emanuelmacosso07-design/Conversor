import streamlit as st

# Configuração da página
st.set_page_config(page_title="Super Conversor S21", page_icon="🚀")

st.title("🌡️ Conversor de Temperatura")
celsius = st.number_input("Digite o valor em Celsius (°C):", value=0.0)

if st.button("Converter para Fahrenheit"):
    f = (celsius * 1.8) + 32
    st.success(f"{celsius}°C é igual a {f:.2f}°F")

st.divider() # Linha para separar os conversores

st.title("💰 Conversor de Moedas")
st.write("Converta valores usando uma cotação fixa")

# Exemplo: Dólar para sua moeda local (ajuste a cotação se quiser)
cotacao_dolar = 5.50 
valor_dolar = st.number_input("Valor em Dólares ($):", min_value=0.0)

if st.button("Converter para Moeda Local"):
    resultado = valor_dolar * cotacao_dolar
    st.warning(f"${valor_dolar:.2f} equivalem a {resultado:.2f} na cotação de {cotacao_dolar}")

st.divider()
st.caption("Criado por um desenvolvedor Python no S21 🚀")
