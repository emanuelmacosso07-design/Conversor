import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Conversor PRO - Emanuel Macosso", layout="centered")

# --- CABEÇALHO ---
st.markdown("<h1 style='text-align: center; color: #FFD700;'>EMANUEL MACOSSO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Tudo o que você precisa converter em um só lugar.</p>", unsafe_allow_html=True)
st.divider()

# --- SEÇÃO 1: MOEDAS MUNDIAIS ---
st.header("💱 Conversor de Moedas")

def buscar_cambio():
    try:
        # API alternativa e estável
        url = "https://open.er-api.com"
        response = requests.get(url, timeout=15)
        return response.json()
    except:
        return None

dados = buscar_cambio()

if dados:
    rates = dados['rates']
    lista_moedas = sorted(list(rates.keys()))
    
    col1, col2 = st.columns(2)
    with col1:
        valor_kz = st.number_input("Valor em Kwanza (AOA):", min_value=0.0, value=1000.0)
    with col2:
        # Tenta colocar o Dólar (USD) como padrão se existir na lista
        padrao = lista_moedas.index("USD") if "USD" in lista_moedas else 0
        moeda_alvo = st.selectbox("Converter para:", lista_moedas, index=padrao)
    
    resultado = valor_kz * rates[moeda_alvo]
    st.success(f"**Resultado:** {resultado:,.2f} {moeda_alvo}")
    st.caption(f"Câmbio atualizado em: {dados['time_last_update_utc'][:16]}")
else:
    st.error("⚠️ Não foi possível carregar o câmbio. Verifique se o arquivo requirements.txt tem a palavra 'requests'.")

st.divider()

# --- SEÇÃO 2: TEMPERATURA ---
st.header("🌡️ Conversor de Temperatura")

c1, c2 = st.columns(2)
with c1:
    valor_t = st.number_input("Graus:", value=0.0)
    unidade_de = st.selectbox("De:", ["Celsius", "Fahrenheit", "Kelvin"])
with c2:
    unidade_para = st.selectbox("Para:", ["Celsius", "Fahrenheit", "Kelvin"])

def converter_t(v, de, para):
    if de == para: return v
    # Converte para Celsius
    c = v if de == "Celsius" else (v - 32) * 5/9 if de == "Fahrenheit" else v - 273.15
    # Converte para o destino
    if para == "Celsius": return c
    if para == "Fahrenheit": return (c * 9/5) + 32
    return c + 273.15

res_t = converter_t(valor_t, unidade_de, unidade_para)
st.info(f"**Resultado:** {res_t:.2f} °{unidade_para}")

# --- RODAPÉ ---
st.divider()
st.caption("© 2024 Desenvolvido por Emanuel Macosso")
