import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API = os.getenv("CHAVE_API")

genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-3-flash-preview')

# FLUXO 1 - DÚVIDA
def gerar_resposta_duvida(dados):
    
    prompt = f"""
Você é um coach de {dados.tipo_treino} e nutricionista.

IMPORTANTE:
O usuário fez uma PERGUNTA ESPECÍFICA.

PROIBIDO:
- NÃO gerar plano completo
- NÃO sugerir rotina completa
- NÃO incluir café, almoço, jantar completo

FAÇA APENAS:
Responder a pergunta de forma direta, prática e objetiva.

Formato obrigatório:

{{
  "resposta": ""
}}

Pergunta:
{dados.mensagem}

Contexto (use apenas se necessário):
- Idade: {dados.idade}
- Peso: {dados.peso}
- Objetivo: {dados.objetivo}

REGRAS:
- Resposta curta
- Máximo 3 frases
- Sem texto fora do JSON
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    # extrai JSON
    inicio = text.find("{")
    fim = text.rfind("}") + 1
    json_str = text[inicio:fim]

    try:
        data = json.loads(json_str)
        return {"tipo": "duvida", "data": data}
    except:
        return {"erro": "Falha ao gerar resposta"}


# FLUXO 2 - PLANO DO DIA
def gerar_plano(dados):
    prompt = f"""
Você é um coach de {dados.tipo_treino} e nutricionista esportivo.

Responda APENAS em JSON válido.

Formato:

{{
  "alimentacao": {{
    "cafe": "",
    "almoco": "",
    "jantar": "",
    "lanches": ""
  }},
  "estrategia_treino": {{
    "como_atingir_objetivo": "",
    "foco": "",
    "metodo": ""
  }},
  "pre_treino": "",
  "pos_treino": "",
  "dica_extra": "",
  "pulo_do_gato": ""
}}

Dados:
- Idade: {dados.idade}
- Peso: {dados.peso}
- Sexo: {dados.sexo}
- Objetivo: {dados.objetivo}
- Tipo: {dados.tipo_treino}
- Horário: {dados.horario_treino}
- tipo: {dados.tipo}

Pedido:
{dados.mensagem if dados.mensagem else "Plano completo do dia"}

Regras:
- Seja direto
- Preencha todos os campos
- Não escreva nada fora do JSON
- O campo 'como_atingir_objetivo' deve ser motivador.
- Use terminologia de {dados.tipo_treino} (Ex: WOD, AMRAP se CrossFit | Super-set se Musculação | Pace se Corrida).
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

     # limpa JSON
    inicio = text.find("{")
    fim = text.rfind("}") + 1
    json_str = text[inicio:fim]

    try:
        data = json.loads(json_str)
        return {"tipo": "plano", "data": data}
    except:
        return {"erro": "Falha ao gerar plano"}
    
# CONTROLLER DE FLUXO
def processar_requisicao(dados):
    if dados.tipo == "duvida":
        return gerar_resposta_duvida(dados)
    else:
        return gerar_plano(dados)

    