import streamlit as st
from pymongo import MongoClient
from datetime import datetime

# Acessando os segredos corretamente
db_username = st.secrets["database"]["DB_USERNAME"]
db_token = st.secrets["database"]["DB_TOKEN"]
allowed_users = st.secrets["users"]["ALLOWED_USERS"]

# Conectar ao MongoDB com as credenciais
uri = f"mongodb+srv://{db_username}:{db_token}@cluster0.sowongv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["pockemon"]
collection = db["pockemontcg"]

# Função para validar as posições
def validar_posicoes(posicoes):
    if len(set(posicoes.values())) != len(posicoes.values()):
        return False, "As posições não podem se repetir."
    if not all(1 <= pos <= 5 for pos in posicoes.values()):
        return False, "Todas as posições devem ser números entre 1 e 5."
    return True, ""

# Cabeçalho do app
st.title("🃏 Pockemon Estampas Ilustradas Pocket - Registro de Posições")

# Input para identificação do usuário
identificacao = st.text_input("👤 Identificação (Nome)")

if identificacao:
    if identificacao in allowed_users:
        st.success(f"✅ Bem-vindo, {identificacao}!")

        # Input da posição desejada inicialmente e final
        posicao_inicial_desejada = st.number_input("🔢 Posição Inicial da Carta Desejada (1 a 5)", min_value=1, max_value=5, step=1)
        posicao_final_desejada = st.number_input("🎯 Posição Final da Carta Desejada (1 a 5)", min_value=1, max_value=5, step=1)

        # Checkbox para indicar se a carta desejada era EX
        carta_ex = st.checkbox("✨ A carta desejada era EX?")

        # Campo para o lugar selecionado pelo usuário
        lugar_selecionado = st.number_input("📍 Lugar Selecionado", min_value=1, max_value=5, step=1)

        # Dividir as posições em linhas usando colunas com emojis
        with st.container():
            col1, col2, col3 = st.columns(3)
            posicoes = {
                "Posição 1": col1.number_input("📍 Posição 1", min_value=1, max_value=5, step=1),
                "Posição 2": col2.number_input("📍 Posição 2", min_value=1, max_value=5, step=1),
                "Posição 3": col3.number_input("📍 Posição 3", min_value=1, max_value=5, step=1)
            }

            col4, col5 = st.columns(2)
            posicoes["Posição 4"] = col4.number_input("📍 Posição 4", min_value=1, max_value=5, step=1)
            posicoes["Posição 5"] = col5.number_input("📍 Posição 5", min_value=1, max_value=5, step=1)

        # Botão para inserir dados com emoji
        if st.button("📥 Inserir"):
            # Validar posições usando a função
            valido, mensagem = validar_posicoes(posicoes)
            if not valido:
                st.error(mensagem)
            else:
                # Simplificando a lógica para calcular "Acertou"
                acertou_carta = posicao_final_desejada == lugar_selecionado

                # Adiciona o timestamp atual
                timestamp_atual = datetime.now().isoformat()

                dados = {
                    "Posicao inicial da carta desejada": posicao_inicial_desejada,
                    "Posicao final da carta desejada": posicao_final_desejada,
                    "Carta era EX": carta_ex,
                    "Lugar selecionado": lugar_selecionado,
                    "Acertou": acertou_carta,
                    "Posicao 1": posicoes["Posição 1"],
                    "Posicao 2": posicoes["Posição 2"],
                    "Posicao 3": posicoes["Posição 3"],
                    "Posicao 4": posicoes["Posição 4"],
                    "Posicao 5": posicoes["Posição 5"],
                    "Identificação": identificacao,
                    "DataHoraRegistro": timestamp_atual
                }

                # Inserir dados no MongoDB
                collection.insert_one(dados)
                st.success("🎉 Dados inseridos com sucesso!")

                # Exibir resultado após a lógica
                if acertou_carta:
                    st.success("🎯 Você acertou a posição da carta!")
                else:
                    st.warning("❌ Você errou a posição da carta.")
    else:
        st.error("🚫 Usuário não autorizado!")
else:
    st.info("ℹ️ Por favor, insira seu nome para continuar.")