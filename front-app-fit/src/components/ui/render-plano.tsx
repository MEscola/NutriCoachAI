"use client";

import React from "react";
import { PlanCard } from "./plan-card";
import {
  Utensils,
  Dumbbell,
  Zap,
  Target,
  Flame,
  Lightbulb,
} from "lucide-react";

export default function RenderPlano({ data }: any) {
  if (!data) return null;

  return (
    <div className="space-y-4">

      {/* ===== ALIMENTAÇÃO ===== */}
      <div className="space-y-2">
        <div className="flex items-center gap-2 text-[10px] uppercase text-zinc-400 font-bold tracking-widest">
          <Utensils size={12} /> Alimentação
        </div>

        <div className="grid gap-2">
          <PlanCard title="⚡ Pré-treino" content={data.alimentacao?.pre_treino} />
          <PlanCard title="🍳 Café da manhã" content={data.alimentacao?.cafe} />
          <PlanCard title="🔥 Pós-treino" content={data.alimentacao?.pos_treino} />
          <PlanCard title="🍗 Almoço" content={data.alimentacao?.almoco} />
          <PlanCard title="🌙 Jantar" content={data.alimentacao?.jantar} />
          <PlanCard title="🥪 Lanches" content={data.alimentacao?.lanches} />
        </div>
      </div>

      {/* ===== DICA EXTRA ===== */}
      <div className="bg-primary/10 border border-primary/30 rounded-2xl p-4 space-y-2">
        <div className="flex items-center gap-2 text-[10px] uppercase text-[var(--primary)] font-bold tracking-widest">
          <Lightbulb size={12} /> Dica do Coach
        </div>

        <p className="text-sm text-zinc-200 leading-relaxed">
          {data.dica_extra}
        </p>
      </div>
    </div>
  );
}