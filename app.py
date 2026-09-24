import streamlit as st
import pandas as pd

st.set_page_config(page_title="Painel de Arbitragem - Série A", layout="wide")

st.title("⚽ Painel de Análise de Arbitragem - Série A")
st.markdown("Acompanhamento estatístico de cartões, faltas e perfis de arbitragem.")

# Dados consolidados dos 20 árbitros
dados = [
    {"Árbitro": "Raphael Claus (SP)", "Faltas 1ºT": 12.0, "Faltas 2ºT": 14.4, "Total Faltas": 26.4, "Cartões 1ºT": 1.80, "Cartões 2ºT": 2.87, "Total Cartões": 4.67, "Estilo": "Técnico e disciplinar"},
    {"Árbitro": "Anderson Daronco (RS)", "Faltas 1ºT": 11.2, "Faltas 2ºT": 13.6, "Total Faltas": 24.8, "Cartões 1ºT": 1.53, "Cartões 2ºT": 2.80, "Total Cartões": 4.33, "Estilo": "Impositivo e físico"},
    {"Árbitro": "Wilton Pereira Sampaio (GO)", "Faltas 1ºT": 15.47, "Faltas 2ºT": 18.53, "Total Faltas": 34.0, "Cartões 1ºT": 2.13, "Cartões 2ºT": 3.27, "Total Cartões": 5.40, "Estilo": "Rígido e formal"},
    {"Árbitro": "Bráulio da Silva Machado (SC)", "Faltas 1ºT": 15.0, "Faltas 2ºT": 18.2, "Total Faltas": 33.2, "Cartões 1ºT": 2.40, "Cartões 2ºT": 3.80, "Total Cartões": 6.20, "Estilo": "Distribuidor de cartões"},
    {"Árbitro": "Bruno Arleu de Araújo (RJ)", "Faltas 1ºT": 14.33, "Faltas 2ºT": 17.13, "Total Faltas": 31.47, "Cartões 1ºT": 2.20, "Cartões 2ºT": 3.40, "Total Cartões": 5.60, "Estilo": "Detalhista e interventor"},
    {"Árbitro": "Ramon Abatti Abel (SC)", "Faltas 1ºT": 11.47, "Faltas 2ºT": 13.73, "Total Faltas": 25.2, "Cartões 1ºT": 1.73, "Cartões 2ºT": 2.87, "Total Cartões": 4.60, "Estilo": "Moderno e dinâmico"},
    {"Árbitro": "Flávio Rodrigues de Souza (SP)", "Faltas 1ºT": 13.47, "Faltas 2ºT": 16.33, "Total Faltas": 29.8, "Cartões 1ºT": 2.00, "Cartões 2ºT": 3.20, "Total Cartões": 5.20, "Estilo": "Conservador e previdente"},
    {"Árbitro": "Edina Alves Batista (SP)", "Faltas 1ºT": 13.0, "Faltas 2ºT": 15.6, "Total Faltas": 28.6, "Cartões 1ºT": 1.87, "Cartões 2ºT": 3.13, "Total Cartões": 5.00, "Estilo": "Rígida e física"},
    {"Árbitro": "Paulo César Zanovelli (MG)", "Faltas 1ºT": 14.53, "Faltas 2ºT": 17.47, "Total Faltas": 32.0, "Cartões 1ºT": 2.33, "Cartões 2ºT": 3.60, "Total Cartões": 5.93, "Estilo": "Enérgico e comunicativo"},
    {"Árbitro": "Rodrigo José Pereira (PE)", "Faltas 1ºT": 13.87, "Faltas 2ºT": 16.53, "Total Faltas": 30.4, "Cartões 1ºT": 2.20, "Cartões 2ºT": 3.47, "Total Cartões": 5.67, "Estilo": "Firme e combativo"},
    {"Árbitro": "Matheus Candançan (SP)", "Faltas 1ºT": 11.73, "Faltas 2ºT": 14.07, "Total Faltas": 25.8, "Cartões 1ºT": 1.60, "Cartões 2ºT": 2.73, "Total Cartões": 4.33, "Estilo": "Fluido e participativo"},
    {"Árbitro": "Felipe Fernandes de Lima (MG)", "Faltas 1ºT": 12.53, "Faltas 2ºT": 15.07, "Total Faltas": 27.6, "Cartões 1ºT": 1.87, "Cartões 2ºT": 3.00, "Total Cartões": 4.87, "Estilo": "Técnico e posicional"},
    {"Árbitro": "Alex Stefano (RJ)", "Faltas 1ºT": 11.0, "Faltas 2ºT": 13.4, "Total Faltas": 24.4, "Cartões 1ºT": 1.60, "Cartões 2ºT": 2.60, "Total Cartões": 4.20, "Estilo": "Discreto e direto"},
    {"Árbitro": "Lucas Paulo Torezin (PR)", "Faltas 1ºT": 13.2, "Faltas 2ºT": 16.0, "Total Faltas": 29.2, "Cartões 1ºT": 2.00, "Cartões 2ºT": 3.20, "Total Cartões": 5.20, "Estilo": "Cauteloso e regulamentar"},
    {"Árbitro": "Davi de Oliveira Lacerda (ES)", "Faltas 1ºT": 10.8, "Faltas 2ºT": 13.0, "Total Faltas": 23.8, "Cartões 1ºT": 1.47, "Cartões 2ºT": 2.53, "Total Cartões": 4.00, "Estilo": "Dialógico e calmo"},
    {"Árbitro": "Jonathan Benkenstein (RS)", "Faltas 1ºT": 12.67, "Faltas 2ºT": 15.33, "Total Faltas": 28.0, "Cartões 1ºT": 1.80, "Cartões 2ºT": 2.93, "Total Cartões": 4.73, "Estilo": "Intenso e próximo"},
    {"Árbitro": "Lucas Casagrande (PR)", "Faltas 1ºT": 14.0, "Faltas 2ºT": 16.8, "Total Faltas": 30.8, "Cartões 1ºT": 2.07, "Cartões 2ºT": 3.40, "Total Cartões": 5.47, "Estilo": "Rígido e disciplinar"},
    {"Árbitro": "Savio Pereira Sampaio (DF)", "Faltas 1ºT": 14.0, "Faltas 2ºT": 17.0, "Total Faltas": 31.0, "Cartões 1ºT": 2.00, "Cartões 2ºT": 3.13, "Total Cartões": 5.13, "Estilo": "Formal e cadenciado"},
    {"Árbitro": "Gustavo Ervino Bauermann (SC)", "Faltas 1ºT": 11.33, "Faltas 2ºT": 13.67, "Total Faltas": 25.0, "Cartões 1ºT": 1.60, "Cartões 2ºT": 2.60, "Total Cartões": 4.20, "Estilo": "Dinâmico"},
    {"Árbitro": "Maguielson Lima Barbosa (DF)", "Faltas 1ºT": 12.4, "Faltas 2ºT": 14.8, "Total Faltas": 27.2, "Cartões 1ºT": 1.80, "Cartões 2ºT": 2.80, "Total Cartões": 4.60, "Estilo": "Firme e pedagógico"}
]

df = pd.DataFrame(dados)

# Filtro lateral
st.sidebar.header("Filtros")
arbitro_selecionado = st.sidebar.selectbox("Escolha um Árbitro:", ["Todos"] + list(df["Árbitro"]))

if arbitro_selecionado != "Todos":
    df_exibicao = df[df["Árbitro"] == arbitro_selecionado]
else:
    df_exibicao = df

st.subheader("Métricas de Faltas e Cartões (Médias por Jogo)")
st.dataframe(df_exibicao, use_container_width=True)
