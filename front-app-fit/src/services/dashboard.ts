import { gerarPlano } from "./ai";
import { apiFetch } from "./api";
import { getCurrentTime } from "@/services/time";

export async function getDashboardData(user: any) {
  const plano = await gerarPlano({
    horario_treino: getCurrentTime(),
    idade: user.idade,
    peso: user.peso,
    sexo: user.sexo,
    objetivo: user.objetivo,
    tipo_treino: user.tipo_treino,
    mensagem: "",
    tipo: "plano",
  });

  const [today, stats, goals, challenge] = await Promise.all([
  apiFetch("/tracking/today"),
  apiFetch("/tracking/stats"),
  apiFetch("/goals/progress"),
  apiFetch("/challenges/current"),
]);

  return {
    plano,
    today,
    stats,
    goals,
    challenge,
  };
}