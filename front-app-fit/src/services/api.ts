const API_URL = "http://localhost:8000";

export async function apiFetch(
  endpoint: string,
  options: RequestInit = {}
) {
  const token = localStorage.getItem("access_token");

  const res = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers: {
  "Content-Type": "application/json",
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
  let message = "Erro na API";

  if (typeof data?.detail === "string") {
    message = data.detail;
  } else if (data?.detail) {
    message = JSON.stringify(data.detail);
  } else if (data) {
    message = JSON.stringify(data);
  }

  const error: any = new Error(message);
  error.status = res.status;
  error.data = data;

  console.error("API ERROR:", data); // 🔥 importante

  throw error;
}}