let form = document.getElementById("noteForm");
let input = document.getElementById("noteInput");
let list = document.getElementById("notesList");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    if (input.value.trim() === "") return;

    // create li
    let li = document.createElement("li");
    li.textContent = input.value;

    let span = document.createElement("span");
    span.textContent = input.value;
    span.className = "note-card";
    

    // create delete button
    const btn = document.createElement("button");
    btn.textContent = "X";
    btn.className = "delete-btn";
    

    btn.addEventListener("click", function () {
        li.remove();
    });
    
    li.appendChild(span);
    li.appendChild(btn);
    list.appendChild(li);

    input.value = "";
});