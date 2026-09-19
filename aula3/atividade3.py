import streamlit as st

# Configuração da página
st.set_page_config(page_title="Priorização de Suporte", page_icon="🚨")

st.title("🚨 Detecção e Priorização de Suporte")
st.write("Identifique mensagens críticas com palavras negativas para atendimento prioritário.")

# Lista de palavras-chave negativas
palavras_negativas = ["ruim", "péssimo", "pessimo", "erro", "defeito", "problema", "horrível", "horrivel", "atraso"]

# Entrada da mensagem do cliente
mensagem = st.text_area(
    "Digite a mensagem do cliente:",
    value="O produto veio com erro e o atendimento foi péssimo.",
    height=120
)

if st.button("Verificar Prioridade", type="primary"):
    if mensagem.strip():
        # Converte para minúsculas para padronizar a busca
        texto_limpo = mensagem.lower()
        
        # Regra condicional: verifica se alguma palavra negativa está no texto
        palavras_encontradas = [palavra for palavra in palavras_negativas if palavra in texto_limpo]
        
        if palavras_encontradas:
            st.error("⚠️ **PRIORIDADE ALTA (Atendimento Crítico)**")
            st.write(f"**Motivo:** Foram encontradas as seguintes palavras negativas: `{', '.join(palavras_encontradas)}`")
        else:
            st.success("✅ **PRIORIDADE NORMAL**")
            st.write("Nenhuma palavra de alerta crítico foi detectada na mensagem.")
            
    else:
        st.warning("Por favor, digite uma mensagem para analisar.")