document.addEventListener("DOMContentLoaded", () => {
  const translateButton = document.getElementById("btn_translate");
  const languageSelect = document.getElementById("language_code");
  const helloDiv = document.getElementById("hello");

  translateButton.addEventListener("click", () => {
    const languageCode = languageSelect.value;
    if (languageCode) {
      const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;
      fetch(apiUrl)
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          return response.json();
        })
        .then(data => {
          helloDiv.textContent = data.hello || "Translation not found";
        })
        .catch(error => {
          console.error("Error fetching the translation:", error);
          helloDiv.textContent = "Error fetching the translation";
        });
    } else {
      helloDiv.textContent = "Please select a language code.";
    }
  });
});
