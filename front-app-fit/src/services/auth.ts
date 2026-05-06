const API_URL = "http://localhost:8000";

type LoginResponse = {
  access_token: string;
  refresh_token: string;
  token_type: string;
};

export async function loginRequest(
  email: string,
  password: string
): Promise<LoginResponse> {
  const res = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email, 
      password,
    }),
  });

  const data = await res.json();


  if (!res.ok) {
  const message =
    typeof data.detail === "string"
      ? data.detail
      : data.detail?.[0]?.msg || "Erro ao fazer login";

  throw new Error(message);
}

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