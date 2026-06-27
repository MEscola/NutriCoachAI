"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import { MetricCard } from "@/components/ui/metricCard";
import { ProgressBar } from "@/components/ui/progressBar";

import { useAuth } from "@/hooks/useAuth";
import { useUser } from "@/hooks/useUser";

import { getDashboardData } from "@/services/dashboard";
import { welcomeMessage } from "@/services/time";

type DashboardState = {
  plano: any;
  today: any;
  stats: any;
  goals: any;
  challenge: any;
};

export default function Dashboard() {
  const [data, setData] = useState<DashboardState | null>(null);
  const [loading, setLoading] = useState(true);

  const router = useRouter();
  const { isAuthenticated, isChecking } = useAuth();
  const { user, loading: userLoading } = useUser();

  useEffect(() => {
    if (!isAuthenticated || !user) return;

    let isMounted = true;

    async function load() {
      try {
        const result = await getDashboardData(user);
        if (isMounted) setData(result);
      } catch (err: any) {
        if (err.status === 401) {
          localStorage.removeItem("access_token");
          router.replace("/login");
        } else {
          console.error(err);
        }
      } finally {
        if (isMounted) setLoading(false);
      }
    }

    load();

    return () => {
      isMounted = false;
    };
  }, [isAuthenticated, user, router]);

  // 🔄 loading states
  if (isChecking || userLoading || loading || !user || !data) {
    return (
      <div className="p-6 md:p-8 text-muted-foreground">
        Carregando dashboard...
      </div>
    );
  }

  return (
    <div className="p-6 md:p-3 flex flex-col gap-6 md:gap-8">

      {/* HEADER */}
      <div className="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 md:p-6 flex justify-between items-center">
        <div className="flex flex-col">
          <span className="text-md text-[var(--foreground)]">
            {welcomeMessage()}, {" "}
            <span className="text-md font-semibold text-[var(--primary)]">
              {user.nome} 👋🏾
            </span>
          </span>

          <span className="text-sm text-[var(--muted-foreground)]">
            Aqui está seu resumo de hoje
          </span>
        </div>

        <div className="text-sm text-muted-foreground text-right">
          <div>{user.objetivo}</div>
          <div>{user.tipo_treino}</div>
        </div>
      </div>

      {/* MÉTRICAS */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 md:gap-6">

        {/* PESO */}
        <div className="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 flex flex-col justify-center">
          <span className="text-sm text-muted-foreground">
            Peso atual
          </span>
          <span className="text-2xl font-semibold text-[var(--primary)]">
            {user.peso} kg
          </span>
        </div>

        <MetricCard title="Score" value={data.stats?.score ?? 0} />
        <MetricCard title="Streak" value={data.stats?.streak ?? 0} />
      </div>

      {/* PROGRESSO */}
      <div className="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 md:p-6 flex flex-col gap-4">
        <h2 className="text-sm text-muted-foreground">
          Progresso geral
        </h2>

        <ProgressBar label="Aderência" value={data.stats?.aderencia ?? 0} />
        <ProgressBar label="Meta" value={data.goals?.progresso ?? 0} />
        <ProgressBar label="Challenge" value={data.challenge?.progresso ?? 0} />
      </div>

      {/* COACH AI */}
      <div className="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 md:p-6 flex flex-col gap-4">
        <h2 className="text-sm text-muted-foreground">
          Coach AI
        </h2>

        <p className="text-sm text-[var(--foreground)]">
          {data.plano?.mensagem || "Seu plano será exibido aqui"}
        </p>

        <div className="flex gap-2 mt-2">
          <input
            placeholder="Pergunte algo..."
            className="flex-1 bg-[#1a1a1a] px-3 py-2 rounded-lg text-sm outline-none"
          />

          <button className="bg-[var(--primary)] text-black px-4 rounded-lg text-sm">
            Enviar
          </button>
        </div>
      </div>

    </div>
  );
}