var title_div = document.getElementById("body-div__main-content-div__create-form__title-description");

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
var finish = document.getElementById("finish")

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

var title = document.getElementById("title")
var description = document.getElementById("description")
var prompt1 = document.getElementById('prompt1')
var prompt2 = document.getElementById('prompt2')
var prompt3 = document.getElementById('prompt3')
var prompt4 = document.getElementById('prompt4')
var prompt5 = document.getElementById('prompt5')
var prompt6 = document.getElementById('prompt6')
var prompt7 = document.getElementById('prompt7')
var prompt8 = document.getElementById('prompt8')
var prompt9 = document.getElementById('prompt9')
var prompt10 = document.getElementById('prompt10')

var a1 = document.getElementById('1a')
var b1 = document.getElementById('1b')
var c1 = document.getElementById('1c')
var d1 = document.getElementById('1d')
var e1 = document.getElementById('1e')

var a2 = document.getElementById('2a')
var b2 = document.getElementById('2b')
var c2 = document.getElementById('2c')
var d2 = document.getElementById('2d')
var e2 = document.getElementById('2e')

var a3 = document.getElementById('3a')
var b3 = document.getElementById('3b')
var c3 = document.getElementById('3c')
var d3 = document.getElementById('3d')
var e3 = document.getElementById('3e')

var a4 = document.getElementById('4a')
var b4 = document.getElementById('4b')
var c4 = document.getElementById('4c')
var d4 = document.getElementById('4d')
var e4 = document.getElementById('4e')

var a5 = document.getElementById('5a')
var b5 = document.getElementById('5b')
var c5 = document.getElementById('5c')
var d5 = document.getElementById('5d')
var e5 = document.getElementById('5e')

var a6 = document.getElementById('6a')
var b6 = document.getElementById('6b')
var c6 = document.getElementById('6c')
var d6 = document.getElementById('6d')
var e6 = document.getElementById('6e')

var a7 = document.getElementById('7a')
var b7 = document.getElementById('7b')
var c7 = document.getElementById('7c')
var d7 = document.getElementById('7d')
var e7 = document.getElementById('7e')

var a8 = document.getElementById('8a')
var b8 = document.getElementById('8b')
var c8 = document.getElementById('8c')
var d8 = document.getElementById('8d')
var e8 = document.getElementById('8e')

var a9 = document.getElementById('9a')
var b9 = document.getElementById('9b')
var c9 = document.getElementById('9c')
var d9 = document.getElementById('9d')
var e9 = document.getElementById('9e')

var a10 = document.getElementById('10a')
var b10 = document.getElementById('10b')
var c10 = document.getElementById('10c')
var d10 = document.getElementById('10d')
var e10 = document.getElementById('10e')

Next0.onclick = function() {
    if(title.value && description.value) {
        title_div.style.display = "none";
        question1.style.display = 'block';
    }
    else {
        alert("All fields must be filled in!")
    }
}

Next1.onclick = function() {
    if(prompt1.value && a1.value && b1.value && c1.value && d1.value && e1.value) {
        question1.style.display = "none";
        question2.style.display = 'block';
    }
    else {
        alert("All fields must be filled in!")
    }
}

back1.onclick = function() {
    question1.style.display = "none";
    title_div.style.display = 'block';
}

