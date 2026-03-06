
async function analyzeCode(){

const code = document.getElementById("codeInput").value;

const response = await fetch("http://127.0.0.1:5000/analyze",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body: JSON.stringify({code:code})
});

const data = await response.json();

document.getElementById("result").innerText = data.analysis;

}
