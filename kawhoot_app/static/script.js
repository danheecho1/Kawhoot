var title = document.getElementById("body-div__main-content-div__create-form__title-description");

var question1 = document.getElementById("question1")
var question2 = document.getElementById("question2")
var question3 = document.getElementById("question3")
var question4 = document.getElementById("question4")
var question5 = document.getElementById("question5")
var question6 = document.getElementById("question6")
var question7 = document.getElementById("question7")
var question8 = document.getElementById("question8")
var question9 = document.getElementById("question9")
var question10 = document.getElementById("question10")

var Next0 = document.getElementById("next0")
var Next1 = document.getElementById("next1")
var Next2 = document.getElementById("next2")
var Next3 = document.getElementById("next3")
var Next4 = document.getElementById("next4")
var Next5 = document.getElementById("next5")
var Next6 = document.getElementById("next6")
var Next7 = document.getElementById("next7")
var Next8 = document.getElementById("next8")
var Next9 = document.getElementById("next9")

var back1 = document.getElementById("back1")
var back2 = document.getElementById("back2")
var back3 = document.getElementById("back3")
var back4 = document.getElementById("back4")
var back5 = document.getElementById("back5")
var back6 = document.getElementById("back6")
var back7 = document.getElementById("back7")
var back8 = document.getElementById("back8")
var back9 = document.getElementById("back9")
var back10 = document.getElementById("back10")

Next0.onclick = function() {
    title.style.display = "none";
    question1.style.display = 'block';
}

Next1.onclick = function() {
    question1.style.display = "none";
    question2.style.display = 'block';
}

back1.onclick = function() {
    question1.style.display = "none";
    title.style.display = 'block';
}

Next2.onclick = function() {
    question2.style.display = 'none';
    question3.style.display = 'block';
}

back2.onclick = function() {
    question2.style.display = 'none';
    question1.style.display = 'block';
}