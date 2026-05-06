import { Card } from "@/components/ui/card";

type Props = {
  title: string;
  value: string | number;
};

export function MetricCard({ title, value }: Props) {
  return (
    <Card>
      <div className="flex flex-col gap-1">
        <span className="text-sm text-muted-foreground">
          {title}
        </span>
        <span className="text-2xl font-semibold text-primary">
          {value}
        </span>
      </div>
    </Card>
  );
}