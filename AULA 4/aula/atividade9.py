import streamlit as st
import string
import re

st.title("🧹 Limpeza e Normalização de Texto")
st.write("Remova pontuações e converta todo o texto para letras minúsculas para preparar os dados para análise.")

# Entrada do texto original
texto_original = st.text_area(
    "Digite ou cole o texto original:",
    height=120,
    placeholder="Ex: Olá, Mundo! Este é um TESTE... Funciona mesmo?? (Sim, funciona!)."
)

if st.button("Limpar e Normalizar Texto", type="primary"):
    if not texto_original.strip():
        st.warning("Por favor, insira um texto para processar.")
    else:
        # 1. NORMALIZAÇÃO: Converter para letras minúsculas
        texto_minusculo = texto_original.lower()
        
        # 2. REMOÇÃO DE PONTUAÇÃO: Usando expressão regular (mantém apenas letras, números e espaços)
        texto_limpo = re.sub(r'[^\w\s]', '', texto_minusculo)
        
        # Opcional: Remover espaços duplos ou extras
        texto_limpo = re.sub(r'\s+', ' ', texto_limpo).strip()

        st.subheader("Resultado do Processamento:")
        
        # Exibição do texto limpo
        st.success(texto_limpo)

        # Detalhes da transformação
        with st.expander("Ver detalhes da transformação"):
            st.write("**Original:**", texto_original)
            st.write("**Passo 1 (Minúsculas):**", texto_minusculo)
            st.write("**Passo 2 (Sem pontuação):**", texto_limpo)