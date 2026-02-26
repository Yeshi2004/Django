document.getElementById("button1").addEventListener("click",function(){
    let note=document.getElementById("notes").value;
    if(note==""){
        return false;
        }

    let li=document.createElement("li");
    li.className = "note-card";

    let span = document.createElement("span");
    span.textContent = note;

    let delBtn = document.createElement("button");
    delBtn.textContent = "X";
    delBtn.className="delete-btn";

    delBtn.addEventListener("click", function () {
    li.remove();
    });

    li.appendChild(span);
    li.appendChild(delBtn);

    document.getElementById("noteList").appendChild(li);
    document.getElementById("notes").value = "";
    });