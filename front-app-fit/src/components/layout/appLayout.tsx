"use client";

import { welcomeMessage } from "@/services/time";
import { Sidebar } from "./sidebar";
import LogoutButton from "@/components/logout-button";

export function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen bg-[var(--background)]">
      
      {/* SIDEBAR */}
      <Sidebar />

      {/* CONTEÚDO */}
      <div className="flex-1 flex flex-col">
        
        {/* HEADER */}
        <header className="flex justify-between items-center px-6 py-4 border-b border-[var(--border)]">
          <span className="text-md text-[var(--foreground)]">
            {welcomeMessage()}, <span className="text-md font-semibold text-[var(--primary)]">Atleta 👋🏾</span>
          </span>
        
          <span className="text-sm text-[var(--muted-foreground)]">
            Aqui está seu resumo de hoje
          </span>

          <LogoutButton />
        </header>

        {/* PAGE */}
                <main className="flex-1 p-6 md:p-8">
          {children}
        </main>
      </div>
    </div>
  );
}