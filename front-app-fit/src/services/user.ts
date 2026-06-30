import { apiFetch } from "./api";

export type UserMe = {
  id: number;
  avatar_url: string;
  nome: string;
  idade: number;
  peso: number;
  altura: number;
  sexo: string;
  objetivo: string;
  tipo_treino: string;
};

export async function getMe(): Promise<UserMe> {
  return apiFetch("/profile/me");
}