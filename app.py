import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Conversor PRO - Emanuel Macosso", layout="centered")

# 2. Cabeçalho com seu nome em destaque
st.markdown("<h1 style='text-align: center; color: #FFD700;'>EMANUEL MACOSSO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Conversor de Moedas e Temperatura</p>", unsafe_allow_html=True)
st.divider()

# 3. CONVERSOR DE MOEDAS (Valores Fixos - Fevereiro 2026)
st.header("💱 Conversor de Moedas")

# Definição das taxas fixas (Base: 1 Kwanza - AOA)
# Valores aproximados baseados no câmbio de 22/02/2026
taxas_fixas = {
    "Dólar (USD)": 0.00108,   # 1 USD ≈ 928 Kz
    "Euro (EUR)": 0.00102,    # 1 EUR ≈ 980 Kz
    "Real (BRL)": 0.00560,    # 1 BRL ≈ 178 Kz
    "Rand (ZAR)": 0.02100     # 1 ZAR ≈ 47 Kz
}

col1, col2 = st.columns(2)
with col1:
    valor_aoa = st.number_input("Valor em Kwanza (AOA):", min_value=0.0, value=1000.0)
with col2:
    moeda_selecionada = st.selectbox("Converter para:", list(taxas_fixas.keys()))

# Cálculo simples sem internet
taxa = taxas_fixas[moeda_selecionada]
resultado_moeda = valor_aoa * taxa

st.success(f"**Resultado:** {resultado_moeda:,.2f} {moeda_selecionada.split()[-1][1:4]}")
st.info(f"Câmbio fixado em: 1 AOA = {taxa:.6f} {moeda_selecionada.split()[-1][1:4]}")

st.divider()

# 4. CONVERSOR DE TEMPERATURA
st.header("🌡️ Conversor de Temperatura")

c1, c2 = st.columns(2)
with c1:
    valor_t = st.number_input("Graus:", value=0.0)
    de_u = st.selectbox("De:", ["Celsius", "Fahrenheit", "Kelvin"])
with c2:
    para_u = st.selectbox("Para:", ["Celsius", "Fahrenheit", "Kelvin"])

def calcular_temp(v, de, para):
    if de == para: return v
    # Converte para Celsius
    c = v if de == "Celsius" else (v - 32) * 5/9 if de == "Fahrenheit" else v - 273.15
    # Converte para o destino
    if para == "Celsius": return c
    if para == "Fahrenheit": return (c * 9/5) + 32
    return c + 273.15

res_t = calcular_temp(valor_t, de_u, para_u)
st.metric("Resultado", f"{res_t:.2f} °{para_u}")

# 5. Rodapé
st.divider()
st.caption("Desenvolvido por Emanuel Macosso | Cabinda, Angola")
