import streamlit as st
import requests

st.title("🇦🇴 Conversor PRO")
st.subheader("Desenvolvedor: Emanuel Macosso")

# 1. Função para buscar cotações em tempo real
def buscar_cotacoes():
    url = "https://open.er-api.com" # Base fixa em Kwanza (AOA)
    response = requests.get(url)
    data = response.json()
    return data['rates']

try:
    rates = buscar_cotacoes()
    # Pega todas as siglas de moedas disponíveis na API (USD, EUR, BRL, etc)
    lista_moedas = list(rates.keys())

    # 2. Interface do Usuário
    moeda_destino = st.selectbox("Escolha a moeda para converter de Kwanza (AOA):", lista_moedas)
    valor_kz = st.number_input("Valor em Kwanza (Kz):", min_value=0.0, value=1.0)

    # 3. Cálculo
    taxa = rates[moeda_destino]
    total = valor_kz * taxa

    st.write(f"**Cotação Atual:** 1 Kz = {taxa:.4f} {moeda_destino}")
    st.success(f"**Total:** {total:.2e} {moeda_destino}")

except Exception as e:
    st.error("Erro ao carregar cotações. Verifique sua conexão.")

st.info("As cotações são atualizadas automaticamente via API.")
