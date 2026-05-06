import LogoutButton from "@/components/logout-button";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR" className="dark">
      <body>
        <header className="flex justify-between p-4">
          <span>NutriCoach</span>
          <LogoutButton />
        </header>

        {children}
      </body>
    </html>
  );
}