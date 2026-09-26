import streamlit as st
from collections import Counter
import re

st.title("📊 Palavras Mais Frequentes em Reclamações")
st.write("Identifique os termos mais citados pelos clientes para priorizar melhorias no produto.")

# Lista basica de stopwords para nao poluir o ranking de frequencias
stopwords = {
    "de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "com", "nao", "uma", "os", "no", "se", "na", "por", "mais",
    "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "aqui", "seu", "sua", "meu", "minha", "eu", "isso", "esta"
}

# Entrada do texto de reclamacao
reclamacao = st.text_area(
    "Cole o texto da reclamação ou feedback do cliente:",
    height=150,
    placeholder="Ex: O aplicativo esta lento. O aplicativo fecha sozinho na tela de pagamento. O sistema é muito lento e o pagamento nao funciona."
)

top_n = st.slider("Quantidade de palavras para exibir no ranking:", min_value=3, max_value=15, value=5)

if st.button("Analisar Frequência", type="primary"):
    if not reclamacao.strip():
        st.warning("Por favor, insira um texto para analisar.")
    else:
        # 1. Normalizacao: converter para minusculas e remover pontuacoes
        texto_limpo = re.sub(r'[^\w\s]', '', reclamacao.lower())
        
        # 2. Separar em palavras (tokenizacao simples)
        palavras = texto_limpo.split()
        
        # 3. Filtrar stopwords
        palavras_filtradas = [p for p in palavras if p not in stopwords and len(p) > 2]
        
        # 4. Contagem de frequencia
        contagem = Counter(palavras_filtradas)
        mais_comuns = contagem.most_common(top_n)
        
        st.subheader("🏆 Palavras Mais Frequentes:")
        
        if mais_comuns:
            # Exibir resultado em tabela
            for i, (palavra, freq) in enumerate(mais_comuns, 1):
                st.write(f"**{i}º** `{palavra}` — **{freq}** ocorrência(s)")
                
            # Exibir métrica geral
            st.info(f"Total de palavras analisadas (sem pontuação/stopwords): **{len(palavras_filtradas)}**")
        else:
            st.warning("Não foram encontradas palavras relevantes para contagem.")