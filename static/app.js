const form = document.getElementById("chatForm");
const input = document.getElementById("msg");
const messages = document.getElementById("messages");

function addMessage(text, who="agent"){
  const el = document.createElement("div");
  el.className = "msg " + (who==="user" ? "user" : "agent");
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.innerText = text;
  el.appendChild(bubble);
  messages.appendChild(el);
  messages.scrollTop = messages.scrollHeight;
}

form.addEventListener("submit", async (e)=>{
  e.preventDefault();
  const txt = input.value.trim();
  if(!txt) return;
  addMessage(txt, "user");
  input.value = "";
  addMessage("…thinking", "agent"); // temporary placeholder

  try {
    const resp = await fetch("/api/chat", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({message: txt})
    });
    const data = await resp.json();
    // remove the last "thinking" agent placeholder
    const last = messages.lastElementChild;
    if(last && last.querySelector && last.querySelector(".bubble").innerText === "…thinking"){
      messages.removeChild(last);
    }
    if(data && data.reply){
      addMessage(data.reply, "agent");
      if(data.escalation){
        addMessage("If you are in immediate danger, please contact local emergency services right away.", "agent");
      }
    } else {
      addMessage("Sorry, something went wrong. Try again.", "agent");
    }
  } catch (err) {
    // remove "thinking"
    const last = messages.lastElementChild;
    if(last && last.querySelector && last.querySelector(".bubble").innerText === "…thinking"){
      messages.removeChild(last);
    }
    addMessage("Network error. Make sure the backend is running.", "agent");
    console.error(err);
  }
});
