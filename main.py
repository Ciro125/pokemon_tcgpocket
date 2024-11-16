import streamlit as st
from funcoes.conexao import conectar_mongodb
from abas.home import exibir_home
from abas.analises import exibir_analises

# Acessando os segredos corretamente
db_username = st.secrets["database"]["DB_USERNAME"]
db_token = st.secrets["database"]["DB_TOKEN"]
allowed_users = st.secrets["users"]["ALLOWED_USERS"]

db = conectar_mongodb(db_username, db_token)
collection = db["pockemontcg"]

# Cabeçalho do app
st.title("🃏 Pockemon Estampas Ilustradas Pocket - Registro de Posições")

# Criar abas
tab1, tab2 = st.tabs(["🃏 Registro", "📊 Analises"])

# Exibir conteúdo da aba
with tab1:
    exibir_home(collection, allowed_users)

# Exibir conteúdo da aba
with tab2:
    exibir_analises(collection)