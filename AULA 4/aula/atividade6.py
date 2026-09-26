import streamlit as st

st.title("🤖 Chatbot de Triagem Inicial")
st.write("Identificação de palavras-chave para direcionamento de atendimento.")

# Entrada da frase do cliente
frase_cliente = st.text_input(
    "Como podemos te ajudar hoje?",
    placeholder="Ex: Estou com um erro na hora de fazer o pagamento."
)

if st.button("Enviar Mensagem", type="primary"):
    if not frase_cliente.strip():
        st.warning("Por favor, digite sua dúvida ou problema.")
    else:
        texto = frase_cliente.lower()
        
        # Verificação das palavras-chave solicitadas
        tem_cancelar = "cancelar" in texto or "cancelamento" in texto
        tem_erro = "erro" in texto or "bug" in texto or "falha" in texto
        tem_pagamento = "pagamento" in texto or "pagar" in texto
        
        st.subheader("Direcionamento do Chatbot:")
        
        # Lógica de decisão
        if tem_cancelar:
            st.error("🚫 Direcionando para o **Setor de Retenção e Cancelamento**...")
            st.info("Palavra-chave detectada: **cancelar**")
            
        elif tem_erro:
            st.warning("🛠️ Direcionando para o **Suporte Técnico**...")
            st.info("Palavra-chave detectada: **erro**")
            
        elif tem_pagamento:
            st.success("💳 Direcionando para o **Setor Financeiro**...")
            st.info("Palavra-chave detectada: **pagamento**")
            
        else:
            st.info("👤 Não identificamos o assunto exato. Direcionando para um **Atendente Geral**...")