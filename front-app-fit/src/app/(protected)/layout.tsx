import { AppLayout } from "@/components/layout/appLayout";

export default function ProtectedLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <AppLayout>{children}</AppLayout>;
}