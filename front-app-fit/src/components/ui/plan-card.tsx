export function PlanCard({
  title,
  content,
}: {
  title: string;
  content: string;
}) {
  return (
    <div className="bg-zinc-900 border border-zinc-700 rounded-xl p-3">
      <p className="text-[10px] uppercase text-[var(--primary)] font-bold tracking-widest mb-1">
        {title}
      </p>
      <p className="text-sm text-zinc-200 leading-relaxed">
        {content || "—"}
      </p>
    </div>
  );
}