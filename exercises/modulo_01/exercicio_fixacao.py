from groq import Groq

client = Groq(api_key="sua_chave")

historico = [
    {"role": "system", "content": "Você é um assistente direto e objetivo."}
]

def chat(mensagem_usuario: str) -> str:
    # 1. adicione a mensagem do usuário ao histórico
    
    # 2. chame a API enviando o histórico completo
    
    # 3. extraia o texto da resposta
    
    # 4. adicione a resposta ao histórico
    
    # 5. imprima os tokens usados
    
    # 6. retorne o texto da resposta

# Loop simples para testar
# while True:
#     entrada = input("Você: ")
#     if entrada.lower() == "sair":
#         break
#     resposta = chat(entrada)
#     print(f"Bot: {resposta}\n")