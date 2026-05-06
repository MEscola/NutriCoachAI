type ProgressBarProps = {
  value: number; // 0 a 100
  label?: string;
};

export function ProgressBar({ value, label }: ProgressBarProps) {
  const safeValue = Math.min(100, Math.max(0, value));

  return (
    <div className="flex flex-col gap-2 w-full">

      {/* LABEL */}
      {label && (
        <div className="flex justify-between text-sm text-muted-foreground">
          <span>{label}</span>
          <span>{safeValue}%</span>
        </div>
      )}

      {/* TRACK */}
      <div className="w-full h-2 rounded-full bg-[#1a1a1a] overflow-hidden">
        
        {/* FILL */}
        <div
          className="h-full bg-[var(--primary)] transition-all duration-500 ease-out"
          style={{ width: `${safeValue}%` }}
        />
      </div>

    </div>
  );
}