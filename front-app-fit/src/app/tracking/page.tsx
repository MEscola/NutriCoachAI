"use client";

import { useEffect, useState } from "react";
import { apiFetch } from "@/services/api";

export default function TrackingPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    apiFetch("/tracking").then(setData);
  }, []);

  return (
    <div>
      <h1>Tracking</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}