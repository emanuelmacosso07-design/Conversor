import streamlit as st
import requests

st.set_page_config(page_title="Conversor Kwanza Pro", page_icon="🇦🇴")

# --- FUNÇÃO PARA BUSCAR CÂMBIO EM TEMPO REAL ---
def buscar_cambio():
    url = "https://open.er-api.com" # Base no Kwanza
    try:
        response = requests.get(url)
        dados = response.json()
        # Pegamos o inverso (1 / valor) para saber quanto 1 USD ou EUR vale em AOA
        taxas = {
            "USD": 1 / dados['rates']['USD'],
            "EUR": 1 / dados['rates']['EUR']
        }
        return taxas
    except:
        return {"USD": 914.0, "EUR": 980.0} # Valores de reserva caso a internet falhe

cambio = buscar_cambio()

st.title("🇦🇴 Conversor de Moedas (AOA)")
st.write("Câmbio atualizado em tempo real via API")

# 1. Escolha da Moeda
moeda_origem = st.selectbox("Selecione a moeda que você tem:", ["Dólar (USD)", "Euro (EUR)"])

# 2. Entrada do Valor
sigla = "USD" if "Dólar" in moeda_origem else "EUR"
simbolo = "$" if sigla == "USD" else "€"
valor_estrangeiro = st.number_input(f"Digite o valor em {moeda_origem}:", min_value=0.0, value=1.0)

# 3. Cálculo
cotacao = cambio[sigla]
valor_kwanza = valor_estrangeiro * cotacao

# 4. Resultado
st.metric(label=f"Cotação 1 {sigla}", value=f"{cotacao:.2f} Kz")
st.success(f"{simbolo}{valor_estrangeiro:.2f} equivalem a **{valor_kwanza:,.2f} Kz**")

st.divider()
if st.button("🔄 Atualizar Câmbio"):
    st.rerun()

st.caption("Criado por um desenvolvedor Python no S21 🚀")
