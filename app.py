import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Conversor PRO - Emanuel Macosso", layout="centered")

# 2. Cabeçalho com seu nome em destaque
st.markdown("<h1 style='text-align: center; color: #FFD700;'>EMANUEL MACOSSO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Conversor de Moedas e Temperatura</p>", unsafe_allow_html=True)
st.divider()

# 3. CONVERSOR DE MOEDAS (Inversível)
st.header("💱 Conversor de Moedas")

# Taxas fixas (Base: 1 Kwanza - AOA)
taxas_para_aoa = {
    "Dólar (USD)": 928.0,
    "Euro (EUR)": 980.0,
    "Real (BRL)": 178.0,
    "Kwanza (AOA)": 1.0
}

col1, col2 = st.columns(2)
with col1:
    moeda_origem = st.selectbox("De:", list(taxas_para_aoa.keys()), index=3) # Começa no AOA
    valor_input = st.number_input("Valor:", min_value=0.0, value=1000.0)
with col2:
    moeda_destino = st.selectbox("Para:", list(taxas_para_aoa.keys()), index=0) # Começa no USD

# Lógica de conversão cruzada
# Converte a origem para Kwanza e depois para o destino
valor_em_aoa = valor_input * taxas_para_aoa[moeda_origem] if moeda_origem != "Kwanza (AOA)" else valor_input
resultado_moeda = valor_em_aoa / taxas_para_aoa[moeda_destino]

st.success(f"**Resultado:** {resultado_moeda:,.2f} {moeda_destino.split()[-1][1:4]}")

st.divider()

# 4. CONVERSOR DE TEMPERATURA (Inversível)
st.header("🌡️ Conversor de Temperatura")

c1, c2 = st.columns(2)
with c1:
    temp_v = st.number_input("Graus:", value=0.0, key="t_val")
    de_temp = st.selectbox("De:", ["Celsius", "Fahrenheit", "Kelvin"], index=0)
with c2:
    para_temp = st.selectbox("Para:", ["Celsius", "Fahrenheit", "Kelvin"], index=1)

def converter_tudo(v, de, para):
    if de == para: return v
    # Converte qualquer entrada para Celsius
    if de == "Fahrenheit": c = (v - 32) * 5/9
    elif de == "Kelvin": c = v - 273.15
    else: c = v
    
    # Converte de Celsius para o destino
    if para == "Fahrenheit": return (c * 9/5) + 32
    if para == "Kelvin": return c + 273.15
    return c

res_t = converter_tudo(temp_v, de_temp, para_temp)
st.metric("Resultado", f"{res_t:.2f} °{para_temp}")

# 5. Rodapé
st.divider()
st.caption("Desenvolvido por Emanuel Macosso | Cabinda, Angola")
