document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("#red_header").addEventListener("click", () => {
    document.querySelector("header").classList.add("red");
  });
});
