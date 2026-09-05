import streamlit as st

# Título principal
st.title("👋 Meu Cartão de Visitas")

st.markdown("---")

# Sobre mim
st.header("👤 Sobre mim")

st.text(
    "Olá! Meu nome é wendell rodrigues de oliveira.\n"
    "Sou estudante de programação e estou aprendendo Python."
)

# Habilidades
st.header("💻 Habilidades")

st.markdown("""
- Python
- HTML
- CSS
- SQL
- Git
""")

# Objetivo
st.header("🎯 Meu objetivo")

st.text(
    "Meu objetivo é aprender programação e desenvolver "
    "meus próprios projetos."
)

# Contato
st.header("📞 Contato")

st.markdown("""
**Email:** w3ndellrodriguesdeoliveira0507@email.com

**Telefone:** (11) 91319-5555
""")

st.markdown("---")

st.markdown("⭐ Obrigado por visitar meu cartão!")