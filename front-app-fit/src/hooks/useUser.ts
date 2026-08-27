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
        setUser(data);
      } catch (err: any) {
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
    user !== null &&
    user.nome !== null &&
    user.idade !== null &&
    user.peso !== null &&
    user.altura !== null &&
    user.sexo !== null &&
    user.objetivo !== null &&
    user.tipo_treino !== null &&
    user.horario_treino !== null;

  return {
    user,
    loading,
    profileComplete,
  };
}