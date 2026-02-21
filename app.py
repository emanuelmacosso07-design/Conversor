import streamlit as st
import requests

# Configuração da página (deve ser a primeira linha de código)
st.set_page_config(page_title="Conversor Multi-Ferramentas", layout="centered")

# --- BARRA LATERAL (MENU) ---
with st.sidebar:
    st.title("⚙️ Navegação")
    # Menu para trocar de "página"
    opcao = st.radio("Selecione:", ["Página Inicial", "💱 Moedas Mundiais", "🌡️ Temperatura"])
    
    st.divider()
    st.markdown("### 👨‍💻 Desenvolvedor")
    st.write("**Emanuel Macosso**")
    st.info("App focado em conversões precisas e rápidas.")

# --- LÓGICA DAS PÁGINAS ---

if opcao == "Página Inicial":
    # Centraliza a imagem e o seu nome
    st.image("https://ibnd.com.br", use_container_width=True)
    st.markdown("<h1 style='text-align: center;'>EMANUEL MACOSSO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Bem-vindo ao seu portal de conversão personalizado.</p>", unsafe_allow_html=True)

elif opcao == "💱 Moedas Mundiais":
    st.header("💱 Câmbio em Tempo Real")
    
    # Busca dados da API
    try:
        # Usando a API gratuita para pegar todas as moedas
        url = "https://open.er-api.com" 
        data = requests.get(url).json()
        rates = data['rates']
        lista_moedas = list(rates.keys())

        col1, col2 = st.columns(2)
        with col1:
            valor_entrada = st.number_input("Quanto converter (Kwanza):", min_value=0.0, value=1000.0)
        with col2:
            moeda_alvo = st.selectbox("Converter para:", lista_moedas, index=lista_moedas.index("USD") if "USD" in lista_moedas else 0)

        resultado = valor_entrada * rates[moeda_alvo]
        st.success(f"**Resultado:** {resultado:,.2f} {moeda_alvo}")
        st.caption(f"Cotação: 1 AOA = {rates[moeda_alvo]:.6f} {moeda_alvo}")
        
    except:
        st.error("Erro ao conectar com o banco de dados mundial. Tente mais tarde.")

elif opcao == "🌡️ Temperatura":
    st.header("🌡️ Conversor de Temperatura")
    
    col1, col2 = st.columns(2)
    with col1:
        temp = st.number_input("Temperatura:", value=0.0)
        tipo = st.selectbox("De:", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        alvo = st.selectbox("Para:", ["Celsius", "Fahrenheit", "Kelvin"])

    # Lógica de cálculo simplificada
    def converter_temp(v, de, para):
        if de == para: return v
        # Converte tudo para Celsius primeiro
        c = v if de == "Celsius" else (v - 32) * 5/9 if de == "Fahrenheit" else v - 273.15
        # Converte de Celsius para o alvo
        return c if para == "Celsius" else (c * 9/5) + 32 if para == "Fahrenheit" else c + 273.15

    res_temp = converter_temp(temp, tipo, alvo)
    st.metric("Resultado", f"{res_temp:.2f} °{alvo[0]}")
