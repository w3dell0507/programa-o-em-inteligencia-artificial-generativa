import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Garantir o download dos dados de tokenização do NLTK
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

st.title("🛍️ Análise de Avaliações de Produtos")
st.write("Tokenização + Condicionais para identificar a satisfação do cliente.")

# Entrada da avaliação
avaliacao = st.text_area(
    "Digite a avaliação do produto:",
    placeholder="Ex: O produto é bom e bonito, mas o prazo de entrega foi péssimo."
)

# Conjuntos de palavras de interesse para verificação direta
palavras_positivas = {"bom", "excelente", "ótimo", "recomendo", "maravilhoso", "satisfeito", "bonito", "rápido"}
palavras_negativas = {"ruim", "péssimo", "horrível", "defeito", "quebrado", "demorado", "insatisfeito", "lixo"}

if st.button("Analisar Avaliação", type="primary"):
    if not avaliacao.strip():
        st.warning("Por favor, digite uma avaliação para analisar.")
    else:
        # 1. TOKENIZAÇÃO: Divisão do texto em tokens (palavras/pontuações)
        tokens = word_tokenize(avaliacao.lower(), language='portuguese')
        
        # Listas para guardar as palavras encontradas
        pos_encontradas = []
        neg_encontradas = []
        
        # 2. ITERAÇÃO E CONDICIONAIS
        for token in tokens:
            if token in palavras_positivas:
                pos_encontradas.append(token)
            elif token in palavras_negativas:
                neg_encontradas.append(token)
        
        qtd_pos = len(pos_encontradas)
        qtd_neg = len(neg_encontradas)
        
        # 3. CONDICIONAL DE DECISÃO FINAL
        st.subheader("Resultado da Análise:")
        
        if qtd_pos > qtd_neg:
            st.success(f"😊 **Cliente Satisfeito** (Palavras positivas: {qtd_pos} | Negativas: {qtd_neg})")
        elif qtd_neg > qtd_pos:
            st.error(f"😡 **Cliente Insatisfeito** (Palavras positivas: {qtd_pos} | Negativas: {qtd_neg})")
        else:
            st.info(f"😐 **Avaliação Neutra / Indefinida** (Palavras positivas: {qtd_pos} | Negativas: {qtd_neg})")
            
        # Exibição dos Tokens extraídos
        with st.expander("Ver Detalhes dos Tokens Extraídos"):
            st.write("**Tokens identificados no texto:**", tokens)
            st.write("**Palavras Positivas:**", pos_encontradas)
            st.write("**Palavras Negativas:**", neg_encontradas)