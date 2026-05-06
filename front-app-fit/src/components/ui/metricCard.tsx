import { Card } from "@/components/ui/card";

type Props = {
  title: string;
  value: string | number;
};

export function MetricCard({ title, value }: any) {
  return (
    <div className="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 flex flex-col gap-2">
      
      <span className="text-sm text-[var(--muted-foreground)]">
        {title}
      </span>

      <span className="text-2xl font-semibold text-white tracking-tight">
        {value}
      </span>

    </div>
  );
}