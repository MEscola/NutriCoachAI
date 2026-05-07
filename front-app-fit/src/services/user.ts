import { apiFetch } from "./api";

export async function getUserProfile() {
  return apiFetch("/user/me");
}