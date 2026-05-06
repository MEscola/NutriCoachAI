"use client";

import { useEffect, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { Home, BarChart3, Target, Settings, LogOut, PanelLeft } from "lucide-react";

export function Sidebar() {
  const pathname = usePathname();
  const router = useRouter();

  const [collapsed, setCollapsed] = useState(false);

  // persistência
  useEffect(() => {
    const saved = localStorage.getItem("sidebar_collapsed");
    if (saved) setCollapsed(saved === "true");
  }, []);

  useEffect(() => {
    localStorage.setItem("sidebar_collapsed", String(collapsed));
  }, [collapsed]);

  const menu = [
    { label: "Dashboard", icon: Home, path: "/dashboard" },
    { label: "Progresso", icon: BarChart3, path: "/progress" },
    { label: "Metas", icon: Target, path: "/goals" },
    { label: "Configurações", icon: Settings, path: "/settings" },
  ];

  return (
    <aside
      className={`h-screen flex flex-col justify-between border-r border-[var(--border)] bg-[var(--card)]
      transition-all duration-300
      ${collapsed ? "w-16" : "w-64"}`}
    >

      {/* TOPO */}
      <div className="px-3 py-4">

        {/* HEADER + TOGGLE */}
        <div className="flex items-center justify-between mb-8">
          
          {!collapsed && (
            <span className="text-[var(--primary)] font-semibold">
              NutriCoach
            </span>
          )}

          <button
            onClick={() => setCollapsed(!collapsed)}
            className="text-[#888] hover:text-white"
          >
            <PanelLeft size={18} />
          </button>

        </div>

        {/* MENU */}
        <nav className="flex flex-col gap-1">
          {menu.map((item) => {
            const isActive = pathname === item.path;

            return (
              <button
                key={item.path}
                onClick={() => router.push(item.path)}
                className={`flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm transition
                ${isActive
                  ? "bg-[#141414] text-white"
                  : "text-[#888] hover:bg-[#141414] hover:text-white"
                }`}
              >
                <item.icon size={18} />

                {/* TEXTO SOME QUANDO COLAPSADO */}
                {!collapsed && <span>{item.label}</span>}
              </button>
            );
          })}
        </nav>
      </div>

      {/* LOGOUT */}
      <div className="px-3 py-4">
        <button
          onClick={() => {
            localStorage.removeItem("access_token");
            router.push("/login");
          }}
          className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-[#888] hover:bg-[#141414] hover:text-white w-full"
        >
          <LogOut size={18} />
          {!collapsed && "Sair"}
        </button>
      </div>

    </aside>
  );
}