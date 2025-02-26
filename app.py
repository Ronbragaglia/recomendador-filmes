import streamlit as st
import sqlite3
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

# Especificar a função de perda ao carregar o modelo
custom_objects = {"mse": tf.keras.losses.MeanSquaredError()}

# Carregar o modelo treinado corretamente
model = keras.models.load_model("modelo_recomendacao.h5", custom_objects=custom_objects)

# Conectar ao banco SQLite
conn = sqlite3.connect("movies.db")

# Carregar os dados das avaliações
df = pd.read_sql("SELECT user_id, movie_id, rating FROM ratings", conn)

# Criar encoders para os IDs dos usuários e filmes
user_encoder = LabelEncoder()
movie_encoder = LabelEncoder()

df['user_id'] = user_encoder.fit_transform(df['user_id'])
df['movie_id'] = movie_encoder.fit_transform(df['movie_id'])

# Criar a interface no Streamlit
st.title("🎬 Sistema de Recomendação de Filmes com IA 🤖")

# Campo para digitar o ID do usuário
user_id_input = st.number_input("Digite seu ID de usuário:", min_value=1, step=1)

def recomendar_filmes_nn(user_id, n=5):
    """ Recomenda filmes para um usuário usando a Rede Neural, retornando títulos em vez de IDs """
    user_idx = user_encoder.transform([user_id])[0]

    # Selecionar filmes que o usuário ainda não avaliou
    filmes_disponiveis = df['movie_id'].unique()
    filmes_nao_vistos = [movie for movie in filmes_disponiveis if not (df[(df['user_id'] == user_id) & (df['movie_id'] == movie)].any().any())]

    # Fazer previsões para os filmes não vistos
    user_input = np.full(len(filmes_nao_vistos), user_idx)
    preds = model.predict([user_input, np.array(filmes_nao_vistos)]).flatten()

    # Selecionar os melhores filmes
    indices = np.argsort(preds)[-n:][::-1]
    filmes_recomendados = [filmes_nao_vistos[i] for i in indices]

    # Buscar os títulos dos filmes recomendados no banco
    filmes_titulos = [pd.read_sql(f"SELECT title FROM movies WHERE id={movie}", conn).iloc[0, 0] for movie in filmes_recomendados]

    return filmes_titulos

# Botão para gerar recomendações
if st.button("🔍 Obter Recomendações"):
    if user_id_input:
        recomendacoes = recomendar_filmes_nn(user_id_input)
        st.subheader("🎥 Filmes Recomendados para Você:")
        for filme in recomendacoes:
            st.write(f"✔ {filme}")
    else:
        st.warning("⚠ Por favor, digite um ID válido.")

# Fechar conexão com o banco de dados
conn.close()

