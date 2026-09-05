import streamlit as st

# Título
st.title("📝 Cadastro de Usuário")

st.markdown("Preencha os dados abaixo para realizar seu cadastro.")

st.markdown("---")

# Nome
st.header("👤 Informações pessoais")

nome = st.text_input(
    "Nome completo:",
    placeholder="Digite seu nome"
)

# Idade
idade = st.number_input(
    "Idade:",
    min_value=1,
    max_value=120,
    value=18,
    step=1
)

# Termos
st.header("📋 Termos de uso")

termos = st.checkbox(
    "✅ Eu aceito os termos de uso"
)

st.markdown("---")

# Botão
if st.button("🚀 Finalizar Cadastro", use_container_width=True):

    if nome == "":
        st.warning("⚠️ Por favor, informe seu nome.")

    elif not termos:
        st.warning("⚠️ Você precisa aceitar os termos de uso.")

    else:
        st.success("🎉 Cadastro realizado com sucesso!")

        st.markdown("### 📌 Dados cadastrados")

        st.info(f"👤 **Nome:** {nome}")
        st.info(f"🎂 **Idade:** {idade}")
        st.info("✅ **Termos de uso:** Aceitos")