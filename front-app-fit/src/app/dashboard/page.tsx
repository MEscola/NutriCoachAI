"use client";

import { useEffect, useState } from "react";
import { apiFetch } from "@/services/api";
import router from "next/dist/shared/lib/router/router";
import { useRouter } from "next/navigation";

export default function Dashboard() {
  const [data, setData] = useState(null);
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      router.replace("/login");
      return;
    }

    apiFetch("/dashboard")
      .then(setData)
      .catch(() => alert("Erro ao carregar dashboard"));
  }, [router]);

  return (
    <div>
      <h1>Dashboard</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}