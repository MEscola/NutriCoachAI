const API_URL = "http://localhost:8000";

export async function apiFetch(
  endpoint: string,
  options: RequestInit = {}
) {
  const token = localStorage.getItem("access_token");

  const res = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers: {
      ...(options.body && { "Content-Type": "application/json" }),
      ...(token && { Authorization: `Bearer ${token}` }),
      ...(options.headers || {}),
    },
  });

  let data;
  try {
    data = await res.json();
  } catch {
    data = null;
  }

  if (!res.ok) {
    const error: any = new Error(data?.detail || "Erro na API");
    error.status = res.status;
    error.data = data;

    throw error;
  }

  return data;
}