import { apiFetch } from "./api";

type LoginResponse = {
  access_token: string;
  refresh_token: string;
  token_type: string;
};

export async function loginRequest(
  email: string,
  password: string
): Promise<LoginResponse> {
  const data = await apiFetch("/auth/login", {
    method: "POST",
    body: JSON.stringify({ email, password }),
  });

  return data;
}

export function saveTokens(data: LoginResponse) {
  localStorage.setItem("access_token", data.access_token);
  localStorage.setItem("refresh_token", data.refresh_token);
}

export function clearTokens() {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
}