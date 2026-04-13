"use client";

import { useState } from "react";
import { loginRequest, saveTokens } from "@/services/auth";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  const handleLogin = async () => {
    try {
      const data = await loginRequest(email, password);
      saveTokens(data);
      router.push("/dashboard");
    } catch {
      alert("Erro ao logar");
    }
  };

  return (
    <div className="flex flex-col gap-4 p-6">
      <input placeholder="email" onChange={(e) => setEmail(e.target.value)} />
      <input placeholder="senha" type="password" onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Entrar</button>
    </div>
  );
}