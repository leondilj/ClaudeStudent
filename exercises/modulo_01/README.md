# Módulo 1 — Exercício de fixação

## Objetivo

Construir um chatbot simples no terminal que mantém histórico de conversa entre mensagens — algo que a API **não faz sozinha**.

## Conceitos praticados

| Conceito | O que você vai observar |
|---|---|
| **Stateless** | O modelo não lembra nada — você precisa reenviar o histórico |
| **Context window** | Você monta o contexto manualmente a cada chamada |
| **Tokens** | Os tokens de input crescem a cada mensagem — veja no terminal |

## Como rodar

```bash
# Instale a dependência
pip install groq

# Configure sua chave no script
# Substitua "sua_chave_aqui" pela sua chave da Groq

# Execute
python exercicio_fixacao.py
```

## O que implementar

Preencha os 6 TODOs dentro da função `chat()`:

1. Adicionar mensagem do usuário ao histórico
2. Chamar a API enviando o histórico completo
3. Extrair o texto da resposta
4. Adicionar a resposta do modelo ao histórico
5. Imprimir os tokens usados
6. Retornar o texto

## Perguntas de reflexão

Após o chatbot funcionar, responda como comentário no próprio script:

- Na 3ª mensagem, quantos tokens de input você tem comparado com a 1ª? Por quê?
- O que acontece se você **não** adicionar a resposta do modelo ao histórico?

## Estrutura esperada do histórico após 2 trocas

```python
[
    {"role": "system",    "content": "Você é um assistente..."},  # sempre presente
    {"role": "user",      "content": "primeira pergunta"},
    {"role": "assistant", "content": "primeira resposta"},
    {"role": "user",      "content": "segunda pergunta"},
    {"role": "assistant", "content": "segunda resposta"},
]
```
