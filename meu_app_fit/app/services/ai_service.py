import json
import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-3-flash-preview')


def salvar_plano(plano):
    # Aqui você pode implementar a lógica para salvar o plano no banco de dados
    # Por exemplo, usando SQLAlchemy:
    # from app.db import SessionLocal
    # from app.models import Plano
    #
    # db = SessionLocal()
    # novo_plano = Plano(**plano)
    # db.add(novo_plano)
    # db.commit()
    pass


# FLUXO DÚVIDA
def gerar_resposta_duvida(dados):
    prompt = f"""
Você é um coach de {dados.tipo_treino} e nutricionista.

Responda APENAS a pergunta de forma direta.

Formato:
{{
  "resposta": ""
}}

Pergunta:
{dados.mensagem}

Regras:
- Máximo 3 frases
- Sem texto fora do JSON
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    inicio = text.find("{")
    fim = text.rfind("}") + 1
    json_str = text[inicio:fim]

    try:
        data = json.loads(json_str)
        return {"tipo": "duvida", "data": data}
    except:
        return {"erro": "Falha ao gerar resposta"}


# FLUXO PLANO
def gerar_plano(user_id, dados): 
    prompt = f"""
Você é um coach de {dados.tipo_treino} e nutricionista.

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

Dados:
- Idade: {dados.idade}
- Peso: {dados.peso}
- Sexo: {dados.sexo}
- Objetivo: {dados.objetivo}
- Tipo: {dados.tipo_treino}
- Horário: {dados.horario_treino}

Regras:
- Simples e prático
- Sem texto fora do JSON
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    inicio = text.find("{")
    fim = text.rfind("}") + 1
    json_str = text[inicio:fim]

    try:
        data = json.loads(json_str)

        plano = {
            "user_id": str(user_id), # Substitua pelo ID real do usuário
            "date": "2026-03-27",
            "alimentacao": data["alimentacao"],
            "dica_extra": data["dica_extra"]
        }

        salvar_plano(plano)

        return {"tipo": "plano", "data": plano}

    except:
        return {"erro": "Falha ao gerar plano"}