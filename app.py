import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Conversor PRO - Emanuel Macosso", layout="centered")

# 2. Cabeçalho Centralizado
st.markdown("<h1 style='text-align: center; color: #FFD700;'>EMANUEL MACOSSO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Conversões Instantâneas e Automáticas</p>", unsafe_allow_html=True)
st.divider()

# 3. CONVERSOR DE MOEDAS (Cálculo Instantâneo)
st.header("💱 Conversor de Moedas")

valores_em_aoa = {
    "Kwanza (AOA)": 1.0,
    "Dólar (USD)": 928.0,
    "Euro (EUR)": 980.0,
    "Real (BRL)": 178.0,
    "Rand (ZAR)": 47.0
}

col1, col2 = st.columns(2)
with col1:
    moeda_de = st.selectbox("Converter de:", list(valores_em_aoa.keys()), index=1)
    valor_input = st.number_input("Digite o valor:", min_value=0.0, value=1.0, step=0.01)
with col2:
    moeda_para = st.selectbox("Converter para:", list(valores_em_aoa.keys()), index=0)

resultado_moeda = (valor_input * valores_em_aoa[moeda_de]) / valores_em_aoa[moeda_para]

st.markdown(f"<h3 style='color: #28a745;'>Resultado: {resultado_moeda:,.2f} {moeda_para.split()[-1][1:4]}</h3>", unsafe_allow_html=True)
st.caption(f"Cotação: 1 {moeda_de.split()[-1][1:4]} = {valores_em_aoa[moeda_de]/valores_em_aoa[moeda_para]:,.2f} {moeda_para.split()[-1][1:4]}")

st.divider()

# 4. CONVERSOR DE TEMPERATURA (Cálculo Instantâneo)
st.header("🌡️ Conversor de Temperatura")

c1, c2 = st.columns(2)
with c1:
    temp_val = st.number_input("Graus:", value=0.0, step=0.1)
    de_t = st.selectbox("De:", ["Celsius", "Fahrenheit", "Kelvin"], index=0)
with c2:
    para_t = st.selectbox("Para:", ["Celsius", "Fahrenheit", "Kelvin"], index=1)

def converter_temp(v, de, para):
    if de == para: return v
    c = v if de == "Celsius" else (v - 32) * 5/9 if de == "Fahrenheit" else v - 273.15
    if para == "Celsius": return c
    if para == "Fahrenheit": return (c * 9/5) + 32
    return c + 273.15

res_t = converter_temp(temp_val, de_t, para_t)
st.subheader(f"Resultado: {res_t:.2f} °{para_t}")

# 5. NOVO RODAPÉ COM CONTATOS DIRETOS
st.divider()
st.markdown("<p style='text-align: center; font-weight: bold;'>Para mais informações:</p>", unsafe_allow_html=True)

# Cria colunas para os ícones de contato ficarem lado a lado e centralizados
col_contato1, col_contato2, col_contato3 = st.columns([1, 1, 1])

with col_contato1:
    st.markdown("[![WhatsApp](https://img.icons8.com)](https://wa.me)")
    st.write("WhatsApp")

with col_contato2:
    st.markdown("[![Telefone](https://img.icons8.com)](tel:+244935227288)")
    st.write("+244 935227288")

with col_contato3:
    st.markdown("[![E-mail](https://img.icons8.com)](mailto:emanuelmacosso07@gmail.com)")
    st.write("E-mail")

st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>© 2026 Desenvolvido por Emanuel Macosso | Cabinda, Angola</p>", unsafe_allow_html=True)
