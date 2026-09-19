import streamlit as st
import re
from collections import Counter
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Contador de Palavras", page_icon="📝")

st.title("📝 Frequência de Palavras em Avaliações")
st.write("Identifique as palavras mais frequentes nas avaliações dos clientes.")

# Caixa de texto para o usuário digitar a avaliação
avaliacao = st.text_area(
    "Digite ou cole a avaliação do cliente:",
    value="O produto é muito bom. O atendimento foi bom e o produto chegou rápido.",
    height=120
)

# Botão de processamento
if st.button("Contar Palavras", type="primary"):
    if avaliacao.strip():
        # 1. Converte o texto para minúsculas
        texto_limpo = avaliacao.lower()
        
        # 2. Extrai apenas as palavras (ignorando pontuações)
        palavras = re.findall(r'\b\w+\b', texto_limpo)
        
        # 3. Conta a frequência de cada palavra
        frequencia = Counter(palavras)
        
        # 4. Transforma o resultado em uma tabela do Pandas
        df_frequencia = pd.DataFrame(
            frequencia.most_common(),
            columns=["Palavra", "Frequência"]
        )
        
        st.subheader("Resultado da Análise")
        
        # Exibe em duas colunas: Tabela e Gráfico
        col1, col2 = st.columns(2)
        
        with col1:
            st.dataframe(df_frequencia, use_container_width=True)
            
        with col2:
            st.bar_chart(df_frequencia.set_index("Palavra"))
            
    else:
        st.warning("Por favor, digite algum texto para analisar.")