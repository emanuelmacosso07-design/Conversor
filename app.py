import streamlit as st
import requests

# 1. Configuração da Página
st.set_page_config(page_title="Kwanza Pro - EMANUEL MACOSSO", page_icon="🇦🇴")

# 2. Estilo Visual (Cores Azul e Amarela)
st.markdown("""
    <style>
    .stApp {
        background-color: #003366; /* Fundo Azul Marinho */
    }
    h1, h2, h3, p, span, label {
        color: #FFCC00 !important; /* Texto em Amarelo Ouro */
    }
    .stButton>button {
        background-color: #FFCC00;
        color: #003366;
        border-radius: 10px;
        font-weight: bold;
    }
    .stNumberInput input {
        color: #003366 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- IDENTIFICAÇÃO DO DONO ---
col_nome, col_vazio = st.columns([2, 1])
with col_nome:
    st.write(f"👤 **DESENVOLVEDOR: EMANUEL MACOSSO**")

# --- FUNÇÃO DE CÂMBIO ---
def buscar_cambio():
    url = "https://open.er-api.com"
    try:
        response = requests.get(url)
        dados = response.json()
        return {"USD": 1 / dados['rates']['USD'], "EUR": 1 / dados['rates']['EUR']}
    except:
        return {"USD": 914.0, "EUR": 980.0}

cambio = buscar_cambio()

# --- TÍTULO COM BANDEIRA ---
st.title("🇦🇴 Conversor de Moedas Pro")
st.write("---")

# --- SEÇÃO DE CONVERSÃO ---
moeda = st.selectbox(
    "Escolha a moeda que deseja converter:",
    ["🇺🇸 Dólar (USD)", "🇪🇺 Euro (EUR)"]
)

sigla = "USD" if "Dólar" in moeda else "EUR"
bandeira = "🇺🇸" if sigla == "USD" else "🇪🇺"

valor = st.number_input(f"Valor em {moeda}:", min_value=0.0, value=1.0)

# Cálculos
cotacao = cambio[sigla]
total_kwanza = valor * cotacao

# Exibição do Resultado
st.metric(label=f"Cotação Atual {bandeira}", value=f"{cotacao:.2f} Kz")
st.header(f"Total: {total_kwanza:,.2f} Kz")

st.write("---")
if st.button("🔄 ATUALIZAR CÂMBIO AGORA"):
    st.rerun()

st.caption("© 2024 | Criado por Emanuel Macosso no Samsung S21 🚀")
