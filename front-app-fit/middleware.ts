//middleware serve para interceptar as requisições e respostas, podendo modificar ou adicionar informações antes de chegar ao destino final

import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  const token = request.cookies.get("access_token");

  const isAuthPage = request.nextUrl.pathname === "/login";

  // não logado tentando acessar dashboard
  if (!token && !isAuthPage) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  // logado tentando acessar login
  if (token && isAuthPage) {
    return NextResponse.redirect(new URL("/dashboard", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/login"],
};