import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Conversor PRO", layout="centered")

# --- BARRA LATERAL (ONDE FICAM SUAS INFORMAÇÕES) ---
with st.sidebar:
    st.title("Menu")
    # Aqui selecionamos a "Banda" ou Página
    opcao = st.radio("Selecione uma ferramenta:", ["Página Inicial", "Conversor de Moedas", "Conversor de Temperatura"])
    
    st.divider()
    st.markdown("### Desenvolvedor")
    st.write("**Emanuel Macosso**")
    st.write("📍 Cabinda, Angola")
    st.write("📞 +244 935227288")

# --- LÓGICA DAS PÁGINAS ---

if opcao == "Página Inicial":
    st.title("Bem-vindo ao Conversor PRO 🇦🇴")
    # Aqui você coloca a imagem de fundo que conversamos antes
    # A imagem aparecerá apenas nesta tela inicial
    st.image("sua_imagem_de_fundo.jpg", caption="Sua ferramenta de conversão completa")

elif opcao == "Conversor de Moedas":
    st.header("💱 Conversão de Moedas")
    # Coloque aqui o código de moedas que te mandei antes
    st.write("Taxas atualizadas em tempo real...")

elif opcao == "Conversor de Temperatura":
    st.header("🌡️ Conversor de Temperaturas")
    # Aqui você coloca a lógica de Celsius para Fahrenheit, etc.
    valor = st.number_input("Graus:", value=0.0)
    # Exemplo simples:
    st.write(f"{valor}°C é igual a {(valor * 9/5) + 32}°F")
