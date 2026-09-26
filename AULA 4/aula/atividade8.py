import streamlit as st

st.title("🏷️ Classificador de Mensagens")
st.write("Triagem automática entre **Suporte Técnico** e **Financeiro** com base em palavras-chave.")

# Palavras-chave de cada categoria
palavras_tecnico = ["erro", "bug", "senha", "login", "sistema", "acesso", "trava", "lento", "configurar", "app"]
palavras_financeiro = ["fatura", "boleto", "pagamento", "cobrança", "reembolso", "nota", "cartão", "pix", "valor", "preço"]

# Entrada de texto do cliente
mensagem = st.text_area(
    "Digite a mensagem do cliente:",
    placeholder="Ex: Não consigo fazer login no aplicativo para pegar minha fatura."
)

if st.button("Classificar Mensagem", type="primary"):
    if not mensagem.strip():
        st.warning("Por favor, digite uma mensagem.")
    else:
        mensagem_lc = mensagem.lower()
        
        # Identificação das palavras presentes na mensagem
        tecnico_encontradas = [palavra for palavra in palavras_tecnico if palavra in mensagem_lc]
        financeiro_encontradas = [palavra for palavra in palavras_financeiro if palavra in mensagem_lc]
        
        score_tecnico = len(tecnico_encontradas)
        score_financeiro = len(financeiro_encontradas)
        
        st.subheader("Resultado do Direcionamento:")
        
        # Estrutura condicional simples para classificação
        if score_tecnico > score_financeiro:
            st.warning(f"💻 **Categoria: SUPORTE TÉCNICO**")
            st.write(f"Termos identificados: {', '.join(tecnico_encontradas)}")
            
        elif score_financeiro > score_tecnico:
            st.success(f"💳 **Categoria: FINANCEIRO**")
            st.write(f"Termos identificados: {', '.join(financeiro_encontradas)}")
            
        elif score_tecnico > 0 and score_financeiro > 0:
            st.info(f"🔀 **Categoria: MISTA (Técnico + Financeiro)**")
            st.write(f"Termos técnicos: {', '.join(tecnico_encontradas)}")
            st.write(f"Termos financeiros: {', '.join(financeiro_encontradas)}")
            
        else:
            st.error("❓ **Categoria: NÃO IDENTIFICADA** (Nenhuma palavra-chave encontrada)")