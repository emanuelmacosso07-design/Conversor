import streamlit as st
import requests

# 1. Configuração Inicial
st.set_page_config(page_title="Conversor PRO - Emanuel Macosso", layout="centered")

# 2. Cabeçalho Principal (O nome fica no topo em destaque)
st.markdown("<h1 style='text-align: center; color: #FFD700;'>EMANUEL MACOSSO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Sua ferramenta completa de conversão</p>", unsafe_allow_html=True)
st.divider()

# 3. SEÇÃO: CONVERSOR DE MOEDAS MUNDIAIS
st.header("💱 Conversor de Moedas (Câmbio Real)")

try:
    # Busca dados em tempo real (Base em Kwanza - AOA)
    url = "https://open.er-api.com"
    data = requests.get(url, timeout=10).json()
    rates = data['rates']
    lista_moedas = sorted(list(rates.keys()))

    col1, col2 = st.columns(2)
    with col1:
        valor_kz = st.number_input("Valor em Kwanza (AOA):", min_value=0.0, value=1000.0, key="moeda_val")
    with col2:
        moeda_destino = st.selectbox("Converter para:", lista_moedas, index=lista_moedas.index("USD"))

    resultado_moeda = valor_kz * rates[moeda_destino]
    st.success(f"**Resultado:** {resultado_moeda:,.2f} {moeda_destino}")
    st.caption(f"Última atualização: {data['time_last_update_utc'][:16]}")

except Exception as e:
    st.error("Conecte-se à internet para atualizar as moedas.")

st.divider()

# 4. SEÇÃO: CONVERSOR DE TEMPERATURA
st.header("🌡️ Conversor de Temperatura")

col3, col4 = st.columns(2)
with col3:
    temp_input = st.number_input("Graus:", value=0.0, key="temp_val")
    de_unidade = st.selectbox("De:", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_de")
with col4:
    para_unidade = st.selectbox("Para:", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_para")

# Lógica de cálculo
def converter_temperatura(v, de, para):
    if de == para: return v
    # Converte para Celsius
    c = v if de == "Celsius" else (v - 32) * 5/9 if de == "Fahrenheit" else v - 273.15
    # Converte de Celsius para o destino
    if para == "Celsius": return c
    if para == "Fahrenheit": return (c * 9/5) + 32
    return c + 273.15

res_temp = converter_temperatura(temp_input, de_unidade, para_unidade)
st.info(f"**Resultado:** {res_temp:.2f} °{para_unidade}")

# 5. Rodapé Fixo
st.divider()
st.caption("Desenvolvido por Emanuel Macosso | Cabinda, Angola")
