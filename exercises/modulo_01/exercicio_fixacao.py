"""
Módulo 1 — Como LLMs funcionam
Exercício de fixação: Chatbot com histórico de conversa

Objetivo:
    Construir um chatbot simples no terminal que mantém histórico
    entre mensagens — algo que a API não faz sozinha.

Conceitos praticados:
    - Context window (você monta o contexto manualmente)
    - Stateless (o modelo não lembra — você reenvia o histórico)
    - Tokens (você vai observar o crescimento a cada chamada)

Pré-requisitos:
    pip install groq

Uso:
    python exercicio_fixacao.py
    Digite "sair" para encerrar.
"""

from groq import Groq

# ─────────────────────────────────────────────
# Configuração
# ─────────────────────────────────────────────
client = Groq(api_key=os.getenv("GROQ_API_KEY", ""))

# O histórico começa com o system prompt.
# Ele será reenviado em TODAS as chamadas — ocupa tokens de input sempre.
historico = [
    {
        "role": "system",
        "content": "Você é um assistente direto e objetivo. Responda em português."
    }
]


# ─────────────────────────────────────────────
# Função principal
# ─────────────────────────────────────────────
def chat(mensagem_usuario: str) -> str:
    """
    Envia uma mensagem para o modelo e mantém o histórico da conversa.

    Args:
        mensagem_usuario: texto digitado pelo usuário

    Returns:
        texto da resposta do modelo
    """
    # 1. Adicione a mensagem do usuário ao histórico
    historico.append({"role": "user", "content": mensagem_usuario})
    # TODO
    # 2. Chame a API enviando o histórico completo
    resposta = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=historico)
    #    Use o modelo: "llama3-8b-8192"
    # TODO
    # substitua pelo retorno da API
    # TODO
    texto_resposta = resposta.choices[0].message.content  # substitua pela extração correta

    # 4. Adicione a resposta do modelo ao histórico
    #    Dica: role="assistant"
    # historico.append({"role": "assistant", "content": texto_resposta})
    # TODO

    # 5. Imprima os tokens usados nessa chamada
    #    Dica: resposta.usage tem .prompt_tokens, .completion_tokens, .total_tokens
    print(f"Tokens usados: prompt={resposta.usage.prompt_tokens}, "
          f"completion={resposta.usage.completion_tokens}, "
          f"total={resposta.usage.total_tokens}")
    # TODO

    # 6. Retorne o texto da resposta
    return texto_resposta


# ─────────────────────────────────────────────
# Loop de conversa
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("Chatbot iniciado. Digite 'sair' para encerrar.\n")

    while True:
        entrada = input("Você: ").strip()

        if not entrada:
            continue

        if entrada.lower() == "sair":
            print(f"\nConversa encerrada. Total de trocas: {len(historico)} mensagens no histórico.")
            break

        resposta = chat(entrada)
        print(f"Bot: {resposta}\n")


# ─────────────────────────────────────────────
# Perguntas para reflexão (responda como comentário aqui)
# ─────────────────────────────────────────────
# Q1: Na 3ª mensagem do usuário, quantos tokens de input você tem
#     comparado com a 1ª mensagem? Por quê?
#
# Resposta: ...
#
# Q2: O que aconteceria se você NÃO adicionasse a resposta do modelo
#     ao histórico (passo 4)?
#
# Resposta: ...
# Q2: sem adicionar a resposta do modelo ao histórico, ele perderia
# a memória das próprias respostas anteriores. Cada pergunta pareceria
# independente — ele não saberia o que já explicou nem poderia dar
# continuidade à conversa.
# Q2: testei na prática comentando o passo 4. O modelo respondia cada
# pergunta mas sem conexão com as anteriores — como se cada mensagem
# fosse uma conversa nova. Isso prova que a "memória" do chatbot não
# está no modelo, está no histórico que a aplicação monta e envia.