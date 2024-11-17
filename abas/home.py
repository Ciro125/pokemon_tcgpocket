import streamlit as st
from datetime import datetime
from funcoes.utilidades import validar_posicoes

def exibir_home(collection, allowed_users):
    st.header("🃏 Registro de Posições")

    identificacao = st.text_input("👤 Identificação (Nome)")

    if identificacao:
        if identificacao in allowed_users:
            st.success(f"✅ Bem-vindo, {identificacao}!")

            # Inputs do usuário
            posicao_inicial_desejada = st.number_input("🔢 Posição Inicial da Carta Desejada (1 a 5)", min_value=1, max_value=5, step=1)
            posicao_final_desejada = st.number_input("🎯 Posição Final da Carta Desejada (1 a 5)", min_value=1, max_value=5, step=1)
            carta_ex = st.checkbox("✨ A carta desejada era EX?")
            lugar_selecionado = st.number_input("📍 Lugar Selecionado", min_value=1, max_value=5, step=1)

            # Captura das posições
            with st.container():
                col1, col2, col3 = st.columns(3)
                posicoes = {
                    "Posicao 1": col1.number_input("📍 Posição 1", min_value=1, max_value=5, step=1),
                    "Posicao 2": col2.number_input("📍 Posição 2", min_value=1, max_value=5, step=1),
                    "Posicao 3": col3.number_input("📍 Posição 3", min_value=1, max_value=5, step=1)
                }

                col4, col5 = st.columns(2)
                posicoes["Posicao 4"] = col4.number_input("📍 Posição 4", min_value=1, max_value=5, step=1)
                posicoes["Posicao 5"] = col5.number_input("📍 Posição 5", min_value=1, max_value=5, step=1)

            # Botão de inserção
            if st.button("📥 Inserir"):
                valido, mensagem = validar_posicoes(posicoes)
                if not valido:
                    st.error(mensagem)
                else:
                    acertou_carta = posicao_final_desejada == lugar_selecionado
                    timestamp_atual = datetime.now().isoformat()

                    dados = {
                        "Posicao inicial da carta desejada": posicao_inicial_desejada,
                        "Posicao final da carta desejada": posicao_final_desejada,
                        "Carta era EX": carta_ex,
                        "Lugar selecionado": lugar_selecionado,
                        "Acertou": acertou_carta,
                        **posicoes,
                        "Identificação": identificacao,
                        "DataHoraRegistro": timestamp_atual
                    }

                    collection.insert_one(dados)
                    st.success("🎉 Dados inseridos com sucesso!")
        else:
            st.error("🚫 Usuário não autorizado!")
    else:
        st.info("ℹ️ Por favor, insira seu nome para continuar.")