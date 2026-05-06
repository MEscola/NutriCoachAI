import { Card } from "@/components/ui/card";
import { ProgressBar } from "@/components/ui/progress";

type Props = {
  title: string;
  value: number;
};

export function ProgressCard({ title, value }: Props) {
  return (
    <Card className="p-4 flex flex-col gap-3">
      <span className="text-sm text-muted-foreground">
        {title}
      </span>

      <span className="text-xl font-semibold text-[var(--primary)]">
        {value}%
      </span>

      <ProgressBar value={value} />
    </Card>
  );
}