type Props = {
  value: number;
  label?: string;
};

export function ProgressBar({ value, label }: Props) {
  return (
    <div className="flex flex-col gap-2">
      {/* label */}
      {label && (
        <div className="flex justify-between text-xs text-muted-foreground">
          <span>{label}</span>
          <span>{value}%</span>
        </div>
      )}

      {/* barra */}
      <div className="w-full h-2 bg-muted rounded-full overflow-hidden">
        <div
          className="h-full bg-primary transition-all duration-500"
          style={{ width: `${value}%` }}
        />
      </div>
    </div>
  );
}