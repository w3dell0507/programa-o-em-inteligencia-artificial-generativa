import os
from groq import Groq


def carregar_prompt(caminho_arquivo: str) -> str:
    """Lê o conteúdo do arquivo prompt.md."""
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo '{caminho_arquivo}' não encontrado.")
    
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.read()


def gerar_resposta(prompt_costar: str) -> str:
    """Envia o prompt COSTAR para a API do Groq."""
    # Cole a sua nova chave gerada na Groq dentro das aspas:
    client = Groq(api_key="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")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing digital focado em ajudar pequenas empresas."
            },
            {
                "role": "user",
                "content": prompt_costar,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content


def main():
    arquivo_prompt = "prompt.md"

    try:
        print("Lendo o prompt...")
        prompt_costar = carregar_prompt(arquivo_prompt)

        print("Enviando solicitação para o Groq...\n")
        resposta = gerar_resposta(prompt_costar)

        print("--- Resposta Gerada ---")
        print(resposta)

    except Exception as e:
        print(f"Erro ao processar: {e}")


if __name__ == "__main__":
    main()