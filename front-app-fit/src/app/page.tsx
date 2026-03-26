"use client";

import React, { useEffect, useRef, useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import RenderPlano from "@/components/ui/render-plano";
import { DSInput, DSSelect, DSTextarea } from "@/components/ui/form-field";
import { toast } from "sonner";

import {
  Loader2,
  Dumbbell,
  Trash2,
  MessageCircle,
  ChevronRight,
} from "lucide-react";

// ===== SCHEMA =====
const schema = z.object({
  idade: z.coerce.number().min(1, "Informe sua idade"),
  peso: z.coerce.number().min(1, "Informe seu peso"),
  sexo: z.string().min(1, "Selecione o sexo"),
  objetivo: z.string().min(1),
  tipo_treino: z.string().min(1),
  horario_treino: z.string(),
  mensagem: z.string().optional(),
});

// 💬 CHAT TYPE
type Message = {
  role: "user" | "assistant";
  content?: string;
  plano?: any;
};

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [perfilPreenchido, setPerfilPreenchido] = useState(false);

  const bottomRef = useRef<HTMLDivElement | null>(null);

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isValid, isSubmitting },
  } = useForm({
    resolver: zodResolver(schema),
    mode: "onChange",
    defaultValues: {
      idade: undefined,
      peso: undefined,
      sexo: "",
      objetivo: "",
      tipo_treino: "",
      horario_treino: "19:00",
      mensagem: "",
    },
  });

  // ===== LOAD PERFIL =====
  useEffect(() => {
    const perfil = localStorage.getItem("perfil");
    if (perfil) {
      const data = JSON.parse(perfil);
      reset(data);
      setPerfilPreenchido(true);
    }
  }, []);

  // ===== SCROLL CHAT =====
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // ===== SUBMIT =====
  const onSubmit = async (data: any) => {
    const tipo = data.mensagem?.trim() ? "duvida" : "plano";

    const userMessage = data.mensagem?.trim()
      ? data.mensagem
      : "Gerar plano completo";

    // mensagem usuário
    setMessages((prev) => [
      ...prev,
      { role: "user", content: userMessage },
    ]);

    try {
      // loading
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "..." },
      ]);

      const res = await fetch("http://localhost:8000/perguntar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...data, tipo }),
      });

    //DEBUG
    if (!res.ok) {
      const error = await res.json();
      console.error("Erro no Backend", error);
      toast.error("Resposta inesperada do servidor.");
      return;
    }

      const result = await res.json();

      // substitui loading
      setMessages((prev) => {
        const updated = [...prev];

        if (result.tipo === "duvida") {
  updated[updated.length - 1] = {
    role: "assistant",
    content: result.data?.resposta || "Não consegui gerar resposta 😅",
  };

} else if (result.tipo === "plano") {
  updated[updated.length - 1] = {
    role: "assistant",
    plano: result.data,
  };
} else {
  updated[updated.length - 1] = {
    role: "assistant",
    content: "Resposta inesperada do servidor",
  };
}

        return updated;
      });

      toast.success(
        tipo === "duvida"
          ? "Resposta pronta!"
          : "Plano gerado com sucesso!"
      );

      localStorage.setItem("perfil", JSON.stringify(data));
      setPerfilPreenchido(true);

      reset({ ...data, mensagem: "" });
    } catch {
      toast.error("Erro ao conectar com o Coach AI.");
    }
  };

  // ===== LIMPAR PERFIL =====
  const limparPerfil = () => {
    if (confirm("Deseja limpar os dados?")) {
      localStorage.removeItem("perfil");
      reset();
      setMessages([]);
      setPerfilPreenchido(false);
      toast.success("Perfil removido!");
    }
  };

  let perfil: any = {};
