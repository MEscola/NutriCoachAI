"use client";

import { useEffect, useState } from "react";
import { apiFetch } from "@/services/api";
import { useRouter } from "next/navigation";
import { MetricCard } from "@/components/ui/metricCard";
import { useAuth } from "@/hooks/useAuth";
import { ProgressCard } from "@/components/ui/ProgressCard";

type DashboardData = {
  score: number;
  streak: number;
  aderencia_geral: number;
  progresso_meta: number;
  challenge_progresso: number;
  mensagem: string;
};

export default function Dashboard() {
  const [data, setData] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState(true);

  const router = useRouter();

  //auth centralizado
  const { isAuthenticated, isChecking } = useAuth();

  useEffect(() => {
    if (!isAuthenticated) return;

    apiFetch("/dashboard")
      .then(setData)
      .catch((err) => {
        if (err.status === 401) {
          localStorage.removeItem("access_token");
          router.replace("/login");
        } else {
          console.error(err);
        }
      })
      .finally(() => {
        setLoading(false);
      });
  }, [isAuthenticated, router]);

  //evita flash
  if (isChecking) {
    return (
      <div className="p-6 text-muted-foreground">
        Verificando sessão...
      </div>
    );
  }

  if (!isAuthenticated) return null;

  // loading API
  if (loading) {
    return (
      <div className="p-6 text-muted-foreground">
        Carregando dashboard...
      </div>
    );
  }

  if (!data) {
    return (
      <div className="p-6 text-red-500">
        Erro ao carregar dados
      </div>
    );
  }

  return (
    <div className="p-6 flex flex-col gap-6">
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        <MetricCard title="Score" value={data.score} />
        <MetricCard title="Streak" value={data.streak} />
        <ProgressCard title="Aderência" value={data.aderencia_geral} />
        <ProgressCard title="Progresso Meta" value={data.progresso_meta} />
        <ProgressCard title="Progresso Challenge" value={data.challenge_progresso} />
      </div>

      <div className="bg-card border border-border p-4 rounded-xl">
        <p className="text-sm text-muted-foreground">
          {data.mensagem}
        </p>
      </div>
    </div>
  );
}