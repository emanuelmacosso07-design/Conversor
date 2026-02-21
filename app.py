import streamlit as st

# 1. Configuração da Página com o novo título solicitado
st.set_page_config(
    page_title="Conversor PRO de moedas e Temperaturas", 
    page_icon="💰",
    layout="centered"
)

# 2. CSS Customizado para Números Amarelos e Rodapé Fixo
st.markdown("""
    <style>
    /* Força cor amarela em inputs, sliders e textos importantes */
    input, .stNumberInput div div input, .stSlider div div, label, .stMarkdown p {
        color: #FFD700 !important;
    }
    .resultado-grande {
        font-size: 28px !important;
        font-weight: bold;
        color: #FFD700;
        margin-top: 10px;
    }
    /* Estilo para o rodapé com seus dados */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: white;
        text-align: left;
        padding: 10px;
        font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🇦🇴 Conversor PRO")
st.write(f"**DESENVOLVEDOR:** EMANUEL MACOSSO")

# --- NAVEGAÇÃO ---
aba = st.tabs(["Moedas 💵", "Temperaturas 🌡️"])

with aba[0]:
    st.subheader("Conversão de Moedas")
    moeda = st.selectbox("Escolha a moeda:", ["Dólar (USD)", "Euro (EUR)"])
    valor = st.number_input("Valor:", min_value=0.0, value=1.0, step=1.0, key="moeda_input")
    
    cotacao = 914.00 if "Dólar" in moeda else 1000.00
    total = valor * cotacao
    
    st.write(f"Cotação Atual: {cotacao} Kz")
    st.markdown(f'<p class="resultado-grande">Total: {total:,.2f} Kz</p>', unsafe_allow_html=True)

with aba[1]:
    st.subheader("Conversão Celsius para Fahrenheit")
    celsius = st.number_input("Graus Celsius (°C):", value=25.0, step=0.5, key="temp_input")
    
    fahrenheit = (celsius * 9/5) + 32
    
    st.markdown(f'<p class="resultado-grande">{celsius}°C = {fahrenheit:.1f}°F</p>', unsafe_allow_html=True)

# 3. Informações de Contato no Canto Inferior
st.markdown(f"""
    <div class="footer">
        Desenvolvedor: Emanuel Macosso<br>
        +244 935227288<br>
        Endereço: Cabinda, Angola, 000
    </div>
    """, unsafe_allow_html=True)