try {
  perfil = JSON.parse(localStorage.getItem("perfil") || "{}");
} catch {
  perfil = {};
}

  const gerarPlano = () => {
  handleSubmit((data) => {
    onSubmit({ ...data, mensagem: "" });
  })();
};

  return (
    <main className="min-h-screen bg-black text-zinc-100 flex justify-center p-4 dark">
      <div className="w-full max-w-md">

        {/* HEADER */}
        <Card className="bg-zinc-900/90 border-zinc-800 shadow-2xl rounded-3xl overflow-hidden">
          <CardHeader className="relative text-center pb-2 border-b border-border/50">

            <button
              onClick={limparPerfil}
              className="absolute right-4 top-4 text-zinc-600 hover:text-red-400"
            >
              <Trash2 size={18} />
            </button>

            {/* LOGO */}
            <div className="flex items-center justify-center gap-3 mb-3">
              <div className="bg-primary w-12 h-12 rounded-2xl flex items-center justify-center shadow-md">
                <Dumbbell className="text-zinc-950" size={26} />
              </div>

              <div className="text-left">
                <h1 className="text-xl font-extrabold leading-tight">
                  NutriCoach AI
                </h1>
                <p className="text-[10px] text-zinc-400 leading-none">
                  Nutrição + Treino inteligente
                </p>
              </div>
            </div>

            {/* MINI PERFIL */}
            {perfilPreenchido && (
              <div className="mt-3 flex flex-col items-center gap-2">
                <p className="text-xs text-zinc-400">
                  👤 {perfil.idade} anos • {perfil.peso}kg • {perfil.objetivo}
                </p>

                <button
                  onClick={() => setPerfilPreenchido(false)}
                  className="text-[10px] px-3 py-1 bg-zinc-800 rounded-full text-primary hover:bg-zinc-700"
                >
                  Editar perfil
                </button>
              </div>
            )}
          </CardHeader>

          <CardContent className="pt-6">

            {!perfilPreenchido ? (
              <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">

                {/* PERFIL */}
                {!perfilPreenchido && (
                  <>
                    <div className="grid grid-cols-2 gap-4">
                      <DSInput label="Idade" type="number" error={errors.idade?.message} {...register("idade")} />
                      <DSInput label="Peso" type="number" error={errors.peso?.message} {...register("peso")} />
                    </div>

                    <div className="grid grid-cols-2 gap-4">
                      <DSSelect label="Sexo" {...register("sexo")}>
                        <option value="">Sexo</option>
                        <option value="masculino">Masculino</option>
                        <option value="feminino">Feminino</option>
                      </DSSelect>

                      <DSSelect label="Objetivo" {...register("objetivo")}>
                        <option value="">Objetivo</option>
                        <option value="hipertrofia">Hipertrofia</option>
                        <option value="emagrecimento">Emagrecimento</option>
                        <option value="performance">Performance</option>
                      </DSSelect>
                    </div>

                    <DSSelect label="Tipo de treino" {...register("tipo_treino")}>
                      <option value="">Selecione</option>
                      <option value="crossfit">CrossFit</option>
                      <option value="musculacao">Musculação</option>
                      <option value="corrida">Corrida</option>
                    </DSSelect>

                    <DSInput
                      label="Horário do treino"
                      type="time"
                      {...register("horario_treino")}
                    />
                  </>
                )}

                {/* CHAT INPUT (SEMPRE VISÍVEL) */}
                <div className="relative">
                  <DSTextarea
                    label={""} placeholder="Pergunte algo ou deixe vazio para gerar um plano..."
                    {...register("mensagem")}                  />

                  <button
                    type="submit"
                    className="absolute bottom-3 right-3 bg-primary text-black p-2 rounded-full"
                  >
                    <ChevronRight size={16} />
                  </button>
                </div>

                {/*  BOTÃO PLANO */}
                <Button
                  type="button"
                  onClick={gerarPlano}
                  className="w-full bg-primary text-black font-bold h-14 rounded-2xl"
                >
                  Gerar Plano Completo
                </Button>
              </form>
            ) : (
              <form onSubmit={handleSubmit(onSubmit)}>
                <div className="relative">
                  <DSTextarea
                    label={""} placeholder="Pergunte ao seu coach..."
                    {...register("mensagem")}
                  />

                  <button
                    type="submit"
                    className="absolute bottom-3 right-3 bg-primary text-black p-2 rounded-full"
                  >
                    <ChevronRight size={16} />
                  </button>
                </div>
              </form>
            )}

          </CardContent>
        </Card>

        {/* CHAT */}
        <div className="mt-6 space-y-3">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"
                }`}
            >
              <div
                className={`max-w-[80%] px-4 py-3 rounded-2xl text-sm whitespace-pre-wrap ${msg.role === "user"
                    ? "bg-primary text-black rounded-br-none"
                    : "bg-zinc-800 text-white rounded-bl-none"
                  }`}
              >
                {msg.content && <span>{msg.content}</span>}
                {msg.plano && <RenderPlano data={msg.plano} />}
              </div>
            </div>
          ))}
          <div ref={bottomRef} />
        </div>

        <Button className="w-full mt-4 bg-[#25D366] text-white font-bold rounded-2xl h-12 flex items-center justify-center gap-2">
          <MessageCircle size={18} /> Compartilhar no WhatsApp
        </Button>
      </div>
    </main>
  );
}