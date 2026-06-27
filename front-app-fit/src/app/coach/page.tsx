"use client";

import React, { useEffect, useRef, useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import RenderPlano from "@/components/ui/render-plano";
import { DSInput, DSSelect, DSTextarea } from "@/components/ui/form-field";
import { toast } from "sonner";
import { useRouter } from "next/navigation";

import { Dumbbell, Trash2, MessageCircle, ChevronRight } from "lucide-react";

import { perguntarCoach } from "@/services/coach.service";
import { useUser } from "@/hooks/useUser";

const { user, loading } = useUser();

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

// ===== TYPES =====
type Message = {
  role: "user" | "assistant";
  content?: string;
  plano?: any;
};

export default function CoachPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [perfilPreenchido, setPerfilPreenchido] = useState(false);

  const bottomRef = useRef<HTMLDivElement | null>(null);
  const router = useRouter();

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
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

  // ===== PROTEÇÃO DE ROTA =====
  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) router.replace("/login");
  }, [router]);

  // ===== LOAD PERFIL =====
  useEffect(() => {
    const perfil = localStorage.getItem("perfil");
    if (perfil) {
      reset(JSON.parse(perfil));
      setPerfilPreenchido(true);
    }
  }, [reset]);

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

  setMessages((prev) => [
    ...prev,
    { role: "user", content: userMessage },
    { role: "assistant", content: "..." },
  ]);

  try {
    const result = await perguntarCoach({
      ...data,
      tipo,
    });

    setMessages((prev) => {
      const updated = [...prev];

      if (result.tipo === "duvida") {
        updated[updated.length - 1] = {
          role: "assistant",
          content: result.data?.resposta || "Sem resposta 😅",
        };
      }

      if (result.tipo === "plano") {
        updated[updated.length - 1] = {
          role: "assistant",
          plano: result.data,
        };
      }

      return updated;
    });

    localStorage.setItem("perfil", JSON.stringify(data));
    setPerfilPreenchido(true);

    toast.success(
      tipo === "duvida"
        ? "Resposta pronta!"
        : "Plano gerado com sucesso!"
    );

    reset({ ...data, mensagem: "" });
  } catch (err) {
    toast.error("Erro ao conectar com o Coach AI.");
  }
};

  // ===== LIMPAR PERFIL =====
  const limparPerfil = () => {
    if (!confirm("Deseja limpar os dados?")) return;

    localStorage.removeItem("perfil");
    reset();
    setMessages([]);
    setPerfilPreenchido(false);

    toast.success("Perfil removido!");
  };

  const gerarPlano = () => {
    handleSubmit((data) => {
      onSubmit({ ...data, mensagem: "" });
    })();
  };

  const perfil = JSON.parse(localStorage.getItem("perfil") || "{}");

  return (
    <main className="min-h-screen bg-black text-zinc-100 flex justify-center p-4">
      <div className="w-full max-w-md">

        {/* HEADER */}
        <Card className="bg-zinc-900 border-zinc-800 rounded-3xl">
          <CardHeader className="relative text-center">

            <button
              onClick={limparPerfil}
              className="absolute right-4 top-4 text-zinc-500 hover:text-red-400"
            >
              <Trash2 size={18} />
            </button>

            <div className="flex items-center justify-center gap-3">
              <div className="bg-primary w-12 h-12 rounded-2xl flex items-center justify-center">
                <Dumbbell className="text-black" />
              </div>

              <div>
                <h1 className="text-lg font-bold">NutriCoach AI</h1>
              </div>
            </div>

            {perfilPreenchido && (
              <p className="text-xs text-zinc-400 mt-2">
                {perfil.idade} anos • {perfil.peso}kg • {perfil.objetivo}
              </p>
            )}
          </CardHeader>

          <CardContent className="space-y-4">

            {/* FORM */}
            {!perfilPreenchido ? (
              <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">

                <div className="grid grid-cols-2 gap-3">
                  <DSInput label="Idade" type="number" {...register("idade")} error={errors.idade?.message} />
                  <DSInput label="Peso" type="number" {...register("peso")} error={errors.peso?.message} />
                </div>

                <div className="grid grid-cols-2 gap-3">
                  <DSSelect label="Sexo" {...register("sexo")}>
                    <option value="">Sexo</option>
                    <option value="masculino">Masculino</option>
                    <option value="feminino">Feminino</option>
                  </DSSelect>

                  <DSSelect label="Objetivo" {...register("objetivo")}>
                    <option value="">Objetivo</option>
                    <option value="hipertrofia">Hipertrofia</option>
                    <option value="emagrecimento">Emagrecimento</option>
                  </DSSelect>
                </div>

                <DSSelect label="Treino" {...register("tipo_treino")}>
                  <option value="">Tipo</option>
                  <option value="crossfit">CrossFit</option>
                  <option value="musculacao">Musculação</option>
                </DSSelect>

                <DSInput type="time" label="Horário" {...register("horario_treino")} />

                <DSTextarea
                  label=""
                  placeholder="Pergunte algo ou gere um plano..."
                  {...register("mensagem")}
                />

                <Button type="submit" className="w-full">
                  Enviar
                </Button>

                <Button type="button" onClick={gerarPlano} className="w-full bg-primary text-black">
                  Gerar Plano
                </Button>
              </form>
            ) : (
              <form onSubmit={handleSubmit(onSubmit)}>
                <DSTextarea
                  placeholder="Pergunte ao coach..."
                  {...register("mensagem")}
                />

                <button className="mt-2 bg-primary p-2 rounded-full">
                  <ChevronRight size={16} />
                </button>
              </form>
            )}
          </CardContent>
        </Card>

        {/* CHAT */}
        <div className="mt-6 space-y-3">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
            >
              <div className={`p-3 rounded-2xl max-w-[80%] text-sm ${
                msg.role === "user"
                  ? "bg-primary text-black"
                  : "bg-zinc-800"
              }`}>
                {msg.content}
                {msg.plano && <RenderPlano data={msg.plano} />}
              </div>
            </div>
          ))}
          <div ref={bottomRef} />
        </div>

        {/* WHATSAPP */}
        <Button className="w-full mt-4 bg-green-500">
          <MessageCircle size={16} /> WhatsApp
        </Button>

      </div>
    </main>
  );
}