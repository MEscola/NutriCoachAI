// components/ui/form-field.tsx
import React from "react";
import { Input } from "@/components/ui/input";

interface BaseProps {
  label: string;
  error?: string;
  icon?: React.ReactNode;
}

// ================= INPUT =================
export function DSInput({ label, error, icon, ...props }: BaseProps & React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <div className="space-y-2">
      <label className="text-[10px] text-zinc-400 uppercase font-bold tracking-widest ml-1">
        {label}
      </label>

      <div className="relative">
        <Input
          {...props}
          className={`bg-zinc-800/80 border-zinc-700 text-white h-12 rounded-xl font-light pr-10 focus-visible:ring-primary transition-all ${error ? "border-red-400/40" : ""}`}
        />

        {icon && (
          <div className="absolute right-3 top-1/2 -translate-y-1/2 text-zinc-400">
            {icon}
          </div>
        )}
      </div>

      {error && <p className="text-[10px] text-red-400 ml-1">{error}</p>}
    </div>
  );
}

// ================= SELECT =================
export function DSSelect({ label, error, children, ...props }: BaseProps & React.SelectHTMLAttributes<HTMLSelectElement>) {
  return (
    <div className="space-y-2">
      <label className="text-[10px] text-zinc-400 uppercase font-bold tracking-widest ml-1">
        {label}
      </label>

      <select
        {...props}
        className={`flex h-12 w-full rounded-xl border border-zinc-700 bg-zinc-800/80 px-3 text-sm font-light text-white focus:outline-none focus:ring-2 focus:ring-primary transition-all ${error ? "border-red-400/40" : ""}`}
      >
        {children}
      </select>

      {error && <p className="text-[10px] text-red-400 ml-1">{error}</p>}
    </div>
  );
}

// ================= TEXTAREA =================
export function DSTextarea({ label, error, ...props }: BaseProps & React.TextareaHTMLAttributes<HTMLTextAreaElement>) {
  return (
    <div className="space-y-2">
      <label className="text-[10px] text-zinc-400 uppercase font-bold tracking-widest ml-1">
        {label}
      </label>

      <textarea
        {...props}
        className={`w-full min-h-[100px] rounded-2xl border border-zinc-700 bg-zinc-800/80 px-4 py-3 text-sm text-zinc-100 focus:outline-none focus:ring-2 focus:ring-primary/40 transition-all resize-none placeholder:text-zinc-600 font-medium ${error ? "border-red-400/40" : ""}`}
      />

      {error && <p className="text-[10px] text-red-400 ml-1">{error}</p>}
    </div>
  );
}

// ================= EXEMPLO DE USO =================

/*

<DSInput
  label="Idade"
  type="number"
  placeholder="Ex: 28"
  value={idade}
  onChange={(e) => setIdade(e.target.value)}
/>

<DSSelect label="Sexo">
  <option value="">Selecione</option>
  <option value="masculino">Masculino</option>
  <option value="feminino">Feminino</option>
</DSSelect>

<DSTextarea
  label="Mensagem"
  placeholder="Digite aqui..."
/>

*/
