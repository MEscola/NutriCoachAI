"use client";

import { useEffect, useState } from "react";
import { getMe, UserMe } from "@/services/user";
import { useRouter } from "next/navigation";

export function useUser() {
  const [user, setUser] = useState<UserMe | null>(null);
  const [loading, setLoading] = useState(true);

  const router = useRouter();

  useEffect(() => {
    async function load() {
      try {
        const data = await getMe();

        console.log("USER RECEBIDO:", data);

        setUser(data);
      } catch (err: any) {
        console.error("ERRO AO BUSCAR USUÁRIO:", err);

        if (err.status === 401) {
          localStorage.removeItem("access_token");
          localStorage.removeItem("refresh_token");
          router.replace("/login");
        }
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [router]);

  const profileComplete =
    !!user &&
    !!user.nome &&
    !!user.idade &&
    !!user.peso &&
    !!user.altura &&
    !!user.sexo &&
    !!user.objetivo &&
    !!user.tipo_treino &&
    !!user.horario_treino;

  console.log("PROFILE COMPLETE:", profileComplete);

  return {
    user,
    loading,
    profileComplete,
  };
}