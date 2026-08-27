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

      console.log("1. BUSCANDO USUÁRIO...");

      try {
        const data = await getMe();

         console.log("2. USER RECEBIDO:", data);

        setUser(data);
      } catch (err: any) {
        console.error("3.ERRO AO BUSCAR USUÁRIO:", err);

        if (err.status === 401) {
          localStorage.removeItem("access_token");
          localStorage.removeItem("refresh_token");
          router.replace("/login");
        }
      } finally {
        console.log("4.FINALIZOU BUSCA USUARIO")
        setLoading(false);
      }
    }

    load();
  }, [router]);

 const profileComplete =
  user !== null &&
  user.nome !== null &&
  user.nome.trim() !== "" &&
  user.idade !== null &&
  user.idade > 0 &&
  user.peso !== null &&
  user.peso > 0 &&
  user.altura !== null &&
  user.altura > 0 &&
  user.sexo !== null &&
  user.sexo !== "" &&
  user.objetivo !== null &&
  user.objetivo !== "" &&
  user.tipo_treino !== null &&
  user.tipo_treino !== "" &&
  user.horario_treino !== null &&
  user.horario_treino !== "";

  console.log("USER:", user);
  console.log("PROFILE COMPLETE:", profileComplete);

  return {
    user,
    loading,
    profileComplete,
  };
}