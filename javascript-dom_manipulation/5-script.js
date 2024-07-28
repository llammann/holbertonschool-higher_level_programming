document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("#update_header").addEventListener("click", () => {
    document.querySelector("header").textContent = "New Header!!!";
  });
});
