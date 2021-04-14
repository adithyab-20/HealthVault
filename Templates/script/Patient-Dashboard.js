window.onload = forfirst;

function forfirst(){
    document.getElementById("p-info").style.display = "block";
    document.getElementById("l-diagnosis").style.display = "none";
    document.getElementById("prescrips").style.display = "none";
    document.getElementById("btn1").style.backgroundColor = "white";
    document.getElementById("btn2").style.background = "none"
    document.getElementById("btn3").style.background = "none";
    document.getElementById("btn1").style.borderBottom = "1px solid black"
    document.getElementById("btn2").style.borderBottom = "none"
    document.getElementById("btn3").style.borderBottom = "none"
}

function forsecond(){
    document.getElementById("p-info").style.display = "none";
    document.getElementById("l-diagnosis").style.display = "block";
    document.getElementById("prescrips").style.display = "none";
    document.getElementById("btn1").style.background = "none";
    document.getElementById("btn2").style.backgroundColor = "white";
    document.getElementById("btn3").style.background = "none";
    document.getElementById("btn1").style.borderBottom = "none"
    document.getElementById("btn2").style.borderBottom = "1px solid black"
    document.getElementById("btn3").style.borderBottom = "none"
}

function forthird(){
    document.getElementById("p-info").style.display = "none";
    document.getElementById("l-diagnosis").style.display = "none";
    document.getElementById("prescrips").style.display = "block";
    document.getElementById("btn1").style.background = "none";
    document.getElementById("btn2").style.background = "none";
    document.getElementById("btn3").style.backgroundColor = "white";
    document.getElementById("btn1").style.borderBottom = "none"
    document.getElementById("btn2").style.borderBottom = "none"
    document.getElementById("btn3").style.borderBottom = "1px solid black"
}