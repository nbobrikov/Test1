document.getElementById("btn").addEventListener("click", async () => {
  try {
    // пример запроса к backend (замени URL на свой Render backend)
    const response = await fetch("https://your-backend.onrender.com/api/hello");
    const data = await response.json();
    document.getElementById("output").textContent = data.message;
  } catch (err) {
    document.getElementById("output").textContent = "Ошибка соединения с бэкендом";
  }
});
