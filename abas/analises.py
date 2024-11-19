import streamlit as st
import pandas as pd
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer

def exibir_analises(collection):
    """
    Exibe os dados da coleção em um DataFrame no Streamlit, com colunas em ordem personalizada.
    """
    st.header("📊 Análises de Dados")

    # Recuperar todos os documentos da coleção
    dados = list(collection.find())

    if dados:
        # Converter os dados em DataFrame do pandas
        df = pd.DataFrame(dados)

        # Remover a coluna "_id" para exibição
        if "_id" in df.columns:
            df.drop(columns=["_id"], inplace=True)

        # Reorganizar as colunas na ordem desejada
        colunas_ordenadas = [
            "Identificação",
            "Posicao inicial da carta desejada",
            "Posicao final da carta desejada",
            "Carta era EX",
            "Lugar selecionado",
            "Acertou",
            "Posicao 1",
            "Posicao 2",
            "Posicao 3",
            "Posicao 4",
            "Posicao 5",
            "DataHoraRegistro"
        ]

        # Garantir que as colunas estão na ordem e presentes no DataFrame
        df = df[[col for col in colunas_ordenadas if col in df.columns]]

        # Exibir o DataFrame
        st.dataframe(df)

        # Abrir a interface interativa
        pyg_app = StreamlitRenderer(df)
        pyg_app.explorer()

    else:
        st.info("ℹ️ Nenhum dado disponível para análise.")