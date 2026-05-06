import { gerarPlano } from "./ai";
import { apiFetch } from "./api";
import { getCurrentTime } from "@/services/time";

export async function getDashboardData() {
  const plano = await gerarPlano({
    horario_treino: getCurrentTime(),
    idade: 25,
    peso: 72,
    sexo: "masculino",
    objetivo: "hipertrofia",
    tipo_treino: "crossfit",
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