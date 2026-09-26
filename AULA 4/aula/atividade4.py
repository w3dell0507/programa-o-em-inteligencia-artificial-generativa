import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Garante o download dos recursos necessários
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

st.title("Remoção de Stopwords")

# Caixa de texto
texto = st.text_area("Cole seu texto aqui:")

if st.button("Processar"):
    if texto:
        stop_words = set(stopwords.words('portuguese'))
        palavras = word_tokenize(texto)
        
        # Filtra mantendo apenas o que não é stopword e não é pontuação
        resultado = [p for p in palavras if p.isalnum() and p.lower() not in stop_words]
        
        st.subheader("Resultado:")
        st.write(" ".join(resultado))
    else:
        st.warning("Por favor, digite um texto.")