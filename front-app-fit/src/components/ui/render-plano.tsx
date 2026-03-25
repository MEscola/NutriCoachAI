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
          <PlanCard title="🍳 Café da manhã" content={data.alimentacao?.cafe} />
          <PlanCard title="🍗 Almoço" content={data.alimentacao?.almoco} />
          <PlanCard title="🌙 Jantar" content={data.alimentacao?.jantar} />
          <PlanCard title="🥪 Lanches" content={data.alimentacao?.lanches} />
        </div>
      </div>

      {/* ===== TREINO ===== */}
      <div className="space-y-2">
        <div className="flex items-center gap-2 text-[10px] uppercase text-zinc-400 font-bold tracking-widest">
          <Dumbbell size={12} /> Estratégia de treino
        </div>

        <div className="grid gap-2">
          <PlanCard
            title="🎯 Como atingir o objetivo"
            content={data.estrategia_treino?.como_atingir_objetivo}
          />

          <PlanCard
            title="🔥 Foco do dia"
            content={data.estrategia_treino?.foco}
          />

          <PlanCard
            title="📈 Método"
            content={data.estrategia_treino?.metodo}
          />
        </div>
      </div>

      {/* ===== PRÉ / PÓS ===== */}
      <div className="grid grid-cols-1 gap-2">
        <PlanCard
          title="⚡ Pré-treino"
          content={data.pre_treino}
        />
        <PlanCard
          title="🔥 Pós-treino"
          content={data.pos_treino}
        />
      </div>

      {/* ===== DICA EXTRA ===== */}
      <div className="bg-primary/10 border border-primary/30 rounded-2xl p-4 space-y-2">
        <div className="flex items-center gap-2 text-[10px] uppercase text-primary font-bold tracking-widest">
          <Lightbulb size={12} /> Dica do Coach
        </div>

        <p className="text-sm text-zinc-200 leading-relaxed">
          {data.dica_extra}
        </p>
      </div>
    </div>
  );
}