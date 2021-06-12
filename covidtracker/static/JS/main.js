var std_lower, std_upper, t_lower, t_upper, nt_lower, nt_upper;
$("#std").ionRangeSlider({
  type: "double",
  min: 15,
  max: 25,
  from: 18,
  to: 21,
  onStart: function (data) {
    std_lower = data.from;
    std_upper = data.to;
  },
  onChange: function (data) {
    console.log(data.from);
    std_lower = data.from;

    console.log("LOL", std_lower, std_upper);
  },

  onFinish: function (data) {
    console.log(data.to);
    std_upper = data.to;

    console.log("LOL", std_lower, std_upper);
  },

  onUpdate: function (data) {
    // console.log(data.from_percent);
    std_lower = data.from;
    std_upper = data.to;
  },
});
console.log("LOL", std_lower, std_upper);

$("#t").ionRangeSlider({
  type: "double",
  min: 25,
  max: 50,
  from: 30,
  to: 45,
  onStart: function (data) {
    t_lower = data.from;
    t_upper = data.to;
  },
  onChange: function (data) {
    console.log(data.from);
    t_lower = data.from;

    console.log("LOLL", t_lower, t_upper);
  },

  onFinish: function (data) {
    console.log(data.to);
    t_upper = data.to;

    console.log("LOLL", t_lower, t_upper);
  },

  onUpdate: function (data) {
    console.log("LOLL", t_lower, t_upper);
    console.log(data.from_percent);
    t_lower = data.from;
    t_upper = data.to;
  },
});
$("#nt").ionRangeSlider({
  type: "double",
  min: 25,
  max: 60,
  from: 30,
  to: 50,
  onStart: function (data) {
    nt_lower = data.from;
    nt_upper = data.to;
  },
  onChange: function (data) {
    console.log(data.from);
    nt_lower = data.from;
    nt_upper = data.to;
  },

  onFinish: function (data) {
    console.log(data.to);
    nt_lower = data.from;
    nt_upper = data.to;
  },

  onUpdate: function (data) {
    console.log(data.from_percent);
    nt_lower = data.from;
    nt_upper = data.to;
  },
});
// document.getElementById("form1").addEventListener("submit",submitf)

// function submitf(e){
//     e.preventDefault();
//     let s=document.getElementById("student").value
// let t=document.getElementById("teacher").value
// let nt=document.getElementById("nonteacher").value
// let avg=document.getElementById("batch").value
// console.log("HI",s,t,nt)
//     console.log("clicked")
//     //let email = document.getElementById("login-email").value;
//   //let pwd = document.getElementById("login-password").value;
//   fetch("http://127.0.0.1:5000/home", {
//     method: "POST",
//     headers: {
//       Accept: "application/json,*/*",
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//         s:parseInt(s),
//         t:parseInt(t),
//         nt:parseInt(nt),
//         avg:parseInt(avg),
//         slower:std_lower,
//         supper:std_upper,
//         tlower:t_lower,
//         tupper:t_upper,
//         ntlower:nt_lower,
//         ntupper:nt_upper
//     }),
//   })
//     .then((res) => res.json())
//     .then((res) => {
//       console.log(res);
//     })
//     .catch((error) => console.error("Error:", error));
// }
