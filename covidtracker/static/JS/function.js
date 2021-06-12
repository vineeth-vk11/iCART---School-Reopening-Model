document.getElementById("form1").addEventListener("submit",submitf)

function submitf(e){
    e.preventDefault();
    console.log("clicked")
    //let email = document.getElementById("login-email").value;
  //let pwd = document.getElementById("login-password").value;
  fetch("http://127.0.0.1:5000/home", {
    method: "POST",
    headers: {
      Accept: "application/json,*/*",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      msg:"Hello"
    }),
  })
    .then((res) => res.json())
    .then((res) => {
      console.log(res);
    })
    .catch((error) => console.error("Error:", error));
}