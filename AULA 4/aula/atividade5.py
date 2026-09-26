import streamlit as st

st.title("📊 Análise Simples de Sentimento")
st.write("Digite o comentário do cliente para analisar a polaridade baseada em palavras-chave.")

# Listas de palavras-chave
palavras_positivas = ["excelente", "ótimo", "bom", "adorei", "gostei", "recomendo", "maravilhoso", "top", "perfeito", "rápido"]
palavras_negativas = ["pÉssimo", "ruim", "horrível", "demorado", "detestei", "odeiei", "defeito", "problema", "não recomendo", "lixo"]

# Caixa de texto de entrada
comentario = st.text_area("Comentário do cliente:", placeholder="Ex: O produto é excelente e a entrega foi muito rápida!")

if st.button("Analisar Sentimento", type="primary"):
    if comentario.strip() == "":
        st.warning("Por favor, digite um comentário.")
    else:
        comentario_lc = comentario.lower()
        
        # Contagem de palavras encontradas
        score_positivo = sum(1 for palavra in palavras_positivas if palavra in comentario_lc)
        score_negativo = sum(1 for palavra in palavras_negativas if palavra in comentario_lc)
        
        # Lógica condicional para determinação de sentimento
        if score_positivo > score_negativo:
            st.success(f"😊 **Sentimento: POSITIVO** (Pontos positivos: {score_positivo} | Negativos: {score_negativo})")
        elif score_negativo > score_positivo:
            st.error(f"😡 **Sentimento: NEGATIVO** (Pontos positivos: {score_positivo} | Negativos: {score_negativo})")
        else:
            st.info(f"😐 **Sentimento: NEUTRO** (Pontos positivos: {score_positivo} | Negativos: {score_negativo})")