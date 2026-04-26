# NutriCoachAI

AI-powered performance assistant that generates personalized nutrition and workout strategies, combined with user progress tracking and gamified challenges.

> ⚠️ Projeto em evolução — arquitetura e funcionalidades sendo continuamente aprimoradas.

---

## Problema

Planejar treino e alimentação de forma personalizada é complexo e difícil de manter ao longo do tempo.

Além disso, falta consistência e acompanhamento — fatores essenciais para evolução.

O NutriCoachAI resolve isso combinando:
- recomendações inteligentes com IA
- acompanhamento de progresso
- sistema de desafios gamificado

---

## Funcionalidades

### Inteligência Artificial
- Geração de estratégias personalizadas de treino e nutrição
- Interpretação de intenção do usuário
- Sugestões de pré e pós-treino

### Sistema de Desafios
- Criação e gerenciamento de challenges (ex: flexões)
- Controle de status:
  - ativo
  - concluído
  - cancelado
- Progressão ao longo do tempo

### Acompanhamento de Progresso
- Registro de evolução do usuário
- Base para métricas e análise futura

### Gamificação
- Engajamento por meio de desafios
- Incentivo à consistência

### Autenticação
- Sistema de autenticação implementado
- Base para controle de usuários

---

## Arquitetura

Arquitetura baseada em separação de responsabilidades (client-server):

- **Frontend** → interface e experiência do usuário  
- **Backend** → regras de negócio, autenticação e processamento  
- **Banco de Dados** → persistência com Supabase  
- **IA (Gemini)** → geração de respostas inteligentes  

### Fluxo principal

1. Usuário interage via frontend  
2. Backend valida e processa dados  
3. Dados persistidos no banco (quando necessário)  
4. IA gera recomendações personalizadas  
5. Backend retorna resposta estruturada  
6. Frontend exibe e atualiza progresso  

---

## Tecnologias

### Frontend
- Next.js 15+
- TypeScript
- Tailwind CSS
- shadcn/ui

### Backend
- Python
- FastAPI
- Pydantic
- Slowapi (rate limiting)

### Banco de Dados
- Supabase (PostgreSQL)

### Inteligência Artificial
- Google Gemini API

---

## Estrutura de Dados (exemplo)

```python
class DadosUsuario(BaseModel):
    horario_treino: str
    idade: int
    peso: float
    sexo: str
    objetivo: str
    tipo_treino: str
    mensagem: Optional[str] = ""
```

## Exemplo de Uso da API

{
  "horario_treino": "07:00",
  "idade": 30,
  "peso": 70,
  "sexo": "Feminino",
  "objetivo": "Hipertrofia",
  "tipo_treino": "CrossFit",
  "mensagem": "O que comer antes do treino?"
}
---
## Instalação Backend
´´´
cd server
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn google-generativeai python-dotenv slowapi pydantic
´´´
# Execute

´´´
uvicorn app.main:app --reload
´´´
## Frontend
´´´
cd front-app-fit
npm install
npm run dev
´´´
## Segurança

Validação de dados com Pydantic
Rate limiting por IP
Autenticação de usuários
Middleware de tratamento de erros e logging

## Uso de Inteligência Artificial

O projeto utiliza a API do Google Gemini para geração de recomendações personalizadas.

Durante o desenvolvimento, ferramentas de IA foram utilizadas como apoio para:

Estruturação de lógica e arquitetura
Otimização de código
Revisão de boas práticas
Apoio em decisões técnicas

O uso de IA atua como acelerador de produtividade, não substituindo decisões de engenharia.

## Próximos Passos

Dashboard completo de métricas
Melhorias de UX/UI
Evolução da gamificação
Deploy e CI/CD
Escalabilidade da infraestrutura

👩‍💻Autora

Márcia Escolástico