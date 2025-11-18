import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    setSummary("");
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/file", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setSummary(data.summary || JSON.stringify(data));
    } catch (err) {
      setSummary("Erreur lors de la requête.");
    }
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 400, margin: "2rem auto", padding: "2rem", border: "1px solid #ccc", borderRadius: 8 }}>
      <h2>Test API résumé audio</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="audio/*" onChange={handleFileChange} />
        <button type="submit" disabled={loading} style={{ marginTop: 10 }}>
          {loading ? "Traitement..." : "Envoyer"}
        </button>
      </form>
      {summary && (
        <div style={{ marginTop: 20 }}>
          <strong>Résumé :</strong>
          <div style={{ whiteSpace: "pre-wrap" }}>{summary}</div>
        </div>
      )}
    </div>
  );
}

export default App;