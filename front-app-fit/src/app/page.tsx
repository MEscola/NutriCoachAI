"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    router.replace(token ? "/dashboard" : "/login");
  }, [router]);

   return (
    <div className="h-screen flex items-center justify-center bg-background">
      <div className="bg-card border border-border p-6 rounded-xl">
        <h1 className="text-primary text-2xl">
          NutriCoachAI
        </h1>
      </div>
    </div>
  );
}