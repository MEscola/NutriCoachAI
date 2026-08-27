import { apiFetch } from "./api";

export type UserMe = {
  id: string;
  avatar_url: string | null;
  nome: string | null;
  idade: number | null;
  peso: number | null;
  altura: number | null;
  sexo: string | null;
  objetivo: string | null;
  tipo_treino: string | null;
  horario_treino: string | null;
};

export async function getMe(): Promise<UserMe> {
  return apiFetch("/profile/me");
}