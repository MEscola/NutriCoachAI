// services/coach.service.ts

export type CoachTipo = "duvida" | "plano";

export interface CoachRequest {
  idade: number;
  peso: number;
  sexo: string;
  objetivo: string;
  tipo_treino: string;
  horario_treino: string;
  mensagem?: string;
  tipo: CoachTipo;
}

export interface CoachResponse {
  tipo: CoachTipo;
  data: any;
}

export async function perguntarCoach(
  payload: CoachRequest
): Promise<CoachResponse> {
  const res = await fetch("http://localhost:8000/perguntar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    const error = await res.json().catch(() => ({}));
    throw new Error(error?.message || "Erro no coach");
  }

  return res.json();
}