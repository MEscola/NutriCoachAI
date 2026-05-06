import { apiFetch } from "./api";

type PlanoRequest = {
  horario_treino: string;
  idade: number;
  peso: number;
  sexo: string;
  objetivo: string;
  tipo_treino: string;
  mensagem: string;
  tipo: "plano";
};

export function gerarPlano(data: PlanoRequest) {
  return apiFetch("/ai/plano", {
    method: "POST",
    body: JSON.stringify(data),
  });
}