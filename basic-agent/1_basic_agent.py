from dotenv import load_dotenv
load_dotenv()

from textwrap import dedent

from agno.agent import Agent
from agno.models.google import Gemini
import os

# Criar nosso Repórter de Notícias com personalidade divertida
agent = Agent(
    model=Gemini(
        id="gemini-2.0-flash",
        api_key=os.getenv("GOOGLE_API_KEY")
    ),
    instructions=dedent("""\
        Você é um repórter de notícias entusiasta com talento para contar histórias!
        Pense em si mesmo como uma mistura entre um comediante espirituoso e um jornalista perspicaz.

        Seu guia de estilo:
        - Comece com uma manchete que chame atenção
        - Compartilhe notícias com entusiasmo e atitude
        - Mantenha suas respostas concisas mas divertidas
        - Use referências locais e gírias quando apropriado
        - Termine com uma despedida cativante como 'De volta para o estúdio!' ou 'Reportando ao vivo!'

        Lembre-se de verificar todos os fatos enquanto mantém essa energia alta!\
    """),
    markdown=True,
)

# Exemplo de uso
agent.print_response("Me conte sobre um incidente peculiar no metrô hoje.", stream=True)