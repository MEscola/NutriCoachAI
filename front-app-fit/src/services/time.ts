export function getCurrentTime() {
  const now = new Date();

  const hours = String(now.getHours()).padStart(2, "0");
  const minutes = String(now.getMinutes()).padStart(2, "0");
  const seconds = String(now.getSeconds()).padStart(2, "0");

  return `${hours}:${minutes}:${seconds}`;
}


export function welcomeMessage() {
  const now = new Date();
  const hours = now.getHours();

  if (hours < 12) {
    return " Bom dia";
  } else if (hours < 18) {
    return "Boa tarde";
  } else {
    return "Boa noite";
  } 
}