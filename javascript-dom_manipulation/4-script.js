document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("#add_item").addEventListener("click", () => {
    const newItem = document.createElement("li");
    newItem.textContent = "Item";
    document.querySelector(".my_list").appendChild(newItem);
  });
});
