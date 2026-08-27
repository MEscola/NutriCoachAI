import { gerarPlano } from "./ai";
import { apiFetch } from "./api";
import { getCurrentTime } from "@/services/time";

export async function getDashboardData(user: any) {
  console.log("DASHBOARD 1 - buscando dados");

  const [today, stats, goals, challenge] = await Promise.all([
    apiFetch("/tracking/today"),
    apiFetch("/tracking/stats"),
    apiFetch("/goals/progress"),
    apiFetch("/challenges/current"),
  ]);

  console.log("DASHBOARD 2 - dados básicos recebidos");

  let plano = null;

  try {
    console.log("DASHBOARD 3 - chamando IA");

    plano = await gerarPlano({
      horario_treino: getCurrentTime(),
      idade: user.idade,
      peso: user.peso,
      sexo: user.sexo,
      objetivo: user.objetivo,
      tipo_treino: user.tipo_treino,
      mensagem: "",
      tipo: "plano",
    });

    console.log("DASHBOARD 4 - IA respondeu");
  } catch (error) {
    console.error("ERRO AO GERAR PLANO:", error);
  }

  return {
    plano,
    today,
    stats,
    goals,
    challenge,
  };
}