Next2.onclick = function() {
    if(prompt2.value && a2.value && b2.value && c2.value && d2.value && e2.value) {
    question2.style.display = 'none';
    question3.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back2.onclick = function() {
    question2.style.display = 'none';
    question1.style.display = 'block';
}

Next3.onclick = function() {
    if(prompt3.value && a3.value && b3.value && c3.value && d3.value && e3.value) {
    question3.style.display = 'none';
    question4.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back3.onclick = function() {
    question3.style.display = 'none';
    question2.style.display = 'block';
}

Next4.onclick = function() {
    if(prompt4.value && a4.value && b4.value && c4.value && d4.value && e4.value) {
    question4.style.display = 'none';
    question5.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back4.onclick = function() {
    question4.style.display = 'none';
    question3.style.display = 'block';
}

Next5.onclick = function() {
    if(prompt5.value && a5.value && b5.value && c5.value && d5.value && e5.value) {
    question5.style.display = 'none';
    question6.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back5.onclick = function() {
    question5.style.display = 'none';
    question4.style.display = 'block';
}

Next6.onclick = function() {
    if(prompt6.value && a6.value && b6.value && c6.value && d6.value && e6.value) {
    question6.style.display = 'none';
    question7.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back6.onclick = function() {
    question6.style.display = 'none';
    question5.style.display = 'block';
}

Next7.onclick = function() {
    if(prompt7.value && a7.value && b7.value && c7.value && d7.value && e7.value) {
    question7.style.display = 'none';
    question8.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back7.onclick = function() {
    question7.style.display = 'none';
    question6.style.display = 'block';
}

Next8.onclick = function() {
    if(prompt8.value && a8.value && b8.value && c8.value && d8.value && e8.value) {
    question8.style.display = 'none';
    question9.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back8.onclick = function() {
    question8.style.display = 'none';
    question7.style.display = 'block';
}

Next9.onclick = function() {
    if(prompt9.value && a9.value && b9.value && c9.value && d9.value && e9.value) {
    question9.style.display = 'none';
    question10.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back9.onclick = function() {
    question9.style.display = 'none';
    question8.style.display = 'block';
}

finish.onclick = function() {
    if(!prompt10.value || !a10.value || !b10.value || !c10.value || !d10.value || !e10.value) {
        alert("All fields must be filled in!")
        finish.setAttribute('type', 'button')
        }
    else if (prompt10.value && a10.value && b10.value && c10.value && d10.value && e10.value) {
        finish.setAttribute('type', 'submit')
    }
}

back10.onclick = function() {
    question10.style.display = 'none';
    question9.style.display = 'block';
}

var correct_answer_1 = document.getElementById("correct_answer_1").value
var correct_option_1 = document.getElementById(`select1${correct_answer_1}`)
correct_option_1.setAttribute("selected", "selected")

var correct_answer_2 = document.getElementById("correct_answer_2").value
var correct_option_2 = document.getElementById(`select2${correct_answer_2}`)
correct_option_2.setAttribute("selected", "selected")

var correct_answer_3 = document.getElementById("correct_answer_3").value
var correct_option_3 = document.getElementById(`select3${correct_answer_3}`)
correct_option_3.setAttribute("selected", "selected")

var correct_answer_4 = document.getElementById("correct_answer_4").value
var correct_option_4 = document.getElementById(`select4${correct_answer_4}`)
correct_option_4.setAttribute("selected", "selected")

var correct_answer_5 = document.getElementById("correct_answer_5").value
var correct_option_5 = document.getElementById(`select5${correct_answer_5}`)
correct_option_5.setAttribute("selected", "selected")

var correct_answer_6 = document.getElementById("correct_answer_6").value
var correct_option_6 = document.getElementById(`select6${correct_answer_6}`)
correct_option_6.setAttribute("selected", "selected")

var correct_answer_7 = document.getElementById("correct_answer_7").value
var correct_option_7 = document.getElementById(`select7${correct_answer_7}`)
correct_option_7.setAttribute("selected", "selected")

var correct_answer_8 = document.getElementById("correct_answer_8").value
var correct_option_8 = document.getElementById(`select8${correct_answer_8}`)
correct_option_8.setAttribute("selected", "selected")

var correct_answer_9 = document.getElementById("correct_answer_9").value
var correct_option_9 = document.getElementById(`select9${correct_answer_9}`)
correct_option_9.setAttribute("selected", "selected")

var correct_answer_10 = document.getElementById("correct_answer_10").value
var correct_option_10 = document.getElementById(`select10${correct_answer_10}`)
correct_option_10.setAttribute("selected", "selected")