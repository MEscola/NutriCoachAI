"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import { useAuth } from "@/hooks/useAuth";
import { useUser } from "@/hooks/useUser";
import { apiFetch } from "@/services/api";

export default function ProfilePage() {
  const router = useRouter();

  const { isAuthenticated, isChecking } = useAuth();
  const { user, loading: userLoading } = useUser();

  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [form, setForm] = useState({
    idade: "",
    peso: "",
    altura: "",
    sexo: "",
    objetivo: "",
    tipo_treino: "",
    horario_treino: "",
  });

  useEffect(() => {
    if (!user) return;

    setForm({
      idade: user.idade?.toString() ?? "",
      peso: user.peso?.toString() ?? "",
      altura: user.altura?.toString() ?? "",
      sexo: user.sexo ?? "",
      objetivo: user.objetivo ?? "",
      tipo_treino: user.tipo_treino ?? "",
      horario_treino: user.horario_treino ?? "",
    });
  }, [user]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    setError(null);
    setSaving(true);

    try {
      const result = await apiFetch("/profile/me", {
  method: "PUT",
  body: JSON.stringify({
    idade: Number(form.idade),
    peso: Number(form.peso),
    altura: Number(form.altura),
    sexo: form.sexo,
    objetivo: form.objetivo,
    tipo_treino: form.tipo_treino,
    horario_treino: form.horario_treino,
  }),
});

console.log("PERFIL SALVO:", result);
console.log("TOKEN:", localStorage.getItem("access_token"));
console.log("INDO PARA DASHBOARD");

router.replace("/dashboard");
    } catch (err: any) {
      console.error(err);
      setError(err.message || "Erro ao atualizar perfil");
    } finally {
      setSaving(false);
    }
  }

  if (isChecking || userLoading) {
    return (
      <div className="p-6">
        Carregando perfil...
      </div>
    );
  }

  if (!isAuthenticated || !user) {
    return null;
  }

  return (
    <div className="max-w-xl mx-auto p-6">

      <div className="bg-[var(--card)] border border-[var(--border)] rounded-xl p-6">

        <h1 className="text-xl font-semibold mb-2">
          Complete seu perfil
        </h1>

        <p className="text-sm text-muted-foreground mb-6">
          Precisamos de algumas informações para personalizar seu plano.
        </p>

        <form
          onSubmit={handleSubmit}
          className="flex flex-col gap-4"
        >

          {/* IDADE */}
          <input
            type="number"
            placeholder="Idade"
            value={form.idade}
            onChange={(e) =>
              setForm({ ...form, idade: e.target.value })
            }
            className="rounded-lg px-3 py-2 bg-[var(--card)] border border-[var(--border)]"
            required
          />

          {/* PESO */}
          <input
            type="number"
            step="0.1"
            placeholder="Peso (kg)"
            value={form.peso}
            onChange={(e) =>
              setForm({ ...form, peso: e.target.value })
            }
            className="rounded-lg px-3 py-2 bg-[var(--card)] border border-[var(--border)]"
            required
          />

          {/* ALTURA */}
          <input
            type="number"
            step="0.01"
            placeholder="Altura (m)"
            value={form.altura}
            onChange={(e) =>
              setForm({ ...form, altura: e.target.value })
            }
            className="rounded-lg px-3 py-2 bg-[var(--card)] border border-[var(--border)]"
            required
          />

          {/* SEXO */}
          <select
            value={form.sexo}
            onChange={(e) =>
              setForm({ ...form, sexo: e.target.value })
            }
            className="rounded-lg px-3 py-2 bg-[var(--card)] border border-[var(--border)]"
            required
          >
            <option value="">Sexo</option>
            <option value="feminino">Feminino</option>
            <option value="masculino">Masculino</option>
          </select>

          {/* OBJETIVO */}
          <select
            value={form.objetivo}
            onChange={(e) =>
              setForm({ ...form, objetivo: e.target.value })
            }
            className="rounded-lg px-3 py-2 bg-[var(--card)] border border-[var(--border)]"
            required
          >
            <option value="">Objetivo</option>
            <option value="hipertrofia">Hipertrofia</option>
            <option value="emagrecimento">Emagrecimento</option>
            <option value="performance">Performance</option>
          </select>

          {/* TIPO TREINO */}
          <select
            value={form.tipo_treino}
            onChange={(e) =>
              setForm({ ...form, tipo_treino: e.target.value })
            }
            className="rounded-lg px-3 py-2 bg-[var(--card)] border border-[var(--border)]"
            required
          >
            <option value="">Tipo de treino</option>
            <option value="crossfit">CrossFit</option>
            <option value="musculacao">Musculação</option>
            <option value="corrida">Corrida</option>
          </select>

          {/* HORÁRIO */}
          <input
            type="time"
            value={form.horario_treino}
            onChange={(e) =>
              setForm({
                ...form,
                horario_treino: e.target.value,
              })
            }
            className="rounded-lg px-3 py-2 bg-[var(--card)] border border-[var(--border)]"
            required
          />

          {error && (
            <p className="text-red-500 text-sm">
              {error}
            </p>
          )}

          <button
            type="submit"
            disabled={saving}
            className="bg-[var(--primary)] text-black rounded-lg py-2 font-medium disabled:opacity-50"
          >
            {saving ? "Salvando..." : "Continuar"}
          </button>

        </form>
      </div>
    </div>
  );
}