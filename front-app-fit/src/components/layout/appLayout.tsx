"use client";

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
          <span className="text-[var(--foreground)] font-medium">
            NutriCoach
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