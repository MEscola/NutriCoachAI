"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export function useAuth() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isChecking, setIsChecking] = useState(true);

  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      router.replace("/login");
    } else {
      setIsAuthenticated(true);
    }

    setIsChecking(false);
  }, [router]);

  return { isAuthenticated, isChecking }; // isChecking para evitar flash de conteúdo protegido
}