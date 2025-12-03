import os

from agno.agent import Agent
from agno.models.google import Gemini

from dotenv import load_dotenv
load_dotenv()


#Criando nosso primeiro agente!
contador_de_historias = Agent (
    # o Modelo que vai "pensar" por trás do agente
    model=Gemini(id="gemini-2.5-flash-lite"),

    # Descrição: quem é esse agente?
    description="Você é um contador de histórias brasileiro muito criativo",

    # Instruções: como ele deve se comportar?
    instructions=[
        "Conte histórias envolventes e divertidas",
        "Use elementos da cultura brasileira",
        "Faça suspense quando apropriado",
        "Seja bem descritivo e criativo"
    ],

    # Formatação em markdown para ficar bonito
    markdown=True
)

print("Contador de histórias criado!")
print("Agora vamos ver ele contando uma história em tempo real...")

print("\n" + "=" * 60)


#Usando streaming - vai mostrar a resposta conforme ela é gerada

while True:
    user_input = input("Peça para o agente contar uma história (Descreva brevemente sobre qual tema seria a história): ")
    if user_input.lower() == "sair":
        break
    contador_de_historias.print_response(user_input,
        stream=True
    )