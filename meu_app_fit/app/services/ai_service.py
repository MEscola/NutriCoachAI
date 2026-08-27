import json
import os

import google.generativeai as genai
from dotenv import load_dotenv

from app.models.user import User


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-3-flash-preview")


# FLUXO DÚVIDA

def gerar_resposta_duvida(user: User, mensagem: str):

    prompt = f"""
Você é um coach de {user.tipo_treino} e nutricionista.

Responda APENAS à pergunta de forma direta.

Formato JSON:

{{
  "resposta": ""
}}

Dados do usuário:

Objetivo:
{user.objetivo}

Peso:
{user.peso}

Altura:
{user.altura}

Pergunta:
{mensagem}

Regras:
- Máximo 3 frases
- Sem texto fora do JSON
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    inicio = text.find("{")
    fim = text.rfind("}") + 1

    if inicio == -1 or fim == 0:
        raise ValueError("IA não retornou JSON válido")

    json_str = text[inicio:fim]

    return json.loads(json_str)


# FLUXO PLANO

def gerar_plano(user: User):

    prompt = f"""
Você é um coach de {user.tipo_treino} e nutricionista.

Gere um plano alimentar simples e prático.

Formato JSON:

{{
  "alimentacao": {{
    "pre_treino": "",
    "cafe": "",
    "pos_treino": "",
    "almoco": "",
    "jantar": "",
    "lanches": ""
  }},
  "dica_extra": ""
}}

Dados do usuário:

Idade: {user.idade}
Peso: {user.peso}
Sexo: {user.sexo}
Objetivo: {user.objetivo}
Treino: {user.tipo_treino}
Horário: {user.horario_treino}

Regras:

- Simples e prático
- Sem texto fora do JSON
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    inicio = text.find("{")
    fim = text.rfind("}") + 1

    if inicio == -1 or fim == 0:
        raise ValueError("IA não retornou JSON válido")

    json_str = text[inicio:fim]

    return json.loads(json_str)