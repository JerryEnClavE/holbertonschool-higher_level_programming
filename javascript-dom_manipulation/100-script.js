document.addEventListener("DOMContentLoaded", () => {
  const addButton = document.getElementById("add_item");
  const removeButton = document.getElementById("remove_item");
  const clearButton = document.getElementById("clear_list");
  const myList = document.querySelector(".my_list");

  addButton.addEventListener("click", () => {
    const newItem = document.createElement("li");
    newItem.textContent = "Item";
    myList.appendChild(newItem);
  });

  removeButton.addEventListener("click", () => {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  });

  clearButton.addEventListener("click", () => {
    myList.innerHTML = "";
  });
});
