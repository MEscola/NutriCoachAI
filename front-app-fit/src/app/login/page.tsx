"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import { loginSchema, LoginFormData } from "@/schemas/loginSchema";
import { loginRequest, saveTokens } from "@/services/auth";
import { Card, CardContent } from "@/components/ui/card";

export default function LoginPage() {
  const router = useRouter();

  const [apiError, setApiError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [rememberEmail, setRememberEmail] = useState(false);
  const [checkingAuth, setCheckingAuth] = useState(true);

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
  });

  // AUTH CHECK + REMEMBER EMAIL (unificado)
  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (token) {
      router.replace("/dashboard");
      return;
    }

    const savedEmail = localStorage.getItem("remember_email");
    if (savedEmail) {
      setValue("email", savedEmail);
      setRememberEmail(true);
    }

    setCheckingAuth(false);
  }, [router, setValue]);

  const onSubmit = async (data: LoginFormData) => {
    setApiError(null);
    setLoading(true);

    try {
      const res = await loginRequest(data.email, data.password);
      saveTokens(res);

      if (rememberEmail) {
        localStorage.setItem("remember_email", data.email);
      } else {
        localStorage.removeItem("remember_email");
      }

      router.push("/dashboard");
    } catch (err: any) {
      setApiError(err.message || "Erro ao fazer login");
    } finally {
      setLoading(false);
    }
  };

  if (checkingAuth) {
    return (
      <div className="h-screen flex items-center justify-center">
        <p className="text-muted-foreground">Carregando...</p>
      </div>
    );
  }

  return (
    <div className="h-screen flex items-center justify-center bg-background">
      <Card className="w-full max-w-md">
        <CardContent>
          <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-4">

            <h1 className="text-xl font-semibold text-[var(--primary)] p-5 text-center">
              Entrar no NutriCoach
            </h1>

            {/* EMAIL */}
            <div className="flex flex-col gap-1">
              <input
                placeholder="Email"
                {...register("email")}
                className={`rounded-lg px-3 py-2 text-sm outline-none
                  ${errors.email
                    ? "border border-red-500"
                    : "bg-[var(--card)] border border-[var(--border)] focus:ring-1 focus:ring-[var(--primary)]"
                  }`}
              />
              {errors.email && (
                <span className="text-red-500 text-xs">
                  {errors.email.message}
                </span>
              )}
            </div>

            {/* PASSWORD */}
            <div className="flex flex-col gap-1 relative">
              <input
                type={showPassword ? "text" : "password"}
                placeholder="Senha"
                {...register("password")}
                className={`rounded-lg px-3 py-2 text-sm outline-none pr-16
                  ${errors.password
                    ? "border border-red-500"
                    : "bg-[var(--card)] border border-[var(--border)] focus:ring-1 focus:ring-[var(--primary)]"
                  }`}
              />

              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3 top-2 text-muted-foreground text-xs"
              >
                {showPassword ? "Ocultar" : "Mostrar"}
              </button>

              {errors.password && (
                <span className="text-red-500 text-xs">
                  {errors.password.message}
                </span>
              )}
            </div>

            {/* REMEMBER */}
            <label className="flex items-center gap-2 text-sm text-muted-foreground">
              <input
                type="checkbox"
                checked={rememberEmail}
                onChange={(e) => setRememberEmail(e.target.checked)}
              />
              Lembrar email
            </label>

            {/* ERROR */}
            {apiError && (
              <p className="text-red-500 text-sm">{apiError}</p>
            )}

            {/* BUTTON */}
            <button
              type="submit"
              disabled={loading}
              className="bg-[var(--primary)] text-black rounded-lg py-2 font-medium hover:opacity-90 transition disabled:opacity-50"
            >
              {loading ? "Entrando..." : "Entrar"}
            </button>

          </form>
        </CardContent>
      </Card>
    </div>
  );
}